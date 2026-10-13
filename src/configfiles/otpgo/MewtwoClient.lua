-- Message types:
CLIENT_LOGIN                                   = 1
CLIENT_LOGIN_RESP                              = 2
CLIENT_GET_AVATARS                             = 3
-- Sent by the server when it is dropping the connection deliberately.
CLIENT_GO_GET_LOST                             = 4
CLIENT_GET_AVATARS_RESP                        = 5
CLIENT_CREATE_AVATAR                           = 6
CLIENT_CREATE_AVATAR_RESP                      = 7
CLIENT_GET_FRIEND_LIST                         = 10
CLIENT_GET_FRIEND_LIST_RESP                    = 11
CLIENT_GET_AVATAR_DETAILS                      = 14
CLIENT_GET_AVATAR_DETAILS_RESP                 = 15
CLIENT_LOGIN_2                                 = 16
CLIENT_LOGIN_2_RESP                            = 17

CLIENT_OBJECT_UPDATE_FIELD                     = 24
CLIENT_OBJECT_UPDATE_FIELD_RESP                = 24
CLIENT_OBJECT_DISABLE                          = 25
CLIENT_OBJECT_DISABLE_RESP                     = 25
CLIENT_OBJECT_DISABLE_OWNER                    = 26
CLIENT_OBJECT_DISABLE_OWNER_RESP               = 26
CLIENT_OBJECT_DELETE                           = 27
CLIENT_OBJECT_DELETE_RESP                      = 27
CLIENT_SET_ZONE_CMU                            = 29
CLIENT_REMOVE_ZONE                             = 30
CLIENT_SET_AVATAR                              = 32
CLIENT_CREATE_OBJECT_REQUIRED                  = 34
CLIENT_CREATE_OBJECT_REQUIRED_RESP             = 34
CLIENT_CREATE_OBJECT_REQUIRED_OTHER            = 35
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_RESP       = 35
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_OWNER      = 36
CLIENT_CREATE_OBJECT_REQUIRED_OTHER_OWNER_RESP = 36

CLIENT_REQUEST_GENERATES                       = 36

CLIENT_DISCONNECT                              = 37

CLIENT_GET_STATE_RESP                          = 47
CLIENT_DONE_INTEREST_RESP                      = 48

CLIENT_DELETE_AVATAR                           = 49

CLIENT_DELETE_AVATAR_RESP                      = 5

CLIENT_HEARTBEAT                               = 52
CLIENT_FRIEND_ONLINE                           = 53
CLIENT_FRIEND_OFFLINE                          = 54
CLIENT_REMOVE_FRIEND                           = 56

CLIENT_CHANGE_PASSWORD                         = 65

CLIENT_SET_NAME_PATTERN                        = 67
CLIENT_SET_NAME_PATTERN_ANSWER                 = 68

CLIENT_SET_WISHNAME                            = 70
CLIENT_SET_WISHNAME_RESP                       = 71
CLIENT_SET_WISHNAME_CLEAR                      = 72
CLIENT_SET_SECURITY                            = 73

CLIENT_SET_DOID_RANGE                          = 74

CLIENT_GET_AVATARS_RESP2                       = 75
CLIENT_CREATE_AVATAR2                          = 76
CLIENT_SYSTEM_MESSAGE                          = 78
CLIENT_SET_AVTYPE                              = 80

CLIENT_GET_PET_DETAILS                         = 81
CLIENT_GET_PET_DETAILS_RESP                    = 82

CLIENT_ADD_INTEREST                            = 97
CLIENT_REMOVE_INTEREST                         = 99
CLIENT_OBJECT_LOCATION                         = 102

CLIENT_LOGIN_3                                 = 111
CLIENT_LOGIN_3_RESP                            = 110

CLIENT_GET_FRIEND_LIST_EXTENDED                = 115
CLIENT_GET_FRIEND_LIST_EXTENDED_RESP           = 116

CLIENT_SET_FIELD_SENDABLE                      = 120

CLIENT_SYSTEMMESSAGE_AKNOWLEDGE                = 123
CLIENT_CHANGE_GENERATE_ORDER                   = 124

-- new toontown specific login message, adds last logged in, and if child account has parent acount
CLIENT_LOGIN_TOONTOWN                          = 125
CLIENT_LOGIN_TOONTOWN_RESP                     = 126

CLIENT_DISCONNECT_GENERIC                = 1
CLIENT_DISCONNECT_RELOGIN                = 100
CLIENT_DISCONNECT_OVERSIZED_DATAGRAM     = 106
CLIENT_DISCONNECT_NO_HELLO               = 107
CLIENT_DISCONNECT_CHAT_AUTH_ERROR        = 120
CLIENT_DISCONNECT_ACCOUNT_ERROR          = 122
CLIENT_DISCONNECT_NO_HEARTBEAT           = 345
CLIENT_DISCONNECT_INVALID_MSGTYPE        = 108
CLIENT_DISCONNECT_TRUNCATED_DATAGRAM     = 109
CLIENT_DISCONNECT_ANONYMOUS_VIOLATION    = 113
CLIENT_DISCONNECT_FORBIDDEN_INTEREST     = 115
CLIENT_DISCONNECT_MISSING_OBJECT         = 117
CLIENT_DISCONNECT_FORBIDDEN_FIELD        = 118
CLIENT_DISCONNECT_FORBIDDEN_RELOCATE     = 119
CLIENT_DISCONNECT_BAD_VERSION            = 125
CLIENT_DISCONNECT_FIELD_CONSTRAINT       = 127
CLIENT_DISCONNECT_ADMIN_KICK             = 151
CLIENT_DISCONNECT_SESSION_OBJECT_DELETED = 153

DATABASE_OBJECT_TYPE_ACCOUNT = 1
DATABASE_OBJECT_TYPE_TOON    = 2
DATABASE_OBJECT_TYPE_ESTATE  = 3
DATABASE_OBJECT_TYPE_HOUSE   = 4
DATABASE_OBJECT_TYPE_PET     = 5

-- Internal message types
STATESERVER_OBJECT_UPDATE_FIELD = 2004
STATESERVER_OBJECT_DELETE_RAM = 2007

CLIENT_AGENT_EJECT = 3004

-- Friend related messages
TOONTOWNCLIENT_FRIEND_ONLINE  = 3501
TOONTOWNCLIENT_FRIEND_OFFLINE = 3502
TOONTOWNCLIENT_CHECK_ONLINE_FRIENDS = 3503
TOONTOWNCLIENT_MAKE_FRIEND = 3504
TOONTOWNCLIENT_REMOVE_FRIEND = 3505

CHANNEL_CLIENT_BROADCAST = 4014

CHANNEL_PUPPET_ACTION = 4004

ACCOUNT_AVATAR_USAGE = 3005
ACCOUNT_ACCOUNT_USAGE = 3006
ALLOW_COMMAND_USAGE = 3007

BROADCAST_MESSAGE_TO_ALL_AI = 4005

GET_SERVER_STATUS = 15000
GET_SERVER_STATUS_RESP = 15001

OTP_DO_ID_NAME_APPROVAL = 4715

NAME_APPROVAL_REQUEST_NAME = 14000

package.path = package.path .. ";../otp/?.lua"

local inspect = require('inspect')
local date = require('date')

-- From https://stackoverflow.com/a/22831842
function string.starts(String,Start)
    return string.sub(String,1,string.len(Start))==Start
end

-- From https://stackoverflow.com/a/2421746
function string.upperFirst(str)
    return (string.gsub(str, "^%l", string.upper))
end

function table.shallow_copy(t)
    local t2 = {}
    for k,v in pairs(t) do
      t2[k] = v
    end
    return t2
end

-- Return the first index with the given value (or nil if not found).
function table.index(array, value)
    for i, v in ipairs(array) do
        if v == value then
            return i
        end
    end
    return nil
end

-- https://gist.github.com/VADemon/afb10dbb0d10d99aeb21449752da6285
function regexEscape(str)
    return string.gsub(str, "[%(%)%.%%%+%-%*%?%[%^%$%]]", "%%%1")
end

string.replace = function (str, this, that)
    return string.gsub(str, regexEscape(this), string.gsub(that, "%%", "%%%%")) -- only % needs to be escaped for 'that'
end

-- Read vismap:
function readVismap()
    local json = require("json")
    local io = require("io")

    -- TODO: Custom path.
    f, err = io.open("vismap.json", "r")
    assert(not err, err)

    decoder = json.new_decoder(f)
    result, err = decoder:decode()
    f:close()
    assert(not err, err)
    return result
