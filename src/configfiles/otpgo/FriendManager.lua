OTP_DO_ID_FRIEND_MANAGER = 4501
STATESERVER_OBJECT_UPDATE_FIELD = 2004

DBSERVER_ID = 4003

CONTEXT = 0
invitesByContext = {} -- context: invite
invitesByInviterId = {} -- inviterId: invite
invitesByInviteeId = {} -- inviteeId: invite

inviteeDeclinedInvierId = {} -- inviteeId[inviterId]: response

-- OTPGlobals.MaxFriends
MAX_FRIENDS = 50

-- This is the length of time that should elapse before we start to
-- forget who has declined friendships from whom.
DECLINE_FRIENDSHIP_TIMEOUT = 600

-- Friend related messages
TOONTOWNCLIENT_MAKE_FRIEND = 3504

-- Internal messages (used exclusively for TransporterManager)
FRIENDMANAGER_REGISTER_INTERNAL_SENDER = 10000
FRIENDMANAGER_QUERY_FRIEND = 10001
FRIENDMANAGER_INVITEE_FRIEND_QUERY = 10002
FRIENDMANAGER_INVITEE_FRIEND_CONSIDERING = 10003
FRIENDMANAGER_INVITEE_FRIEND_RESPONSE = 10004
FRIENDMANAGER_CANCEL_FRIEND_QUERY = 10005

local inspect = require('inspect')

local senderByAvatarId = {} -- avId: channel

-- Load the configuration varables (see config.example.lua)
dofile("config.lua")

-- Character set for secret friend codes
local charset = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","z","y","w","q","1","2","3","4","5","6","7","8","9","0"}

-- From: https://stackoverflow.com/a/2282547
function tableContains(table, key)
    return table[key] ~= nil
end

function init(participant)
    participant:subscribeChannel(OTP_DO_ID_FRIEND_MANAGER)
end

function newInviteTable(context, inviterId, inviterFields, inviteeId, inviteeFields)
    return {
        context = context,
        inviterId = inviterId,
        inviterFields = inviterFields,
        inviteeId = inviteeId,
        inviteeFields = inviteeFields,
        inviteeKnows = false,
        sendSpecialResponse = 0
    }
end

function handleDatagram(participant, msgType, dgi)
    if msgType == STATESERVER_OBJECT_UPDATE_FIELD then
        if dgi:readUint32() == OTP_DO_ID_FRIEND_MANAGER then
            participant:handleUpdateField(dgi, "FriendManager")
        end
    elseif msgType == FRIENDMANAGER_REGISTER_INTERNAL_SENDER then
        handleRegister(participant, dgi)
    elseif msgType == FRIENDMANAGER_QUERY_FRIEND then
        handleFriendQuery(participant, dgi)
    elseif msgType == FRIENDMANAGER_INVITEE_FRIEND_RESPONSE then
        handleFriendResponse(participant, dgi)
    elseif msgType == FRIENDMANAGER_CANCEL_FRIEND_QUERY then
        handleCancelFriendQuery(participant, dgi)
    else
        participant:warn(string.format("Got unknown message: %d", msgType))
    end
end

-- Messages sent internally (AI)
function handleRegister(participant, dgi)
    local sender = participant:getSender()
    local avatarId = dgi:readUint32()

    participant:debug(string.format("handleRegister(%d, %d)", avatarId, sender))
    senderByAvatarId[avatarId] = sender
end

function handleFriendQuery(participant, dgi)
    local inviterId = dgi:readUint32()
    local inviteeId = dgi:readUint32()
    beginFriendQuery(participant, inviterId, inviteeId)
end

function handleFriendResponse(participant, dgi)
    local response = dgi:readUint8()
    local context = dgi:readUint32()
    handleFriendManager_inviteeFriendResponse(participant, 0, {response, context})
end

