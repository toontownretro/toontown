DBSERVER_GET_ESTATE = 1040
DBSERVER_GET_ESTATE_RESP = 1041

DBSERVER_ID = 4003
DATABASE_OBJECT_TYPE_ESTATE  = 3
DATABASE_OBJECT_TYPE_HOUSE   = 4

-- Every single required db fields for DistributedEstate:
ESTATE_FIELDS = {"setEstateType", "setDecorData", "setRentalTimeStamp",
                 "setRentalType", "setSlot0ToonId", "setSlot0Items",
                 "setSlot1ToonId", "setSlot1Items", "setSlot2ToonId",
                 "setSlot4ToonId", "setSlot4Items", "setSlot5ToonId",
                 "setSlot2Items", "setSlot3ToonId", "setSlot3Items",
                 "setSlot5Items", "setLastEpochTimeStamp"
                }

-- Every single required db fields for DistributedHouse
HOUSE_FIELDS = {"setHouseType", "setGardenPos", "setAvatarId", "setName",
                "setAtticItems", "setInteriorItems", "setAtticWallpaper",
                "setInteriorWallpaper", "setAtticWindows", "setInteriorWindows",
                "setDeletedItems"
               }

-- Toon's name for the house and pet id for response message
TOON_FIELDS = {"setName", "setHouseId", "setPetId"}

-- Helper functions:
function table.length(t)
    -- Since there's no shortcut for counting the length of key-based tables,
    -- we have to do it ourselves.
    local total = 0
    for k, v in pairs(t) do
        total = total + 1
    end
    return total
end

function table.shallow_copy(t)
    local t2 = {}
    for k,v in pairs(t) do
      t2[k] = v
    end
    return t2
end

local inspect = require('inspect')

function init(participant)
    participant:subscribeChannel(DBSERVER_GET_ESTATE)
end

function handleDatagram(participant, msgType, dgi)
    if msgType == DBSERVER_GET_ESTATE then
        handleGetEstate(participant, dgi)
    else
        participant:warning(string.format("Got unknown message type: %d", msgType))
    end
end

function sendError(participant, sender, context)
    dg = datagram:new()
    dg:addServerHeader(sender, DBSERVER_GET_ESTATE, DBSERVER_GET_ESTATE_RESP)
    dg:addUint32(context)
    dg:addUint8(1)
    participant:routeDatagram(dg)
end

function handleGetEstate(participant, dgi)
    local sender = participant:getSender()
    local context = dgi:readUint32()
    local avId = dgi:readUint32()

    participant:debug(string.format("handleGetEstate(%d, %d, %d)", sender, context, avId))

    participant:getDatabaseValues(DBSERVER_ID, avId, "DistributedToon", {"setDISLid"}, DBSERVER_GET_ESTATE, function (doId, success, fields)
        if not success then
            participant:error(string.format("Failed to get avatar %d", doId))
            sendError(participant, sender, context)
            return
        end

        if fields.setDISLid == nil then
            participant:error(string.format("Avatar %d has no setDISLid!", doId))
            sendError(participant, sender, context)
            return
        end

        fetchAccount(participant, sender, context, fields.setDISLid[1])
    end)
end