end

VISMAP = readVismap()
print("MewtwoClient: Vismap successfully loaded.")

function readAccountBridge()
    local json = require("json")
    local io = require("io")

    -- TODO: Custom path.
    f, err = io.open("databases/accounts.json", "r")
    if err then
        print("MewtwoClient: Returning empty table for account bridge")
        return {}
    end

    decoder = json.new_decoder(f)
    result, err = decoder:decode()
    f:close()
    assert(not err, err)
    print("MewtwoClient: Account bridge successfully loaded.")
    return result
end

ACCOUNT_BRIDGE = readAccountBridge()

function saveAccountBridge()
    local json = require("json")
    local io = require("io")

    -- TODO: Custom path.
    f, err = io.open("databases/accounts.json", "w")
    assert(not err, err)
    encoder = json.new_encoder(f)
    err = encoder:encode(ACCOUNT_BRIDGE)
    assert(not err, err)
end

WHITELIST = {}
function readWhitelist()
    local io = require("io")
    local f, err = io.open("../../chat/twhitelist.dat")
    assert(not err, err)
    for line in f:lines() do
        WHITELIST[line] = true
    end
end
readWhitelist()
print("MewtwoClient: Successfully loaded whitelist.")

NAME_PATTERNS = {}
function readNameMaster()
    local io = require("io")
    local f, err = io.open("../NameMasterEnglish.txt")
    assert(not err, err)
    for line in f:lines() do
        if string.starts(line, "#") then
            goto continue
        end
        local parsed = {}
        -- Match any character except "*"
        for w in string.gmatch(line, "([^*]+)") do
            table.insert(parsed, w)
        end
        if #parsed ~= 3 then
            print(string.format("readNameMaster: Invalid entry: %s", inspect(parsed)))
            goto continue
        end
        -- Need to keep the unique ID, since Disney sometimes removed names and thus indexing order isn't necessarily the same as the unique ID.
        NAME_PATTERNS[tostring(parsed[1])] = parsed[3]
        ::continue::
    end
    print("MewtwoClient: Successfully loaded NameMaster.txt.")
end
readNameMaster()

-- Converts a hexadecimal string to a string of bytes
-- From: https://smherwig.blogspot.com/2013/05/a-simple-binascii-module-in-ruby-and-lua.html
function unhexlify(s)
    if #s % 2 ~= 0 then
        error('unhexlify: hexstring must contain even number of digits')
    end
    local a = {}
    for i=1,#s,2 do
        local hs = string.sub(s, i, i+1)
        local code = tonumber(hs, 16)
        if not code then
            error(string.format("unhexlify: '%s' is not avalid hex number", hs))
        end
        table.insert(a, string.char(code))
    end
    return table.concat(a)
end

-- Load the configuration varables (see config.example.lua)
dofile("config.lua")

-- Load patches
-- dofile("PickleGlobals.lua")

NumToColor = {
    'White', 'Peach', 'Bright Red', 'Red', 'Maroon', 'Sienna', 'Brown', 'Tan',
    'Coral', 'Orange', 'Yellow', 'Cream', 'Citrine', 'Lime', 'Sea Green',
    'Green', 'Light Blue', 'Aqua', 'Blue', 'Periwinkle', 'Royal Blue',
    'Slate Blue', 'Purple', 'Lavender', 'Pink', 'Plum', 'Black'
}

AnimalToSpecies = {
    dog = 'Dog',
    cat = 'Cat',
    mouse = 'Mouse',
    horse = 'Horse',
    rabbit = 'Rabbit',
    duck = 'Duck',
    monkey = 'Monkey',
    bear = 'Bear',
    pig = 'Pig'
}

toonHeadTypes = {'dls',
 'dss',
 'dsl',
 'dll',
 'cls',
 'css',
 'csl',
 'cll',
 'hls',
 'hss',
 'hsl',
 'hll',
 'mls',
 'mss',
 'rls',
 'rss',
 'rsl',
 'rll',
 'fls',
 'fss',
 'fsl',
 'fll',
 'pls',
 'pss',
 'psl',
 'pll',
 'bls',
 'bss',
 'bsl',
 'bll',
 'sls',
 'sss',
 'ssl',
 'sll'}

toonHeadTypeToAnimalName = {
    d = 'dog',
    c = 'cat',
    m = 'mouse',
    h = 'horse',
    r = 'rabbit',
    f = 'duck',
    p = 'monkey',
    b = 'bear',
    s = 'pig'
}

avatarSpeedChatPlusStates = {}

function isValidNetString(dnaString)
    local validDna = true

    local dg = datagram:new()
    dg:addString(dnaString)

    local _dgi = datagramiterator.new(dg)
    _dgi:readUint16() -- length, unused

    if _dgi:getRemainingSize() ~= DNA_LENGTH then
        validDna = false
    end

    if _dgi:readFixedString(1) ~= DNA_FIRST_CHAR then
        validDna = false
    end

    -- headIndex
    local headIndex = _dgi:readUint8()
    if headIndex >= DNA_MAX_HEAD_INDEX then
        validDna = false
    end

    -- torsoIndex
    if _dgi:readUint8() >= DNA_MAX_TORSO_INDEX then
        validDna = false
    end

    -- legsIndex
    if _dgi:readUint8() >= DNA_MAX_LEG_INDEX then
        validDna = false
    end

    -- gender
    local validForGender

    if  _dgi:readUint8() == 1 then
        validForGender = DNA_MAX_MALE_BOTTOMS
    else
        validForGender = DNA_MAX_FEMALE_BOTTOMS
    end

    local topTex = _dgi:readUint8()
    local topTexColor = _dgi:readUint8()
    local sleeveTex = _dgi:readUint8()
    local sleeveTexColor = _dgi:readUint8()
    local botTex = _dgi:readUint8()
    local botTexColor = _dgi:readUint8()
    local armColor = _dgi:readUint8()
    local gloveColor = _dgi:readUint8()
    local legColor = _dgi:readUint8()
    local headColor = _dgi:readUint8()

    -- Shirts
    if topTex >= DNA_MAX_SHIRTS then
        validDna = false
    end

    -- ClothesColors
    if topTexColor >= DNA_MAX_CLOTHING_COLORS then
        validDna = false
    end

    -- Sleeves
    if sleeveTex >= DNA_MAX_SLEEVES then
        validDna = false
    end

    -- ClothesColors
    if sleeveTexColor >= DNA_MAX_CLOTHING_COLORS then
        validDna = false
    end

    if botTex >= validForGender then
        validDna = false
    end

    -- ClothesColors
    if botTexColor >= DNA_MAX_CLOTHING_COLORS then
        validDna = false
    end

    -- allColorsList
    if armColor >= DNA_MAX_COLOR then
        validDna = false
    end

    if gloveColor ~= 0 then
        validDna = false
    end

    if legColor >= DNA_MAX_COLOR then
        validDna = false
    end

    if headColor >= DNA_MAX_COLOR then
        validDna = false
    end

    local head = toonHeadTypes[headIndex + 1]
    return validDna, {headColor + 1, toonHeadTypeToAnimalName[head:sub(1, 1)]}
end

function handleDatagram(client, msgType, dgi)
    -- Internal datagrams
    if msgType == TOONTOWNCLIENT_CHECK_ONLINE_FRIENDS then
        handleCheckFriendOnline(client, dgi)
    elseif msgType == TOONTOWNCLIENT_FRIEND_ONLINE then
        handleFriendOnline(client, dgi)
    elseif msgType == TOONTOWNCLIENT_FRIEND_OFFLINE then
        handleFriendOffline(client, dgi)
    elseif msgType == TOONTOWNCLIENT_MAKE_FRIEND then
        handleMakeFriend(client, dgi)
    elseif msgType == TOONTOWNCLIENT_REMOVE_FRIEND then
        handleClientRemoveFriend(client, dgi:readUint32())
    elseif msgType == GET_SERVER_STATUS_RESP then
        handleServerStatusResp(client, dgi:readUint8(), dgi:readString())
    else
        client:warn(string.format("Received unknown server msgtype %d", msgType))
    end
end

function handleServerStatusResp(client, serverStatus, accountType)
    if serverStatus == 1 and accountType == "Player" then
        client:sendDisconnect(CLIENT_DISCONNECT_ADMIN_KICK, "You have been logged out by an administrator working on the servers.", false)
    end
end

