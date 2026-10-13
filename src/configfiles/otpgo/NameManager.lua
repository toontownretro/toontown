OTP_DO_ID_NAME_APPROVAL = 4715

NAME_APPROVAL_REQUEST_NAME = 14000

local http = require("http")
local json = require("json")

function sendToDiscord(hook, color, name, message, fields)
    local embed = {
          {
              ["color"] = color,
              ["title"] = "**".. name .."**",
              ["description"] = message,
              ["fields"] = fields
          }
      }

    http.post(hook, {
        body=json.encode({username = name, embeds = embed}),
        headers={
            ["Content-Type"]="application/json"
        }
    })
end

function init(participant)
    participant:subscribeChannel(OTP_DO_ID_NAME_APPROVAL)
end

function handleDatagram(participant, msgType, dgi)
    if msgType == NAME_APPROVAL_REQUEST_NAME then
        handleRequestName(participant, dgi)
    else
        participant:warning(string.format("Got unknown message type: %d", msgType))
    end
end

function handleRequestName(participant, dgi)
    local avId = dgi:readUint32()
    local avatarName = dgi:readString()
    local webhookUrl = dgi:readString()

    sendToDiscord(webhookUrl, 1127128, "Name Approval", "New avatar typed name request has arrived.", {
        {
            name = 'Avatar Id',
            value = avId,
            inline = true
        },
        {
            name = 'Name',
            value = avatarName,
            inline = true
        },
        {
            name = 'Server Type',
            value = 1, -- Final Toontown
            inline = true
        }
    })
end