function handleCancelFriendQuery(participant, dgi)
    local context = dgi:readUint32()

    local invite = invitesByContext[context]
    if invite == nil then
        participant:error(string.format("got cancelFriendQuery from AI for unknown context %d!", context))
        return
    end

    cancelInvite(participant, invite)
end

-- Messages sent from inviter client to OTP:
function handleFriendManager_friendQuery(participant, fieldId, data)
    -- The sender is stored internally in Go, because Lua has no native
    -- uint64 support (all of Lua numbers are of float64 type).
    local inviterId = participant:getAvatarIdFromSender()
    local inviteeId = data[1]

    -- Sent by the inviter to initiate a friendship request.
    participant:debug(string.format("friendQuery(%d, %d)", inviterId, inviteeId))
    beginFriendQuery(participant, inviterId, inviteeId)
end

function beginFriendQuery(participant, inviterId, inviteeId)
    local avatarFields = {}
    local gotInviterFields = false
    local gotInviteeFields = false

    local function queryAvatarResponse(doId, success, fields)
        -- Go will print an error if its not successful.
        if success then
            if doId == inviterId then
                gotInviterFields = true
            elseif doId == inviteeId then
                gotInviteeFields = true
            else
                participant:error(string.format("queryAvatarResponse: Got results for unknown ID %d!", doId))
            end
            avatarFields[doId] = fields
        end
        if gotInviterFields and gotInviteeFields then
            -- We got all the avatars we need.
            invite = newInviteTable(CONTEXT, inviterId, avatarFields[inviterId], inviteeId, avatarFields[inviteeId])
            CONTEXT = CONTEXT + 1
            beginInvite(participant, invite)
        end
    end

    -- Now we query the fields from the State Server (this is assuming they are alive)
    participant:queryObjectFields(inviterId, "DistributedToon", {"setName", "setFriendsList", "setDNAString"}, OTP_DO_ID_FRIEND_MANAGER, queryAvatarResponse)
    participant:queryObjectFields(inviteeId, "DistributedToon", {"setFriendsList"}, OTP_DO_ID_FRIEND_MANAGER, queryAvatarResponse)
end

function beginInvite(participant, invite)
    -- If the invitee has previously (recently) declined a
    -- friendship from this inviter, don't ask again.
    if inviteeDeclinedInvierId[invite.inviteeId] ~= nil then
        declineResponse = inviteeDeclinedInvierId[invite.inviteeId][invite.inviterId]
        if declineResponse ~= nil then
            if tableContains(senderByAvatarId, invite.inviterId) then
                local dg = datagram:new()
                dg:addServerHeader(senderByAvatarId[invite.inviterId], OTP_DO_ID_FRIEND_MANAGER, FRIENDMANAGER_INVITEE_FRIEND_CONSIDERING)
                dg:addUint32(invite.inviterId)
                dg:addUint8(declineResponse)
                dg:addUint32(invite.context)
                participant:routeDatagram(dg)
            else
                participant:sendUpdateToAvatarId(invite.inviterId, OTP_DO_ID_FRIEND_MANAGER,
                    "FriendManager", "friendConsidering", {declineResponse, invite.context})
            end
            clearInvite(invite)
            return
        end
    end

    if invite.inviterId == invite.inviteeId then
        -- You can't be friends with yourself.
        return
    end

    -- If the inviter is already involved in some other context,
    -- that one is now void.
    if tableContains(invitesByInviterId, invite.inviterId) then
        cancelInvite(participant, invitesByInviterId[invite.inviterId])
    end

    invitesByContext[invite.context] = invite
    invitesByInviterId[invite.inviterId] = invite
    invitesByInviteeId[invite.inviteeId] = invite

    -- Ask the invitee if he is available to consider being
    -- someone's friend--that is, that he's not busy playing a
    -- minigame or something.

    invite["inviteeKnows"] = true
    participant:debug(string.format("inviteeFriendQuery(%d, %s, dna, %d)",
        invite.inviterId, invite.inviterFields.setName[1], invite.context))
    if tableContains(senderByAvatarId, invite.inviteeId) then
        local dg = datagram:new()
        dg:addServerHeader(senderByAvatarId[invite.inviteeId], OTP_DO_ID_FRIEND_MANAGER, FRIENDMANAGER_INVITEE_FRIEND_QUERY)
        dg:addUint32(invite.inviteeId)
        dg:addUint32(invite.inviterId)
        dg:addUint32(invite.context)
        dg:addString(invite.inviterFields.setName[1])
        dg:addString(invite.inviterFields.setDNAString[1])
        participant:routeDatagram(dg)
    else
        participant:sendUpdateToAvatarId(invite.inviteeId, OTP_DO_ID_FRIEND_MANAGER,
            "FriendManager", "inviteeFriendQuery", {invite.inviterId,
            invite.inviterFields.setName[1], invite.inviterFields.setDNAString[1], invite.context})
    end