-- function sendPatch(client, payload)
--     local patchMsg = datagram:new()
--     patchMsg:addUint16(CLIENT_OBJECT_UPDATE_FIELD)
--     patchMsg:addUint32(1337) -- doId
--     patchMsg:addUint16(139) -- fieldId (avatarListResponse)
--     patchMsg:addString(payload)
--     client:sendDatagram(patchMsg)
-- end

function receiveDatagram(client, dgi)
    -- Client received datagrams
    msgType = dgi:readUint16()

    if msgType == CLIENT_HEARTBEAT then
        client:handleHeartbeat()
    elseif msgType == CLIENT_DISCONNECT then
        client:handleDisconnect()
    elseif msgType == CLIENT_LOGIN_TOONTOWN then
        handleLogin(client, dgi)
    -- We have reached the only message types unauthenticated clients can use.
    elseif not client:authenticated() then
        client:sendDisconnect(CLIENT_DISCONNECT_GENERIC, "First datagram is not CLIENT_LOGIN_TOONTOWN", true)
    elseif msgType == CLIENT_ADD_INTEREST then
        handleAddInterest(client, dgi)
    elseif msgType == CLIENT_REMOVE_INTEREST then
        client:handleRemoveInterest(dgi)
    elseif msgType == CLIENT_GET_AVATARS then
        handleGetAvatars(client, false)
    elseif msgType == CLIENT_OBJECT_UPDATE_FIELD then
        client:handleUpdateField(dgi)
    elseif msgType == CLIENT_CREATE_AVATAR then
        handleCreateAvatar(client, dgi)
    elseif msgType == CLIENT_SET_NAME_PATTERN then
        handleSetNamePattern(client, dgi)
    elseif msgType == CLIENT_SET_WISHNAME then
        handleSetWishname(client, dgi)
    elseif msgType == CLIENT_SET_WISHNAME_CLEAR then
        handleSetWishnameClear(client, dgi)
    elseif msgType == CLIENT_SET_AVATAR then
        handleSetAvatar(client, dgi)
    elseif msgType == CLIENT_GET_FRIEND_LIST then
        handleGetFriendList(client)
    elseif msgType == CLIENT_REMOVE_FRIEND then
        handleClientRemoveFriend(client, dgi:readUint32())
    elseif msgType == CLIENT_OBJECT_LOCATION then
        client:setLocation(dgi)
    elseif msgType == CLIENT_GET_AVATAR_DETAILS then
        handleGetAvatarDetails(client, dgi, "DistributedToon", CLIENT_GET_AVATAR_DETAILS_RESP)
    elseif msgType == CLIENT_GET_PET_DETAILS then
        handleGetAvatarDetails(client, dgi, "DistributedPet", CLIENT_GET_PET_DETAILS_RESP)
    elseif msgType == CLIENT_DELETE_AVATAR then
        handleClientDeleteAvatar(client, dgi)
    else
        client:sendDisconnect(CLIENT_DISCONNECT_GENERIC, string.format("Unknown message type: %d", msgType), true)
    end

    if dgi:getRemainingSize() ~= 0 then
        client:sendDisconnect(CLIENT_DISCONNECT_OVERSIZED_DATAGRAM, string.format("Datagram contains excess data.\n%s", tostring(dgi)), true)
    end
end

function handleLogin(client, dgi)
    local playToken = dgi:readString()
    local version = dgi:readString()
    local hash = dgi:readUint32()
    local tokenType = dgi:readInt32()
    local wantMagicWords = dgi:readString()

    if client:authenticated() then
        client:sendDisconnect(CLIENT_DISCONNECT_RELOGIN, "Authenticated client tried to login twice!", true)
        return
    end

    -- Check if version and hash matches
    if version ~= SERVER_VERSION then
        client:sendDisconnect(CLIENT_DISCONNECT_BAD_VERSION, string.format("Client version mismatch: client=%s, server=%s", version, SERVER_VERSION), true)
        return
    end
    if hash ~= DC_HASH then
        client:sendDisconnect(CLIENT_DISCONNECT_BAD_VERSION, string.format("Client DC hash mismatch: client=%d, server=%d", hash, DC_HASH), true)
        return
    end

    local speedChatPlus
    local openChat
    local isPaid
    local dislId
    local linkedToParent
    if PRODUCTION_ENABLED then
        local json = require("json")
        local crypto = require("crypto")
        local ok, err = pcall(function()
            local decodedToken, err = crypto.base64_decode(playToken)
            if err then
                error(err)
                return
            end
            local encrypted, err = json.decode(decodedToken)
            if err then
                error(err)
                return
            end
            local encryptedData, err = crypto.base64_decode(encrypted.data)
            if err then
                error(err)
                return
            end
            local iv, err = crypto.base64_decode(encrypted.iv)
            if err then
                error(err)
                return
            end

            local data, err = crypto.decrypt(encryptedData, 'aes-cbc', unhexlify(PLAY_TOKEN_KEY), crypto.RAW_DATA, iv)
            if err then
                error(err)
                return
            end
            local jsonData, err = json.decode(data)
            if err then
                error(err)
                return
            end

            -- Retrieve data from the API response.
            playToken = jsonData.playToken
            if tonumber(jsonData.OpenChat) == 1 then
                openChat = true
            else
                openChat = false
            end

            if tonumber(jsonData.Member) == 1 then
                isPaid = true
            else
                isPaid = false
            end

            local timestamp = jsonData.Timestamp
            dislId = tonumber(jsonData.dislId)
            accountType = jsonData.accountType
            linkedToParent = jsonData.LinkedToParent

            if tonumber(jsonData.SpeedChatPlus) == 1 then
                speedChatPlus = true
            else
                speedChatPlus = false
            end

            if WANT_TOKEN_EXPIRATIONS and timestamp < os.time() then
                client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "Token has expired.", true)
                return
            end
        end)

        if not ok then
            -- Bad play token
            client:warn(string.format("MewtwoClient: Error when decrypting play token: %s", err))
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "Invalid play token", true)
            return
        end
        -- TODO: Send discord webhook.
    else
        -- Production is not enabled
        -- We need these dummy values
        openChat = false
        if WANT_OPEN_CHAT then
            openChat = true
        end
        isPaid = false
        if WANT_MEMBERSHIP then
            isPaid = true
        end
        dislId = 1
        linkedToParent = false
        accountType = "Administrator"
        speedChatPlus = false
        if WANT_SPEEDCHAT_PLUS then
            speedChatPlus = true
        end
    end

    local accountId = ACCOUNT_BRIDGE[playToken]
    if accountId ~= nil then
        -- Query the account object
        client:getDatabaseValues(accountId, "Account", {"ACCOUNT_AV_SET", "CREATED", "LAST_LOGIN"}, function (doId, success, fields)
            if not success then
                client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "The Account object was unable to be queried.", true)
                return
            end

            -- Update LAST_LOGIN
            fields.LAST_LOGIN = os.date("%a %b %d %H:%M:%S %Y")
            client:setDatabaseValues(accountId, "Account", {
                LAST_LOGIN = fields.LAST_LOGIN,
            })

            loginAccount(client, fields, accountId, playToken, openChat, isPaid, dislId, linkedToParent, accountType, speedChatPlus)
        end)
    else
        -- Create a new account object
        local account = {
            -- The rest of the values are defined in the dc file.
            CREATED = os.date("%a %b %d %H:%M:%S %Y"),
            LAST_LOGIN = os.date("%a %b %d %H:%M:%S %Y"),
        }

        client:createDatabaseObject("Account", account, DATABASE_OBJECT_TYPE_ACCOUNT, function (accountId)
            if accountId == 0 then
                client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "The Account object was unable to be created.", false)
                return
            end

            -- Store the account into the bridge
            ACCOUNT_BRIDGE[playToken] = accountId
            saveAccountBridge()

            account.ACCOUNT_AV_SET = {0, 0, 0, 0, 0, 0}

            client:writeServerEvent("account-created", "MewtwoClient", string.format("%d", accountId))

            loginAccount(client, account, accountId, playToken, openChat, isPaid, dislId, linkedToParent, accountType, speedChatPlus)
        end)
    end
end

