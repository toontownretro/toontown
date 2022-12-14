title Toontown [AI Server]
:: cd into root
cd ../../../
call env.bat
call cta toontown
:main
%PYTHON_LOCATION%\python.exe -m toontown.ai.AIStart
goto main
