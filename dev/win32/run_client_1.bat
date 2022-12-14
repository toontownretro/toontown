title Toontown [Dev Client]
:: cd into root
cd ../../../
call env.bat
call cta toontown
:main
%PYTHON_LOCATION%\python.exe -m toontown.toonbase.ToontownStart
goto main