function loginAccount(client, account, accountId, playToken, openChat, isPaid, dislId, linkedToParent, accountType, speedChatPlus)
    if PRODUCTION_ENABLED then
        -- Check if we are in maintenance mode
        dg = datagram:new()
        client:addServerHeader(dg, GET_SERVER_STATUS, GET_SERVER_STATUS)
        dg:addString(accountType)
        client:routeDatagram(dg)
    end

    -- Eject other client if already logged in.
    local ejectDg = datagram:new()
    client:addServerHeaderWithAccountId(ejectDg, accountId, CLIENT_AGENT_EJECT)
    ejectDg:addUint16(100)
    ejectDg:addString("You have been disconnected because someone else just logged in using your account on another computer.")
    client:routeDatagram(ejectDg)

    -- Subscribe to our puppet channel.
    client:subscribePuppetChannel(accountId, 3)

    -- Set our channel containing our account id
    client:setChannel(accountId, 0)

    client:authenticated(true)

    -- Store the account id and avatar list into our client's user table:
    local userTable = client:userTable()
    userTable.accountId = accountId
    userTable.avatars = account.ACCOUNT_AV_SET
    userTable.playToken = playToken
    userTable.isPaid = isPaid
    userTable.speedChatPlus = speedChatPlus
    userTable.openChat = openChat
    userTable.accountType = accountType
    client:userTable(userTable)

    -- Log the event
    client:writeServerEvent("account-login", "MewtwoClient", string.format("%d", accountId))

    -- HACK: Add a fake OtpAvatarManager generate, so we can send client-related patches.
    local genMsg = datagram:new()
    genMsg:addUint16(CLIENT_CREATE_OBJECT_REQUIRED)
    genMsg:addUint32(0) -- parentId
    genMsg:addUint32(0) -- zoneId
    genMsg:addUint16(25) -- classId (OtpAvatarManager)
    genMsg:addUint32(1337) -- doId
    client:sendDatagram(genMsg)

    -- Magic Words handler
    if accountType ~= "Player" then
        -- This account is allowed to use Magic Words.
        local dg = datagram:new()
        dg:addServerHeader(BROADCAST_MESSAGE_TO_ALL_AI, accountId, ALLOW_COMMAND_USAGE)
        dg:addUint32(accountId)
        dg:addString(accountType)
        client:routeDatagram(dg)
    end

    -- Prepare the login response.
    local resp = datagram:new()
    resp:addUint16(CLIENT_LOGIN_TOONTOWN_RESP)
    resp:addUint8(0) -- Return code
    resp:addString("All Ok")
    resp:addUint32(dislId) -- accountNumber
    resp:addString(playToken) -- accountName
    resp:addUint8(1) -- accountNameApproved

    if openChat then
        resp:addString('YES') -- openChatEnabled, does not seem to be used
        resp:addString('CODE') -- createFriendsWithChat
        resp:addString('YES') -- chatCodeCreationRule
    else
        resp:addString('NO') -- openChatEnabled, does not seem to be used
        resp:addString('NO') -- createFriendsWithChat
        resp:addString('NO') -- chatCodeCreationRule
    end

    resp:addUint32(os.time()) -- sec
    resp:addUint32(os.clock()) -- usec

    if isPaid then
        resp:addString("FULL") -- access
    else
        resp:addString("VELVET") -- access
    end

    if speedChatPlus then
        resp:addString("YES") -- WhiteListResponse
    else
        resp:addString("NO") -- WhiteListResponse
    end

    resp:addString(os.date("%Y-%m-%d %H:%M:%S")) -- lastLoggedInStr
    resp:addInt32(math.floor(date.diff(account.LAST_LOGIN, account.CREATED):spandays())) -- accountDays
    if linkedToParent then
        resp:addString("WITH_PARENT_ACCOUNT") -- toonAccountType
    else
        resp:addString("NO_PARENT_ACCOUNT") -- toonAccountType
    end
    resp:addString(playToken) -- userName

    -- Dispatch the response to the client.
    client:sendDatagram(resp)
end

function handleAddInterest(client, dgi)
    local handle = dgi:readUint16()
    local context = dgi:readUint32()
    local parent = dgi:readUint32()
    local zones = {}
    while dgi:getRemainingSize() > 0 do
        local zone = dgi:readUint32()
        if zone == 1 then
            -- We don't want quiet zone.
            goto continue
        end
        table.insert(zones, zone)
        ::continue::
    end


    -- Replace street zone with vismap if exists
    if #zones == 1 then
        if VISMAP[tostring(zones[1])] ~= nil then
            zones = VISMAP[tostring(zones[1])]
        elseif zones[1] >= 22000 and zones[1] < 61000 then
            -- Handle Welcome Valley zones
            local welcomeValleyZone = zones[1]
            local hoodId = zones[1] - math.fmod(zones[1], 1000)
            local offset = math.fmod(welcomeValleyZone, 2000)
            -- Get original vismap
            if VISMAP[tostring(offset + 2000)] ~= nil then
                zones = table.shallow_copy(VISMAP[tostring(offset + 2000)])
                for i, v in ipairs(zones) do
                    local offset = math.fmod(zones[i], 2000)
                    zones[i] = offset + hoodId
                end
            end
        end
    end
    client:handleAddInterest(handle, context, parent, zones)
end

function handleGetAvatars(client, deletion)
    local userTable = client:userTable()
    local avatarList = userTable.avatars

    local retreivedFields = {}
    local expectingAvatars = {}
    local gotAvatars = {}

    -- sendPatch(client, DISABLE_LOADING_BLOCKER)

    local function gotAllAvatars()
        dg = datagram:new()
        local msgType = CLIENT_GET_AVATARS_RESP
        if delete then
            msgType = CLIENT_DELETE_AVATAR_RESP
        end
        dg:addUint16(msgType)
        dg:addUint8(0) -- returnCode
        dg:addUint16(#gotAvatars) -- avatarTotal
        for index, fields in pairs(retreivedFields) do
            local wishNameState = fields.WishNameState[1]
            local wishName = fields.WishName[1]

            local aName = 0

            local wantName = ""
            local approvedName = ""
            local rejectedName = ""

            if wishNameState == "OPEN" then
                aName = 1
            end

            if wishNameState == "PENDING" then
                wantName = wishName
            end

            if wishNameState == "APPROVED" then
                approvedName = wishName
            end

            if wishNameState == "REJECTED" then
                rejectedName = wishName
            end

            dg:addUint32(fields.avatarId)
            dg:addString(fields.setName[1]) -- name
            dg:addString(wantName) -- wantName
            dg:addString(approvedName) -- approvedName
            dg:addString(rejectedName) -- rejectedName

            dg:addString(fields.setDNAString[1]) -- avDNA
            dg:addUint8(index - 1) -- avPosition
            dg:addUint8(aName) -- aName
        end
        client:sendDatagram(dg)
    end

    for index, avatarId in ipairs(avatarList) do
        if avatarId ~= 0 then
            -- Query the avatar object
            client:getDatabaseValues(avatarId, "DistributedToon", {"setName", "setDNAString", "WishNameState", "WishName"}, function (doId, success, fields)
                if not success then
                    client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d was unable to be queried.", avatarId), false)
                    return
                end

                fields.avatarId = avatarId
                retreivedFields[index] = fields
                table.insert(gotAvatars, {})
                if #gotAvatars == #expectingAvatars then
                    gotAllAvatars()
                end
            end)
            table.insert(expectingAvatars, avatarId)
        end
        if index == 6 and #expectingAvatars == 0 then
            -- We got nothing to do.
            gotAllAvatars()
        end
    end
end

function handleCreateAvatar(client, reader)
    local userTable = client:userTable()
    local accountId = userTable.accountId

    local contextId = reader:readUint16()
    local dnaString = reader:readString()
    local avPosition = reader:readUint8()

    if avPosition > 6 then
        -- Client sent an invalid av position
        client:sendDisconnect(CLIENT_DISCONNECT_GENERIC, "Invalid Avatar index chosen.", true)
        return
    end

    if userTable.avatars[avPosition + 1] ~= 0 then
        -- This index isn't available.
        client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "The Avatar index chosen is not available.", true)
        return
    end

    local result, dna = isValidNetString(dnaString)

    if not result then
        client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "Invalid Avatar DNA sent.", true)
        return
    end

    -- Create a new DistributedToon object
    local avatar = {
        -- The rest of the values are defined in the dc file.
        setName = {NumToColor[dna[1]] .. " " .. AnimalToSpecies[dna[2]]},
        setDISLid = {accountId},
        setDNAString = {dnaString},
        setPosIndex = {avPosition},
        setAccountName = {userTable.playToken},
    }

    client:createDatabaseObject("DistributedToon", avatar, DATABASE_OBJECT_TYPE_TOON, function (avatarId)
        if avatarId == 0 then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "The DistributedToon object was unable to be created.", false)
            return
        end

        userTable.avatars[avPosition + 1] = avatarId

        client:setDatabaseValues(accountId, "Account", {
            ACCOUNT_AV_SET = userTable.avatars,
        })

        client:writeServerEvent("avatar-created", "MewtwoClient", string.format("%d|%d", accountId, avatarId))

        -- Prepare the create avatar response.
        local resp = datagram:new()
        resp:addUint16(CLIENT_CREATE_AVATAR_RESP)
        resp:addUint16(contextId)
        resp:addUint8(0) -- returnCode
        resp:addUint32(avatarId)

        -- Dispatch the response to the client.
        client:sendDatagram(resp)
    end)