end

function clearInvite(invite)
    if tableContains(invitesByContext, invite.context) then
        invitesByContext[invite.context] = nil
    end
    if tableContains(invitesByInviterId, invite.inviterId) then
        invitesByInviterId[invite.inviterId] = nil
    end
    if tableContains(invitesByInviteeId, invite.inviteeId) then
        invitesByInviteeId[invite.inviteeId] = nil
    end
end

function handleFriendManager_inviteeFriendConsidering(participant, fieldId, data)
    local response = data[1]
    local context = data[2]
    local inviteeId = participant:getAvatarIdFromSender()

    -- Sent by the invitee to indicate whether the invitee
    -- is able to consider the request right now.

    -- The responses are:
    -- 0 - no
    -- 1 - yes
    -- 4 - the invitee is ignoring you.
    participant:debug(string.format("inviteeFriendConsidering(%d, %d)", response, context))

    local invite = invitesByContext[context]
    if invite == nil then
        participant:writeServerEvent("suspicious", "FriendManager", inviteeId, string.format("inviteeFriendConsidering unknown context|%d", context))
        participant:error(string.format("got inviteeFriendConsidering for unknown context %d!", context))
        return
    end

    if tableContains(senderByAvatarId, invite.inviterId) then
        local dg = datagram:new()
        dg:addServerHeader(senderByAvatarId[invite.inviterId], OTP_DO_ID_FRIEND_MANAGER, FRIENDMANAGER_INVITEE_FRIEND_CONSIDERING)
        dg:addUint32(invite.inviterId)
        dg:addUint8(response)
        dg:addUint32(context)
        participant:routeDatagram(dg)
    else
        participant:sendUpdateToAvatarId(invite.inviterId, OTP_DO_ID_FRIEND_MANAGER,
            "FriendManager", "friendConsidering", {response, context})
    end
    if response ~= 1 then
        -- Cannot make the request for one of these reasons:
        -- 0 - the invitee is busy
        -- 2 - the invitee is already your friend
        -- 3 - the invitee is yourself
        -- 4 - the invitee is ignoring you.
        -- 6 - the invitee not accepting friends
        clearInvite(invite)
    end
end

