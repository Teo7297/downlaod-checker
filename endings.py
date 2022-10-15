import ctypes, time, sys, os

def send_alert():
    print('\a')
    if ctypes.windll.user32.MessageBoxW(0, "Download completed!", "Download alert", u'MB_SETFOREGROUND') == 1:
        sys.exit()  

def poweroff():
    time.sleep(300) #the app may need some time to finalize a big download
    os.system("shutdown /s /t 1")