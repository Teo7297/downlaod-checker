import psutil

def convert_to_mbit(value):
    return int(value/1024./1024.*8)

class Network_monitor():
    def __init__(self):
        self.old = convert_to_mbit(psutil.net_io_counters().bytes_recv)
    def get_download_rate(self):
        new_value = convert_to_mbit(psutil.net_io_counters().bytes_recv)
        res = new_value - self.old
        self.old = new_value
        print(res, 'Mbit/s')
        return res
        
            