end

function handleSetNamePattern(client, dgi)
    local avId = dgi:readUint32()

    client:getDatabaseValues(avId, "DistributedToon", {"WishNameState"}, function (doId, success, fields)
        if not success then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d was unable to be queried.", avId), false)
            return
        end

        if fields.WishNameState[1] ~= "OPEN" then
            -- Only one name allowed!
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d is unable to be named.", avId), true)
            return
        end
    end)

    local p1 = dgi:readInt16()
    local f1 = dgi:readInt16()
    local p2 = dgi:readInt16()
    local f2 = dgi:readInt16()
    local p3 = dgi:readInt16()
    local f3 = dgi:readInt16()
    local p4 = dgi:readInt16()
    local f4 = dgi:readInt16()

    -- Construct a pattern.
    local pattern = {{p1, f1}, {p2, f2},
                     {p3, f3}, {p4, f4}}

    local parts = {}
    for _, pair in ipairs(pattern) do
        local p, f = pair[1], pair[2]
        local part = NAME_PATTERNS[tostring(p)]
        if part == nil then
            part = ""
        end

        if f then
            string.upperFirst(part)
        else
            string.lower(part)
        end

        table.insert(parts, part)
    end

    -- # Merge 3&4 (the last name) as there should be no space.
    parts[3] = parts[3] .. table.remove(parts, 4)

    for i = #parts, 1, -1 do
        if parts[i] == "" then
            table.remove(parts, i)
        end
    end

    local name = table.concat(parts, " ")

    client:setDatabaseValues(avId, "DistributedToon", {
        WishNameState = {"LOCKED"},
        WishName = {""},
        setName = {name}
    })

    resp = datagram:new()
    resp:addUint16(CLIENT_SET_NAME_PATTERN_ANSWER)
    resp:addUint32(avId)
    resp:addUint8(0)

    client:sendDatagram(resp)
end

function handleSetWishname(client, dgi)
    local avId = dgi:readUint32()
    local pendingName = dgi:readString()

    local approvedName = ""

    if not PRODUCTION_ENABLED then
        approvedName = pendingName
        pendingName = ""
    end

    if avId == 0 then
        -- Client just wants to check the name
        local resp = datagram:new()
        resp:addUint16(CLIENT_SET_WISHNAME_RESP)
        resp:addUint32(avId)
        resp:addUint16(0) -- returnCode
        resp:addString(pendingName) -- pendingName
        resp:addString(approvedName) -- approvedName
        resp:addString("") -- rejectedName

        -- Dispatch the response to the client.
        client:sendDatagram(resp)
        return
    end

    -- Query to see if this is a valid request
    -- This prevents bogus name approvals being sent to our Discord
    client:getDatabaseValues(avId, "DistributedToon", {"WishNameState"}, function (doId, success, fields)
        if not success then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d was unable to be queried.", avId), false)
            return
        end

        if fields.WishNameState[1] ~= "OPEN" then
            -- Only one name allowed!
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d is unable to be named.", avId), true)
            return
        end

        if PRODUCTION_ENABLED then
            client:setDatabaseValues(avId, "DistributedToon", {
                WishNameState = {"PENDING"},
                WishName = {pendingName},
            })

            -- Send name to our approval service
            local dg = datagram:new()
            dg:addServerHeader(OTP_DO_ID_NAME_APPROVAL, 0, NAME_APPROVAL_REQUEST_NAME)
            dg:addUint32(avId)
            dg:addString(pendingName)
            dg:addString(NAME_APPROVAL_WEBHOOK_URL)
            client:routeDatagram(dg)
        end
    end)

    if not PRODUCTION_ENABLED then
        -- Approve name instantly as we are not on production
        client:setDatabaseValues(avId, "DistributedToon", {
            WishNameState = {"LOCKED"},
            setName = {approvedName},
        })
    end

    -- Prepare the wish name response.
    local resp = datagram:new()
    resp:addUint16(CLIENT_SET_WISHNAME_RESP)
    resp:addUint32(avId)
    resp:addUint16(0) -- returnCode
    resp:addString(pendingName) -- pendingName
    resp:addString(approvedName) -- approvedName
    resp:addString("") -- rejectedName

     -- Dispatch the response to the client.
    client:sendDatagram(resp)
end

function handleSetWishnameClear(client, dgi)
    local avatarId = dgi:readUint32()
    local actionFlag = dgi:readUint8()

    client:getDatabaseValues(avatarId, "DistributedToon", {"WishName", "WishNameState"}, function (doId, success, fields)
        if not success then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("The DistributedToon object %d was unable to be queried.", avatarId), false)
            return
        end

        if fields.WishNameState[1] == "APPROVED" and actionFlag == 1 then
            -- This name was approved.
            -- Set their name.
            client:setDatabaseValues(avatarId, "DistributedToon", {
                WishNameState = {""},
                WishName = {""},
                setName = {fields.WishName[1]},
            })
        else
            -- This name was rejected.
            -- Set them to the OPEN state so they can try again.
            client:setDatabaseValues(avatarId, "DistributedToon", {
                WishNameState = {"OPEN"},
                WishName = {""}
            })
        end
    end)
end

function checkIsAvInList(avatarId, avatarList)
    local isAvInList = false
    for _, avId in ipairs(avatarList) do
        if avatarId == avId then
            isAvInList = true
            break
        end
    end
    return isAvInList
end

function handleSetAvatar(client, dgi)
    local userTable = client:userTable()
    local accountId = userTable.accountId

    local avatarId = dgi:readUint32()

    if avatarId == 0 then
        clearAvatar(client)
        return
    end

    local isAvInList = checkIsAvInList(avatarId, userTable.avatars)
    if not isAvInList then
        client:sendDisconnect(CLIENT_DISCONNECT_GENERIC, string.format("Avatar %d not in list.", avatarId), true)
        return
    end

    userTable.avatarId = avatarId
    userTable.friendQueue = {}
    client:userTable(userTable)

    client:setChannel(accountId, avatarId)

    local setAccess = 1
    if userTable.isPaid then
        setAccess = 2
    end

    -- Send street sign patch
    -- sendPatch(client, FIX_STREET_SIGN_URL)

    -- Magic Words handler
    -- if userTable.accountType ~= "Player" then
    --     sendPatch(client, ENABLE_MAGIC_WORDS)
    -- end

    client:sendActivateObject(avatarId, "DistributedToon", {
        setAccess = {setAccess},
        setDISLid = {accountId}
    })

    client:objectSetOwner(avatarId, true)

    -- Let the UberDog know about our avatar usage.
    sendUsage(client, userTable.playToken, userTable.openChat, 0, avatarId, accountId, userTable.isPaid, false)

    -- Broadcast to our friends that we are coming online
    dg = datagram:new()
    client:addServerHeader(dg, CHANNEL_CLIENT_BROADCAST, TOONTOWNCLIENT_FRIEND_ONLINE)
    dg:addUint32(avatarId)
    dg:addBool(userTable.speedChatPlus)
    client:routeDatagram(dg)

    -- Set post removes in case we go offline.
    dg = datagram:new()
    client:addServerHeader(dg, CHANNEL_CLIENT_BROADCAST, TOONTOWNCLIENT_FRIEND_OFFLINE)
    dg:addUint32(avatarId)
    client:addPostRemove(dg)

    -- Let the UberDog know about our avatar usage (going offline).
    sendUsage(client, userTable.playToken, userTable.openChat, avatarId, 0, accountId, userTable.isPaid, true)

    avatarSpeedChatPlusStates[avatarId] = userTable.speedChatPlus
end

