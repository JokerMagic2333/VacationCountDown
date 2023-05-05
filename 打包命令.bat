chcp 65001
Pyinstaller -F -w %~dp0\main.py -n 假期倒计时 -i %~dp0\logo.ico
COPY /Y %~dp0\cfg.ini %~dp0\dist\
COPY /Y %~dp0\设置开机自启动.bat %~dp0\dist\
COPY /Y %~dp0\取消开机自启动.bat %~dp0\dist\