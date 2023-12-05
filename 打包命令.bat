chcp 65001
Pyinstaller -F -w %~dp0main.py -n 假期倒计时 -i %~dp0logo.ico
COPY /Y %~dp0cfg.ini %~dp0dist\
COPY /Y %~dp0设置开机自启动.bat %~dp0dist\
COPY /Y %~dp0取消开机自启动.bat %~dp0dist\