function sendUsage(client, playToken, openChat, priorAvatar, newAvatar, accountId, isPaid, postRemove)
    -- Log avatar usage
    local playerName = playToken
    local playerNameApproved = 1
    local openChatEnabled = "NO"
    local createFriendsWithChat = "NO"
    local chatCodeCreation = "NO"

    if openChat then
        openChatEnabled = "YES"
        createFriendsWithChat = "CODE"
        chatCodeCreation = "YES"
    end

    local avatarId

    if priorAvatar ~= 0 then
        avatarId = priorAvatar
    else
        avatarId = newAvatar
    end

    local dg = datagram:new()
    dg:addServerHeader(CHANNEL_PUPPET_ACTION, avatarId, ACCOUNT_AVATAR_USAGE)

    dg:addUint32(priorAvatar) -- priorAvatar
    dg:addUint32(newAvatar) -- newAvatar
    dg:addUint16(0) -- newAvatarType
    dg:addUint32(accountId) -- accountId
    dg:addString(openChatEnabled) -- openChatEnabled
    dg:addString(createFriendsWithChat) -- createFriendsWithChat
    dg:addString(chatCodeCreation) -- chatCodeCreation

    if isPaid then
        dg:addString("FULL") -- piratesAccess
    else
        dg:addString("VELVET") -- piratesAccess
    end

    dg:addInt32(0) -- familyAccountId
    dg:addInt32(accountId) -- playerAccountId

    dg:addString(playerName) -- playerName
    dg:addInt8(playerNameApproved) -- playerNameApproved

    -- maxAvatars
    local maxAvatars

    if isPaid then
        maxAvatars = 6
    else
        maxAvatars = 1
    end

    dg:addInt32(maxAvatars) -- maxAvatars

    dg:addInt16(0) -- numFamilyMembers

    if postRemove then
        client:addPostRemove(dg)
    else
        client:routeDatagram(dg)
    end
end

function clearAvatar(client)
    local userTable = client:userTable()

    if userTable.avatarId == nil then
        return
    end

    client:removeSessionObject(userTable.avatarId)
    client:unsubscribePuppetChannel(userTable.avatarId, 1)

    dg = datagram:new()
    client:addServerHeader(dg, userTable.avatarId, STATESERVER_OBJECT_DELETE_RAM)
    dg:addUint32(userTable.avatarId)
    client:routeDatagram(dg)

    -- Tell our friends that we are going offline
    -- and clear the post remove set for it.
    dg = datagram:new()
    client:addServerHeader(dg, CHANNEL_CLIENT_BROADCAST, TOONTOWNCLIENT_FRIEND_OFFLINE)
    dg:addUint32(userTable.avatarId)
    client:routeDatagram(dg)

    client:clearPostRemoves()

    -- Undeclare all friends.
    client:undeclareAllObjects()

    avatarSpeedChatPlusStates[userTable.avatarId] = nil

    userTable.avatarId = nil
    userTable.friendsList = nil
    client:userTable(userTable)

    client:setChannel(userTable.accountId, 0)
end

function handleAddOwnership(client, doId, parent, zone, dc, dgi)
    local userTable = client:userTable()
    local accountId = userTable.accountId
    local avatarId = userTable.avatarId
    if doId ~= avatarId then
        client:warn(string.format("Got AddOwnership for object %d, our avatarId is %d", doId, avatarId))
        return
    end

    client:addSessionObject(doId)
    client:subscribePuppetChannel(avatarId, 1)

    -- Store name for SpeedChat+
    local name = dgi:readString()
    userTable.avatarName = name
    client:userTable(userTable)

    local remainder = dgi:readRemainder()

    client:writeServerEvent("selected-avatar", "MewtwoClient", string.format("%d|%d", accountId, avatarId))

    local resp = datagram:new()
    resp:addUint16(CLIENT_GET_AVATAR_DETAILS_RESP)
    resp:addUint32(doId) -- avatarId
    resp:addUint8(0) -- returnCode
    resp:addString(name) -- setName
    resp:addData(remainder)
    client:sendDatagram(resp)

    -- Update common chat flags:
    local dg = datagram:new()
    dg:addServerHeader(avatarId, avatarId, STATESERVER_OBJECT_UPDATE_FIELD)
    dg:addUint32(avatarId)
    client:packFieldToDatagram(dg, "DistributedToon", "setCommonChatFlags", {0}, true)
    client:routeDatagram(dg)

    -- update whitelist chat flags:
    local dg = datagram:new()
    dg:addServerHeader(avatarId, avatarId, STATESERVER_OBJECT_UPDATE_FIELD)
    dg:addUint32(avatarId)
    if userTable.speedChatPlus then
        client:packFieldToDatagram(dg, "DistributedToon", "setWhitelistChatFlags", {1}, true)
    else
        client:packFieldToDatagram(dg, "DistributedToon", "setWhitelistChatFlags", {0}, true)
    end
    client:routeDatagram(dg)
end

function handleGetFriendList(client)
    local userTable = client:userTable()

    client:queryObjectFields(userTable.avatarId, "DistributedToon", {"setFriendsList"}, function (doId, success, fields)
        if not success then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("An error has occurred when attempting to fetch your friends list. (doId: %d)", avatarId), false)
            return
        end

        cleanupFriendsList(client, fields.setFriendsList[1])
        userTable.friendsList = fields.setFriendsList[1]
        client:userTable(userTable)

        if #userTable.friendsList == 0 then
            -- Nothing to do.
            finishGetFriendsList(client, {})
            return
        end

        local avatarFields = {}
        local gotNumAvatars = 0
        local function queryAvatarResponse(doId, success, fields)
            if not success then
                client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, string.format("An error has occurred when attempting to fetch your friends list. (doId: %d)", doId), false)
                return
            end
            avatarFields[doId] = fields
            gotNumAvatars = gotNumAvatars + 1
            if gotNumAvatars == #userTable.friendsList then
                finishGetFriendsList(client, avatarFields)
                avatarFields = nil
            end

            if (userTable.friendQueue ~= nil) and (#userTable.friendQueue > 0) then
                for i, pair in ipairs(userTable.friendQueue) do
                    checkFriendOnline(client, pair)
                end
            end
            userTable.friendQueue = nil
            client:userTable(userTable)
        end

        for _, v in ipairs(userTable.friendsList) do
            client:getDatabaseValues(v[1], "DistributedToon", {"setName", "setDNAString", "setPetId"}, queryAvatarResponse)
        end
    end)
end

function cleanupFriendsList(client, friendsList)
    local userTable = client:userTable()

    -- This cleans up the friends list by removing any
    -- non-db ids (this is caused by logging off/crashing while in the
    -- middle of using a teleport bot).
    local modifiedFriendsList = false
    for i = #friendsList, 1, -1 do
        if friendsList[i][1] > 199999999 then
            table.remove(friendsList, i)
            modifiedFriendsList = true
        end
    end

    if modifiedFriendsList then
        -- Update the object itself
        local dg = datagram:new()
        dg:addServerHeader(userTable.avatarId, 0, STATESERVER_OBJECT_UPDATE_FIELD)
        dg:addUint32(userTable.avatarId)
        client:packFieldToDatagram(dg, "DistributedToon", "setFriendsList", {friendsList}, true)
        client:routeDatagram(dg)
    end
end

