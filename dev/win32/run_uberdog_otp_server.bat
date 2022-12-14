title Toontown [UberDOG Server]
:: cd into root
cd ../../../
call env.bat
call cta toontown
set uberdog_objects=gifting party
:main
%PYTHON_LOCATION%\python.exe -m toontown.uberdog.Start
goto main
