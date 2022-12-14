REM We setup our needed enviorment here.
call env.bat
call cta toontown
title Toontown [AI Server]

%PYTHON_LOCATION%\python.exe -m toontown.ai.AIStart
pause