function finishGetFriendsList(client, avatarFields)
    local userTable = client:userTable()

    local resp = datagram:new()
    resp:addUint16(CLIENT_GET_FRIEND_LIST_RESP)
    resp:addUint8(0) -- errorCode
    resp:addUint16(#userTable.friendsList) -- count
    for _, v in ipairs(userTable.friendsList) do

        -- Declare the object's existance so they can teleport.
        client:declareObject(v[1], "DistributedToon")

        -- Check if this avatar is online
        local dg = datagram:new()
        client:addServerHeaderWithAvatarId(dg, v[1], TOONTOWNCLIENT_CHECK_ONLINE_FRIENDS)
        dg:addUint32(userTable.avatarId)
        client:routeDatagram(dg)

        local fields = avatarFields[v[1]]
        resp:addUint32(v[1]) -- doId
        resp:addString(fields.setName[1]) -- name
        resp:addString(fields.setDNAString[1]) -- dna
        resp:addUint32(fields.setPetId[1]) -- petId
    end
    client:sendDatagram(resp)
end

function handleFriendOnline(client, dgi)
    local userTable = client:userTable()
    local friendId = dgi:readUint32()
    local speedChatPlus = dgi:readBool()

    if userTable.avatarId == nil then
        return
    end

    if friendId == userTable.avatarId then
        return
    end

    if userTable.friendsList == nil then
        -- Have not gotten our friends list yet.
        -- This will be resolved later by the queue
        return
    end

    for i, v in ipairs(userTable.friendsList) do
        if v[1] == friendId then
            -- Send a CLIENT_FRIEND_ONLINE message.
            local dg = datagram:new()
            dg:addUint16(CLIENT_FRIEND_ONLINE)
            dg:addUint32(friendId) -- doId
            dg:addUint8(v[2]) -- commonChatFlags
            if speedChatPlus then
                dg:addBool(speedChatPlus) -- whitelistChatFlags
            end

            client:sendDatagram(dg)
            break
        end
    end
end

function handleFriendOffline(client, dgi)
    local userTable = client:userTable()
    local friendId = dgi:readUint32()

    if userTable.avatarId == nil then
        return
    end

    if friendId == userTable.avatarId then
        return
    end

    if userTable.friendsList == nil then
        client:warn("handleFriendOffline: TODO: No friends list yet.")
        -- Have not gotten our friends list yet.
        -- TODO: Put the friendId in a queue table and
        -- wait until we have gotten the friends list
        -- before doing the check.
        return
    end

    for i, v in ipairs(userTable.friendsList) do
        if v[1] == friendId then
            -- Send a CLIENT_FRIEND_OFFLINE message.
            local dg = datagram:new()
            dg:addUint16(CLIENT_FRIEND_OFFLINE)
            dg:addUint32(friendId) -- doId
            client:sendDatagram(dg)
            break
        end
    end
end

function handleCheckFriendOnline(client, dgi)
    local userTable = client:userTable()
    local friendId = dgi:readUint32()

    if userTable.avatarId == nil then
        -- Not logged in yet.
        return
    end

    if userTable.friendsList == nil then
        client:warn("handleCheckFriendOnline: No friends list yet.")
        -- Put the friendId in a queue table and
        -- wait until we have gotten the friends list
        -- before doing the check.
        table.insert(userTable.friendQueue, friendId)
        return
    end

    checkFriendOnline(client, friendId)
end

function checkFriendOnline(client, friendId)
    local userTable = client:userTable()

    for i, v in ipairs(userTable.friendsList) do
        if v[1] == friendId then
            local dg = datagram:new()
            client:addServerHeaderWithAvatarId(dg, friendId, TOONTOWNCLIENT_FRIEND_ONLINE)
            dg:addUint32(userTable.avatarId)
            dg:addBool(userTable.speedChatPlus)
            client:routeDatagram(dg)
            break
        end
    end
end

function handleMakeFriend(client, dgi)
    local userTable = client:userTable()
    local friendId = dgi:readUint32()
    local flag = dgi:readUint8()

    if userTable.friendsList == nil then
        client:warn("handleMakeFriend: No friends list")
        return
    end

    local addNewFriend = true
    for i, v in ipairs(userTable.friendsList) do
        if v[1] == friendId then
            userTable.friendsList[i][2] = flag
            addNewFriend = false
            break
        end
    end

    if addNewFriend then
        table.insert(userTable.friendsList, {friendId, flag})
    end

    client:userTable(userTable)

    -- Declare the object's existance so they can teleport.
    client:declareObject(friendId, "DistributedToon")

    client:writeServerEvent("made-friends", "MewtwoClient", string.format("%d|%d", userTable.avatarId, friendId))

    -- Check if the friend is online (in case someone redeems a
    -- code while they're offline)
    local dg = datagram:new()
    client:addServerHeaderWithAvatarId(dg, friendId, TOONTOWNCLIENT_CHECK_ONLINE_FRIENDS)
    dg:addUint32(userTable.avatarId)
    client:routeDatagram(dg)
end

function handleClientRemoveFriend(client, friendId)
    local userTable = client:userTable()
    if userTable.friendsList == nil then
        client:warn("handleClientRemoveFriend: No friends list")
        return
    end

    for i, v in ipairs(userTable.friendsList) do
        if v[1] == friendId then
            -- Remove from our friends list.
            userTable.friendsList[i] = nil

            -- Undeclare the object
            client:undeclareObject(friendId)

            -- Update the object itself
            local dg = datagram:new()
            dg:addServerHeader(userTable.avatarId, 0, STATESERVER_OBJECT_UPDATE_FIELD)
            dg:addUint32(userTable.avatarId)
            client:packFieldToDatagram(dg, "DistributedToon", "setFriendsList", {userTable.friendsList}, true)
            client:routeDatagram(dg)

            client:writeServerEvent("removed-friend", "MewtwoClient", string.format("%d|%d", userTable.avatarId, friendId))

            -- Update the other friend's list as well.
            local function queryFriendsListResponse(doId, success, fields)
                if not success then
                    client:error(string.format("MewtwoClient: handleClientRemoveFriend: Unable to get friends list for friendId: %d", friendId))
                    return
                end
                if fields.setFriendsList ~= nil then
                    for i, v in ipairs(fields.setFriendsList[1]) do
                        if v[1] == userTable.avatarId then
                            fields.setFriendsList[1][i] = nil

                            -- Update the object itself
                            local dg = datagram:new()
                            dg:addServerHeader(friendId, 0, STATESERVER_OBJECT_UPDATE_FIELD)
                            dg:addUint32(friendId)
                            client:packFieldToDatagram(dg, "DistributedToon", "setFriendsList", fields.setFriendsList, true)
                            client:routeDatagram(dg)
                            return
                        end
                    end
                end
            end
            if friendId < 199999999 then
                client:getDatabaseValues(friendId, "DistributedToon", {"setFriendsList"}, queryFriendsListResponse)
            else
                client:queryObjectFields(friendId, "DistributedToon", {"setFriendsList"}, queryFriendsListResponse)
            end
            return
        end
    end
    client:error(string.format("handleClientRemoveFriend: friend %d not found!", friendId))
end

function handleGetAvatarDetails(client, dgi, className, responseMsg)
    local doId = dgi:readUint32()

    local function queryAvatarResponse(doId, success, fields)
        resp = datagram:new()
        resp:addUint16(responseMsg)
        resp:addUint32(doId)

        if not success then
            client:error(string.format("handleGetAvatarDetails: Unable to get avatar: %d", doId))
            resp:addUint8(1) -- error
            client:sendDatagram(resp)
            return
        end

        resp:addUint8(0) -- error
        for _, field in ipairs(fields) do
            local name = field[1]
            local value = field[2]
            client:packFieldToDatagram(resp, className, name, value, false)
        end
        client:sendDatagram(resp)
    end
    if doId > 199999999 then
        client:queryAllRequiredFields(doId, className, queryAvatarResponse)
    else
        client:getAllRequiredFromDatabase(doId, className, queryAvatarResponse)
    end
end

function handleClientDeleteAvatar(client, dgi)
    local avatarId = dgi:readUint32()

    local userTable = client:userTable()

    local isAvInList = checkIsAvInList(avatarId, userTable.avatars)
    if not isAvInList then
        client:sendDisconnect(CLIENT_DISCONNECT_GENERIC, string.format("Avatar %d not in list.", avatarId), true)
        return
    end

    client:getDatabaseValues(userTable.accountId, "Account", {"ACCOUNT_AV_SET_DEL", "HOUSE_ID_SET"}, function (doId, success, fields)
        if not success then
            client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "The Account object was unable to be queried.", true)
            return
        end

        local index = table.index(userTable.avatars, avatarId)

        -- Remove avatar from list
        userTable.avatars[index] = 0

        -- Add avatar to deleted avatar list as well
        table.insert(fields.ACCOUNT_AV_SET_DEL, {avatarId, os.time()})

        -- Reset house. (EstateAI will take care of setSlotToonId and setSlotItems)
        fields.HOUSE_ID_SET[index] = 0

        client:setDatabaseValues(userTable.accountId, "Account", {
            ACCOUNT_AV_SET = userTable.avatars,
            ACCOUNT_AV_SET_DEL = fields.ACCOUNT_AV_SET_DEL,
            HOUSE_ID_SET = fields.HOUSE_ID_SET
        })

        client:userTable(userTable)

        client:writeServerEvent("deleted-avatar", "MewtwoClient", string.format("%d", avatarId))

        client:getDatabaseValues(avatarId, "DistributedToon", {"setFriendsList"}, function (doId, success, fields)
            if not success then
                client:warn(string.format("handleClientDeleteAvatar: queryAvatarResponse: Avatar %d not found"))
                -- Send avatar deletion response
                handleGetAvatars(client, true)
                return
            end

            local friendsList = fields.setFriendsList[1]

            local function queryFriendResponse(friendId, success, friendFields)
                if not success then
                    client:error(string.format("handleClientDeleteAvatar: Unable to get friends list for friendId: %d", friendId))
                    return
                end

                if friendFields.setFriendsList ~= nil then
                    for i, v in ipairs(friendFields.setFriendsList[1]) do
                        if v[1] == avatarId then
                            friendFields.setFriendsList[1][i] = nil

                            -- Update the object itself
                            local dg = datagram:new()
                            dg:addServerHeader(friendId, 0, STATESERVER_OBJECT_UPDATE_FIELD)
                            dg:addUint32(friendId)
                            client:packFieldToDatagram(dg, "DistributedToon", "setFriendsList", friendFields.setFriendsList, true)
                            client:routeDatagram(dg)
                            return
                        end
                    end
                end
            end

            -- Fetch every friend and delete the newly-deleted avatar
            -- out of their friends lists.
            for i, pair in ipairs(friendsList) do
                local friendId = pair[1]
                if friendId < 199999999 then
                    client:getDatabaseValues(friendId, "DistributedToon", {"setFriendsList"}, queryFriendResponse)
                else
                    client:queryObjectFields(friendId, "DistributedToon", {"setFriendsList"}, queryFriendResponse)
                end
            end

            -- Clear out their friends list in case someone wants
            -- them restored.
            client:setDatabaseValues(avatarId, "DistributedToon", {
                setFriendsList = {{}}
            })

            -- Send avatar deletion response
            handleGetAvatars(client, true)
        end)
    end)
end

function filterWhitelist(message, filterOverride)
    local modifications = {}
    local wordsToSub = {}
    local offset = 0

    if filterOverride then
        local cleanMessage = "*"
        table.insert(modifications, {0, 0})
        return cleanMessage, modifications
    end

    local function stripLeadingAndTrailingPunctuation(word, reversed)
        -- Disney just stripped punctuation from the start and end of the word. This allows words with punctuation to be in the whitelist.
        local pattern = "[.,?!]+"
        local strippedWord = word
        local matchStart, matchEnd = string.find(strippedWord, pattern)

        -- Strip leading characters.
        if matchStart == 1 then
            strippedWord = string.sub(strippedWord, matchEnd + 1)
        end

        -- We will reverse the word and call ourself again if we haven't already, to make checking for trailing characters easier.
        local reversedWord = string.reverse(strippedWord)

        if not reversed then
            return stripLeadingAndTrailingPunctuation(reversedWord, true)
        end

        -- Return the reversed word. This will actually be the normal word since we only get here in the reversed call.
        return reversedWord
    end

    local function isWordOnWhitelist(word)
        local wordToFind = string.lower(word)

        -- If the word is already on the whitelist, we can return immediately.
        if WHITELIST[wordToFind] then
            return true
        end

        wordToFind = stripLeadingAndTrailingPunctuation(wordToFind, false)

        -- Now return whether the word is in the whitelist.
        return WHITELIST[wordToFind]
    end

    -- Match any character except spaces.
    for word in string.gmatch(message, "[^%s]*") do
        if filterOverride == true or word ~= "" and isWordOnWhitelist(word) ~= true then
            table.insert(modifications, {offset, offset + string.len(word) - 1})
            table.insert(wordsToSub, word)
        end
        if word ~= "" then
            offset = offset + string.len(word) + 1
        end
    end
    local cleanMessage = message
    for _, modification in ipairs(modifications) do
        local length = modification[2] - modification[1] + 1
        cleanMessage = string.sub(cleanMessage, 0, modification[1]) .. string.rep("*", length) .. string.sub(cleanMessage, modification[1] + 1 + length)
    end

    return cleanMessage, modifications
end

-- setTalk from client
function handleClientDistributedToon_setTalk(client, doId, fieldId, data)
    -- The data is safe to use, as the ranges has already been
    -- verified by the server prior to calling this function.

    local userTable = client:userTable()
    local accountId = userTable.accountId
    local avatarId = userTable.avatarId
    local avatarName = userTable.avatarName

    -- All other data are blank values, except for chat.
    local message = data[4] --chat

    -- Log it for moderation purposes.
    local cleanMessage, _ = filterWhitelist(message, false)
    client:writeServerEvent("chat-message", "MewtwoClient", string.format("%d|%d|%s|%s", accountId, avatarId, message, cleanMessage))

    local dg = datagram:new()
    -- We set the sender field to the doId instead of our channel to make sure
    -- we can receive the broadcast.
    dg:addServerHeader(doId, doId, STATESERVER_OBJECT_UPDATE_FIELD)
    dg:addUint32(doId)
    client:packFieldToDatagram(dg, "DistributedToon", "setTalk", {avatarId, accountId, avatarName, message, {}, 0}, true)
    client:routeDatagram(dg)
end

-- setTalk from server
function handleDistributedToon_setTalk(client, doId, fieldId, data)
    -- The data is safe to use, as the ranges has already been
    -- verified by the server prior to calling this function.

    local userTable = client:userTable()

    local avatarId = data[1]
    local accountId = data[2]
    local avatarName = data[3]
    local message = data[4]
    -- The rest are intentionally left blank.
    local modifications = {}

    local shouldFilterMessage = true
    local notSecretFriends = true
    if userTable.friendsList ~= nil then
        if avatarId == userTable.avatarId then
            -- That's us.  Don't filter from whitelist
            -- if one of our friends is a true friend
            for i, v in ipairs(userTable.friendsList) do
                if userTable.friendsList[i][2] == 1 then
                    shouldFilterMessage = false
                    notSecretFriends = false
                    break
                end
            end
        else
            -- That's a different person.  Check if that person
            -- is a true friend:
            for i, v in ipairs(userTable.friendsList) do
                if userTable.friendsList[i][1] == avatarId and userTable.friendsList[i][2] == 1 then
                    shouldFilterMessage = false
                    notSecretFriends = false
                    break
                end
            end
        end
    end

    -- Special cases
    local filterOverride = true

    -- sender, receiver
    if (avatarSpeedChatPlusStates[avatarId] and userTable.speedChatPlus) or (notSecretFriends == false) then
        filterOverride = false
    end

    if shouldFilterMessage then
        message, modifications = filterWhitelist(message, filterOverride)
    end

    local dg = datagram:new()
    dg:addUint16(CLIENT_OBJECT_UPDATE_FIELD)
    dg:addUint32(doId)
    client:packFieldToDatagram(dg, "DistributedToon", "setTalk", {avatarId, accountId, avatarName, message, modifications, 0}, true)
    client:sendDatagram(dg)
end

function handleClientDistributedToon_setTalkWhisper(client, doId, fieldId, data)
    -- The data is safe to use, as the ranges has already been
    -- verified by the server prior to calling this function.

    local userTable = client:userTable()
    local accountId = userTable.accountId
    local avatarId = userTable.avatarId
    local avatarName = userTable.avatarName

    -- All other data are blank values, except for chat.
    local message = data[4] --chat

    if message == "" then
        return
    end

    local cleanMessage, modifications = filterWhitelist(message)
    -- Check friends list if what we're sending this too is a true friend:
    if userTable.friendsList ~= nil then
        for i, v in ipairs(userTable.friendsList) do
            if v[1] == doId and v[2] == 1 then
                -- Send unfiltered message
                cleanMessage, modifications = message, {}
            end
        end
    end

     -- Log it for moderation purposes.
     client:writeServerEvent("chat-message-whisper", "MewtwoClient", string.format("%d|%d|%s|%s", avatarId, doId, message, cleanMessage))

    local dg = datagram:new()
    -- We set the sender field to the doId instead of our channel to make sure
    -- we can receive the broadcast.
    dg:addServerHeader(doId, doId, STATESERVER_OBJECT_UPDATE_FIELD)
    dg:addUint32(doId)
    client:packFieldToDatagram(dg, "DistributedToon", "setTalkWhisper", {avatarId, accountId, avatarName, cleanMessage, modifications, 0}, true)
    client:routeDatagram(dg)
end

-- sendMessage from client
function handleClientCentralLogger_sendMessage(client, doId, fieldId, data)
    -- The data is safe to use, as the ranges has already been
    -- verified by the server prior to calling this function.
    local category = data[1]
    local eventString = data[2]
    local targetDISLId = data[3]
    local targetAvId = data[4]

    local toLog = eventString .. "|" .. string.format("%d", targetDISLId) .. "|" .. string.format("%d", targetAvId)
    client:writeServerEvent(category, "CentralLogger", toLog)
end
