chcp 65001
Pyinstaller -F -w %~dp0\main.py -n 假期倒计时
COPY %~dp0\cfg.ini %~dp0\dist\cfg.ini