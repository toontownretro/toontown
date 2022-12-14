REM We setup our needed enviorment here.
call env.bat
call cta toontown
set uberdog_objects=gifting party
title Toontown [UberDOG Server]

%PYTHON_LOCATION%\python.exe -m toontown.uberdog.Start
pause