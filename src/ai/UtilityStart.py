import time
import os
import sys

# Initialize ihooks importer On the production servers, we run genPyCode -n
# meaning no squeeze, so nobody else does this. When we squeeze, the
# unpacker does this for us and it does not hurt to do in either case.
import ihooks
ihooks.install()

print("Initializing...")

from otp.ai.AIBaseGlobal import *
from . import UtilityAIRepository

simbase.mdip = ConfigVariableString("msg-director-ip", "localhost").getValue()
simbase.mdport = ConfigVariableInt("msg-director-port", 6665).getValue()
simbase.esip = ConfigVariableString("event-server-ip", "localhost").getValue()
simbase.esport = ConfigVariableInt("event-server-port", 4343).getValue()

districtType = 0
ssId = ConfigVariableInt("utility-ssid", 20100000).getValue()
utilityChannel = ConfigVariableInt("utility-channel", 399900000).getValue()

if ConfigVariableBool("want-dev", 0).getValue():
    # In development, the dcfiles are specified in prc files
    dcFileNames = None
else:
    # In production we have to list them out
    dcFileNames = ['otp.dc', 'toon.dc']

simbase.air = UtilityAIRepository.UtilityAIRepository(simbase.mdip,
                                                      simbase.mdport,
                                                      simbase.esip,
                                                      simbase.esport,
                                                      dcFileNames,
                                                      1,
                                                      "Utility",
                                                      districtType,
                                                      ssId,
                                                      utilityChannel,
                                                      utilityChannel + 1)

# How we let the world know we are not running a service
simbase.aiService = 0