function handleFriendManager_inviteeFriendResponse(participant, fieldId, data)
    local yesNoMaybe = data[1]
    local context = data[2]
    local inviteeId = participant:getAvatarIdFromSender()

    -- Sent by the invitee to the AI, following an affirmative
    -- response in inviteeFriendConsidering, to indicate whether or
    -- not the user decided to accept the friendship.

    participant:debug(string.format("inviteeFriendResponse(%d, %d)", yesNoMaybe, context))

    local invite = invitesByContext[context]
    if invite == nil then
        participant:writeServerEvent("suspicious", "FriendManager", inviteeId, string.format("inviteeFriendResponse unknown context|%d", context))
        participant:error(string.format("got inviteeFriendResponse for unknown context %d!", context))
        return
    end

    if tableContains(senderByAvatarId, invite.inviterId) then
        local dg = datagram:new()
        dg:addServerHeader(senderByAvatarId[invite.inviterId], OTP_DO_ID_FRIEND_MANAGER, FRIENDMANAGER_INVITEE_FRIEND_RESPONSE)
        dg:addUint32(invite.inviterId)
        dg:addUint8(yesNoMaybe)
        dg:addUint32(context)
        participant:routeDatagram(dg)
    else
        participant:sendUpdateToAvatarId(invite.inviterId, OTP_DO_ID_FRIEND_MANAGER,
            "FriendManager", "friendResponse", {yesNoMaybe, context})
    end

    if yesNoMaybe == 1 then
        makeFriends(participant, invite, 0)
    else
        -- The invitee declined to make friends.
        --
        -- 0 - no
        -- 2 - unable to answer; e.g. entered a minigame or something.
        -- 3 - the invitee has too many friends already.
        if yesNoMaybe == 0 or yesNoMaybe == 3 then
            -- The user explictly said no or has too many friends.
            -- Disallow this guy from asking again for the next ten
            -- minutes or so.
            storeDeclineResponse(participant, invite.inviteeId, invite.inviterId, yesNoMaybe)
        end
        clearInvite(invite)
    end
end

function handleFriendManager_cancelFriendQuery(participant, fieldId, data)
    local context = data[1]
    local inviterId = participant:getAvatarIdFromSender()

    -- Sent by the inviter to cancel a pending friendship
    -- request.

    participant:debug(string.format("cancelFriendQuery(%d)", context))

    local invite = invitesByContext[context]
    if invite == nil then
        participant:writeServerEvent("suspicious", "FriendManager", inviterId, string.format("cancelFriendQuery unknown context|%d", context))
        participant:error(string.format("got cancelFriendQuery for unknown context %d!", context))
        return
    end

    cancelInvite(participant, invite)
end

function cancelInvite(participant, invite)
    participant:sendUpdateToAvatarId(invite.inviteeId, OTP_DO_ID_FRIEND_MANAGER,
        "FriendManager", "inviteeCancelFriendQuery", {invite.context})
end

function handleFriendManager_inviteeAcknowledgeCancel(participant, fieldId, data)
    local context = data[1]
    local inviteeId = participant:getAvatarIdFromSender()

    participant:debug(string.format("inviteeAcknowledgeCancel(%d)", context))

    local invite = invitesByContext[context]
    if invite == nil then
        participant:writeServerEvent("suspicious", "FriendManager", inviteeId, string.format("inviteeAcknowledgeCancel unknown context|%d", context))
        participant:error(string.format("got inviteeAcknowledgeCancel for unknown context %d!", context))
        return
    end

    clearInvite(invite)

end

function makeFriends(participant, invite, flag)
    local addInviteeToInviter = true
    local addInviterToInvitee = true

    for i, v in ipairs(invite.inviterFields.setFriendsList[1]) do
        if v[1] == invite.inviteeId then
            invite.inviterFields.setFriendsList[1][i][2] = flag
            addInviteeToInviter = false
            break
        end
    end

    for i, v in ipairs(invite.inviteeFields.setFriendsList[1]) do
        if v[1] == invite.inviterId then
            invite.inviteeFields.setFriendsList[1][i][2] = flag
            addInviterToInvitee = false
            break
        end
    end

    if addInviteeToInviter then
        table.insert(invite.inviterFields.setFriendsList[1], {invite.inviteeId, flag})
    end
    if addInviterToInvitee then
        table.insert(invite.inviteeFields.setFriendsList[1], {invite.inviterId, flag})
    end

    -- Send update to their avatars.
    participant:sendUpdate(invite.inviterId, invite.inviterId,
        "DistributedToon", "setFriendsList", invite.inviterFields.setFriendsList)
    participant:sendUpdate(invite.inviteeId, invite.inviteeId,
        "DistributedToon", "setFriendsList", invite.inviteeFields.setFriendsList)

    -- Tell the clients that a new friendship has been made.
    local dg = datagram:new()
    participant:addServerHeaderWithAvatarId(dg, invite.inviterId, OTP_DO_ID_FRIEND_MANAGER, TOONTOWNCLIENT_MAKE_FRIEND)
    dg:addUint32(invite.inviteeId)
    dg:addUint8(flag)
    participant:routeDatagram(dg)

    local dg = datagram:new()
    participant:addServerHeaderWithAvatarId(dg, invite.inviteeId, OTP_DO_ID_FRIEND_MANAGER, TOONTOWNCLIENT_MAKE_FRIEND)
    dg:addUint32(invite.inviterId)
    dg:addUint8(flag)
    participant:routeDatagram(dg)
