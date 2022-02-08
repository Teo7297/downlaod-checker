import sys, time
from endings import send_alert, poweroff
from monitor_ntw import Network_monitor

ENDINGS = {'-a' : send_alert, '-off' : poweroff}

def main():
    complete = False
    count = 0
    monitor = Network_monitor()

    while not complete:
        time.sleep(1)
        while monitor.get_download_rate() == 0:
            time.sleep(1)
            count += 1
            if count > 10:
                complete = True
                break
        count = 0
    ENDINGS[sys.argv[1]]()
    
    
def print_err():
    print('Error insert a valid parameter\n  -a : Send an alert message when the download is complete\n  -off : Turns off the pc when the download is complete (waits a couple minutes to complete the installation)')

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ENDINGS:
        print_err()
    else:
        main()
        print("running..")