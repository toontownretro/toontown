title Toontown [UberDOG Server]
:: cd into root
cd ../../../
call env.bat
call cta toontown
set uberdog_objects=friends speedchatRelay gifting mail party RAT award coderedemption ingamenews whitelist cpuinfo security randomsource
:main
%PYTHON_LOCATION%\python.exe -m toontown.uberdog.Start
goto main