end

function storeDeclineResponse(participant, inviteeId, inviterId, response)
    participant:debug(string.format("storeDeclineResponse (%d, %d, %d)", inviteeId, inviterId, response))
    if inviteeDeclinedInvierId[inviteeId] == nil then
        inviteeDeclinedInvierId[inviteeId] = {}
    end

    inviteeDeclinedInvierId[inviteeId][inviterId] = response
    participant:debug(inspect(inviteeDeclinedInvierId[inviteeId]))

    participant:doLater(DECLINE_FRIENDSHIP_TIMEOUT, function (_)
        participant:debug(string.format("DeclineResponse Timeout: Removing response from [%d][%d]", inviteeId, inviterId))
        inviteeDeclinedInvierId[inviteeId][inviterId] = nil
        participant:debug(inspect(inviteeDeclinedInvierId[inviteeId]))
        if next(inviteeDeclinedInvierId[inviteeId]) == nil then
            participant:debug(string.format("inviteeDeclinedInvierId[%d] empty; deleting", inviteeId))
            inviteeDeclinedInvierId[inviteeId] = nil
        end
    end)
end

-- Secret/True Friends
function generateSecret()
    local secret = ""
    for i = 1, 7 do
        if i == 4 then
            -- Add space in the middle
            secret = secret .. " "
            goto continue
        end
        local rdm = math.random(1,#charset)
        secret = secret .. charset[rdm]
        ::continue::
    end
    return secret
end

function loadSecretCodes(participant)
    local json = require("json")
    local io = require("io")

    local f, err = io.open(SECRET_FRIEND_STORAGE, "r")
    if err ~= nil then
        if string.find(err, "no such file or directory") ~= nil then
           participant:error(string.format("loadSecretCodes: Unable to read file %s, %s", SECRET_FRIEND_STORAGE, err))
        end
        return {}
    end

    decoder = json.new_decoder(f)
    result, err = decoder:decode()
    f:close()
    if err then
        participant:error(string.format("loadSecretCodes: Unable to decode file %s, %s", SECRET_FRIEND_STORAGE, err))
        return {}
    end

    -- Remove expired codes.
    local today = os.time()
    for code, info in pairs(result) do
        local days = math.floor(os.difftime(today, info[1]) / (24 * 60 * 60)) -- seconds in a day
        if days > 2 then
            participant:debug(string.format("loadSecretCodes: Deleting expired code: %s", code))
            result[code] = nil
        end
    end
    participant:debug(inspect(result))
    return result
end

function saveSecretCodes(participant, secrets)
    local json = require("json")
    local io = require("io")

    local f, err = io.open(SECRET_FRIEND_STORAGE, 'w')
    if err then
        participant:error(string.format("saveSecretCodes: Unable to open file %s for writing: %s", SECRET_FRIEND_STORAGE, err))
        return
    end
    local encoder = json.new_encoder(f)
    err = encoder:encode(secrets)
    if err then
        participant:error(string.format("saveSecretCodes: Unable to encode secrets for writing: %s", err))
    end
end

function handleFriendManager_requestSecret(participant, fieldId, data)
    local inviterId = participant:getAvatarIdFromSender()
    participant:debug(string.format("requestSecret(%d)", inviterId))

    -- This checks that the inviter is alive and in-game.
    participant:queryObjectFields(inviterId, "DistributedToon", {"setFriendsList"}, OTP_DO_ID_FRIEND_MANAGER, function (doId, success, fields)
        -- Go will print an error if its not successful.
        if success then
            if doId ~= inviterId then
                participant:error(string.format("queryAvatarResponse: Got results for unknown ID %d!", doId))
                return
            end
            if fields.setFriendsList == nil then
                participant:warn(string.format("requestSecret: Missing friends list for inviter %d!", inviterId))
                return
            end

            local secrets = loadSecretCodes(participant)

            local secret = ""
            local madeUniqueSecret = false
            while not madeUniqueSecret do
                secret = generateSecret()
                if not tableContains(secrets, secret) then
                    madeUniqueSecret = true
                end
            end

            secrets[secret] = {os.time(), inviterId}
            saveSecretCodes(participant, secrets)

            participant:sendUpdateToAvatarId(inviterId, OTP_DO_ID_FRIEND_MANAGER,
                "FriendManager", "requestSecretResponse", {1, secret})
        end
    end)

end

function handleFriendManager_submitSecret(participant, fieldId, data)
    local secret = data[1]
    local inviteeId = participant:getAvatarIdFromSender()
    participant:debug(string.format("submitSecret(%d, %s)", inviteeId, secret))

    local secrets = loadSecretCodes(participant)

    if secrets[secret] == nil then
        -- Invalid code
        participant:sendUpdateToAvatarId(inviteeId, OTP_DO_ID_FRIEND_MANAGER,
            "FriendManager", "submitSecretResponse", {0, 0})
        return
    end

    local inviterId = secrets[secret][2]
    secrets[secret] = nil
    saveSecretCodes(participant, secrets)

    if inviterId == inviteeId then
        -- Used own code
        participant:sendUpdateToAvatarId(inviteeId, OTP_DO_ID_FRIEND_MANAGER,
            "FriendManager", "submitSecretResponse", {3, inviterId})
        return
    end

    local avatarFields = {}
    local gotInviterFields = false
    local gotInviteeFields = false

    local function queryAvatarResponse(doId, success, fields)
        -- Go will print an error if its not successful.
        if success then
            if doId == inviterId then
                gotInviterFields = true
            elseif doId == inviteeId then
                gotInviteeFields = true
            else
                participant:error(string.format("queryAvatarResponse: Got results for unknown ID %d!", doId))
            end
            avatarFields[doId] = fields
        end
        if gotInviterFields and gotInviteeFields then
            -- We got all the avatars we need.
            invite = newInviteTable(CONTEXT, inviterId, avatarFields[inviterId], inviteeId, avatarFields[inviteeId])

            if #invite.inviterFields.setFriendsList[1] >= MAX_FRIENDS or #invite.inviteeFields.setFriendsList[1] >= MAX_FRIENDS then
                -- Full friends list
                participant:sendUpdateToAvatarId(inviteeId, OTP_DO_ID_FRIEND_MANAGER,
                    "FriendManager", "submitSecretResponse", {2, inviterId})
                return
            end

            -- Establish secret friend!
            makeFriends(participant, invite, 1)

            participant:sendUpdateToAvatarId(inviteeId, OTP_DO_ID_FRIEND_MANAGER,
                "FriendManager", "submitSecretResponse", {1, inviterId})

        end
    end
    -- Get the fields for both the inviter and invitee
    participant:queryObjectFields(inviteeId, "DistributedToon", {"setFriendsList"}, OTP_DO_ID_FRIEND_MANAGER, queryAvatarResponse)
    -- We're getting the inviter out of the database because
    -- the invitee can use the code while they are offline.
    participant:getDatabaseValues(DBSERVER_ID, inviterId, "DistributedToon", {"setFriendsList"}, OTP_DO_ID_FRIEND_MANAGER, queryAvatarResponse)
end
