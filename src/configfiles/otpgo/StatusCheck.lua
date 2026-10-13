GET_SERVER_STATUS = 15000
GET_SERVER_STATUS_RESP = 15001

SERVER_TYPE = "Final Toontown"

local http = require("http")

function getStatus()
    response, error_message = http.get("https://api.sunrise.games/api/getStatusForServer?serverType=" .. SERVER_TYPE, {})
    return tonumber(response.body)
end

function init(participant)
    participant:subscribeChannel(GET_SERVER_STATUS)
end

function handleDatagram(participant, msgType, dgi)
    if msgType == GET_SERVER_STATUS then
        handleGetServerStatus(participant, dgi)
    else
        participant:warning(string.format("Got unknown message type: %d", msgType))
    end
end

function handleGetServerStatus(participant, dgi)
    local dg = datagram:new()
    dg:addServerHeader(participant:getSender(), GET_SERVER_STATUS, GET_SERVER_STATUS_RESP)
    dg:addUint8(getStatus()) -- serverStatus
    dg:addString(dgi:readString()) -- accountType
    participant:routeDatagram(dg)
end