function fetchAccount(participant, sender, context, accountId)
    participant:debug(string.format("fetchAccount(%d, %d, %d)", sender, context, accountId))

    participant:getDatabaseValues(DBSERVER_ID, accountId, "Account", {"ACCOUNT_AV_SET", "ESTATE_ID", "HOUSE_ID_SET"}, DBSERVER_GET_ESTATE, function (doId, success, fields)
        if not success then
            participant:error(string.format("Failed to get account %d", doId))
            sendError(participant, sender, context)
            return
        end

        if fields.ACCOUNT_AV_SET == nil then
            participant:error(string.format("Account %d has no avatars!", doId))
            sendError(participant, sender, context)
            return
        elseif #fields.ACCOUNT_AV_SET ~= 6 then
            participant:error(string.format("Account %d has too many/few avatars!  Length is %d", doId, #fields.ACCOUNT_AV_SET))
            sendError(participant, sender, context)
        end

        if fields.ESTATE_ID == 0 or fields.ESTATE_ID == nil then
            createNewEstate(participant, sender, context, accountId, fields)
        else
            fetchExistingEstate(participant, sender, context, accountId, fields)
        end
    end)
end

function createNewEstate(participant, sender, context, accountId, accountFields)
    participant:debug(string.format("createNewEstate(%d, %d)", context, accountId))
    -- Generate new estate with default values:
    participant:createDatabaseObject(DBSERVER_ID, "DistributedEstate", {setLastEpochTimeStamp = {os.time()}}, DATABASE_OBJECT_TYPE_ESTATE, DBSERVER_GET_ESTATE, function (estateId)
        if estateId == 0 then
            participant:error("Estate creation failed!")
            sendError(participant, sender, context)
            return
        end

        participant:debug(string.format("Successfully created new estate: %d", estateId))

        -- Store our new estateId in the database
        participant:setDatabaseValues(accountId, DBSERVER_ID, "Account", {
            ESTATE_ID = estateId
        })
        accountFields.ESTATE_ID = estateId
        gotEstate(participant, sender, context, accountId, accountFields, {})
    end)
end

function fetchExistingEstate(participant, sender, context, accountId, accountFields)
    participant:getDatabaseValues(DBSERVER_ID, accountFields.ESTATE_ID, "DistributedEstate", ESTATE_FIELDS, DBSERVER_GET_ESTATE, function (estateId, success, fields)
        if estateId == 0 then
            participant:error(string.format("Could not find estate of id: %d", estateId))
            sendError(participant, sender, context)
            return
        end
        gotEstate(participant, sender, context, accountId, accountFields, fields)
    end)
end

function gotEstate(participant, sender, context, accountId, accountFields, estateFields)
    participant:debug(string.format("gotEstate(%d, %d %d)", sender, context, accountId))

    -- Now to get the houses for each avatar.
    local houseFields = {{}, {}, {}, {}, {}, {}}
    local houseIds = table.shallow_copy(accountFields.HOUSE_ID_SET)
    local numGotHouses = 0

    local function fixHouseIdSet()
        for i, houseId in ipairs(houseIds) do
            if houseId ~= accountFields.HOUSE_ID_SET[i] then
                -- Update HOUSE_ID_SET in database.
                participant:setDatabaseValues(accountId, DBSERVER_ID, "Account", {
                    HOUSE_ID_SET = houseIds
                })
                accountFields.HOUSE_ID_SET = houseIds
                return
            end
        end
    end


    for i, houseId in ipairs(houseIds) do
        local function queryHouseResponse (doId, success, fields)
            if doId == 0 then
                participant:error(string.format("Could not find house of id: %d", houseId))
                sendError(participant, sender, context)
                return
            end
            houseFields[i] = fields
            numGotHouses = numGotHouses + 1
            if numGotHouses == #houseFields then
                fixHouseIdSet()
                gotHouses(participant, sender, context, accountFields, estateFields, houseFields)
            end
        end

        if houseId > 0 then
            -- Fetch existing house
            participant:getDatabaseValues(DBSERVER_ID, houseId, "DistributedHouse", HOUSE_FIELDS, DBSERVER_GET_ESTATE, queryHouseResponse)
        else
            -- Create new house
            participant:debug(string.format("Creating new house for index %d", i))
            participant:createDatabaseObject(DBSERVER_ID, "DistributedHouse", {}, DATABASE_OBJECT_TYPE_HOUSE, DBSERVER_GET_ESTATE, function (houseId)
                if houseId == 0 then
                    participant:error("House creation failed!")
                    sendError(participant, sender, context)
                    return
                end
                participant:debug(string.format("New house id: %d", houseId))
                houseIds[i] = houseId
                participant:getDatabaseValues(DBSERVER_ID, houseId, "DistributedHouse", HOUSE_FIELDS, DBSERVER_GET_ESTATE, queryHouseResponse)
            end)
        end
    end
end

function gotHouses(participant, sender, context, accountFields, estateFields, houseFields)
    participant:debug(string.format("gotHouses(%d, %d)", sender, context))
    -- Now get the avatar associated for each house if any.
    local numGotAvatars = 0
    local petIds = {}

    for i, avatarId in ipairs(accountFields.ACCOUNT_AV_SET) do
        if avatarId == 0 then
            -- Skip if there's no avatar for that house
            numGotAvatars = numGotAvatars + 1
            if numGotAvatars == #accountFields.ACCOUNT_AV_SET then
                finish(participant, sender, context, accountFields, estateFields, houseFields, petIds)
            end
        else
            local function queryAvatarResponse(avatarId, success, fields)
                if avatarId == 0 then
                    participant:error(string.format("Could not find avatar of id: %d", avatarId))
                    sendError(participant, sender, context)
                    return
                end
                if fields.setHouseId[1] ~= accountFields.HOUSE_ID_SET[i] then
                    -- Update the house id for that avatar
                    participant:sendUpdate(avatarId, avatarId, "DistributedToon", "setHouseId", {accountFields.HOUSE_ID_SET[i]})
                end

                -- Update setAvatarId and setName if any changes were found:
                if houseFields[i].setAvatarId ~= {avatarId} then
                    houseFields[i].setAvatarId = {avatarId}
                    participant:setDatabaseValues(accountFields.HOUSE_ID_SET[i], DBSERVER_ID, "DistributedHouse", {
                        setAvatarId = {avatarId}
                    })
                end
                if houseFields[i].setName ~= fields.setName then
                    houseFields[i].setName = fields.setName
                    participant:setDatabaseValues(accountFields.HOUSE_ID_SET[i], DBSERVER_ID, "DistributedHouse", {
                        setName = fields.setName
                    })
                end

                if fields.setPetId[1] ~= 0 then
                    table.insert(petIds, fields.setPetId[1])
                end
                numGotAvatars = numGotAvatars + 1
                if numGotAvatars == #accountFields.ACCOUNT_AV_SET then
                    finish(participant, sender, context, accountFields, estateFields, houseFields, petIds)
                end
            end
        participant:getDatabaseValues(DBSERVER_ID, avatarId, "DistributedToon", TOON_FIELDS, DBSERVER_GET_ESTATE, queryAvatarResponse)
        end
    end
end

function finish(participant, sender, context, accountFields, estateFields, houseFields, petIds)
    participant:debug(string.format("finish(%d, %d)", sender, context))

    -- Finally, we're done.  Create and send the response message!
    dg = datagram:new()
    dg:addServerHeader(sender, DBSERVER_GET_ESTATE, DBSERVER_GET_ESTATE_RESP)
    dg:addUint32(context)
    dg:addUint8(0)

    dg:addUint32(accountFields.ESTATE_ID) -- estateId
    dg:addUint16(table.length(estateFields)) --numFields
    for name, value in pairs(estateFields) do
        dg:addString(name)
        participant:packFieldToDatagram(dg, "DistributedEstate", name, value, false, true) -- value
        dg:addUint8(1) -- found
    end

    dg:addUint16(#accountFields.HOUSE_ID_SET) -- numHouses
    for _, houseId in ipairs(accountFields.HOUSE_ID_SET) do
        dg:addUint32(houseId) -- houseId
    end

    -- Length of house fields
    dg:addUint16(#HOUSE_FIELDS) -- numHouseKeys
    -- Field keys
    for _, name in pairs(HOUSE_FIELDS) do
        dg:addString(name)
    end

    -- Length of house values
    dg:addUint16(#HOUSE_FIELDS) -- numHouseVal
    --
    for _, name in pairs(HOUSE_FIELDS) do
        dg:addUint16(#accountFields.HOUSE_ID_SET) -- numHouses2 ¯\_(ツ)_/¯
        for i, houseId in ipairs(accountFields.HOUSE_ID_SET) do
            if houseFields[i][name] ~= nil then
                participant:packFieldToDatagram(dg, "DistributedHouse", name, houseFields[i][name], false, true) -- tempHouseVal
            else
                dg:addString("")
            end
        end
    end

    dg:addUint16(0) -- numHouseFound (UNUSED)
    for _, name in pairs(HOUSE_FIELDS) do
        dg:addUint16(0) -- hvLen (UNUSED)
        for i, houseId in ipairs(accountFields.HOUSE_ID_SET) do
            local found = 0
            if houseFields[i][name] ~= nil then
                found = 1
            end
            dg:addUint8(found) -- found
        end
    end

    dg:addUint16(#petIds) -- numPets
    for _, petId in ipairs(petIds) do
        dg:addUint32(petId) -- petId
    end

    participant:routeDatagram(dg)
end
