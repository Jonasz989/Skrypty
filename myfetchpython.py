#!/usr/bin

import platform
import psutil
import datetime
import time

kb = 1024
Mb = 1024 * 1024

def print_system_info():

    print("         _       **  ")
    print("        | |      __  ")
    print("     ___| |     |  | ")
    print("    / __  |     |  | ")
    print("   | (__| |    /|  | ")
    print("    \_____|   / /\ | ")
    print("              \ \/ / ")
    print("               \__/  ")
    print("                     ")
    print("")
    print("OS:     " + platform.system())
    print("Release:" + platform.release())
    print("Kernel: " + platform.version())
    print("CPU:    " + platform.processor())



def read_system():
    with open('/var/log/zapis.log', 'a') as file:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        print("Current date and time: ", now.strftime("%Y-%m-%d"), current_time, file=file)

        i = 0
        for load in psutil.cpu_percent(interval=1, percpu=True):
            print("CPU " + str(i) + " usage: " + str(load) + "%", file=file)
            i += 1

        print(f"Total mem: {round(psutil.virtual_memory().total / Mb, 2)} Mb", file=file)
        print(f"Used mem: {round(psutil.virtual_memory().used / Mb, 2)} Mb", file=file)
        print(f"Free mem: {round(psutil.virtual_memory().available / Mb, 2)} Mb", file=file)

        print(f"Total swap: {round(psutil.swap_memory().total / Mb, 2)} Mb", file=file)
        print(f"Used swap: {round(psutil.swap_memory().used / Mb, 2)} Mb", file=file)

        print(f"Total disk: {round(psutil.disk_usage('/').total / Mb, 2)} Mb", file=file)
        print(f"Used disk: {round(psutil.disk_usage('/').used / Mb, 2)} Mb", file=file)
        print(f"Free disk: {round(psutil.disk_usage('/').free / Mb, 2)} Mb", file=file)


        print(f"Total kb sent: {round(psutil.net_io_counters().bytes_sent / kb, 2)} kb", file=file)
        print(f"Total kb received: {round(psutil.net_io_counters().bytes_recv / kb, 2)} kb", file=file)

        net_io_counters = psutil.net_io_counters()
        up_speed_start = net_io_counters.bytes_sent / 1024
        dw_speed_start = net_io_counters.bytes_recv / 1024

        time.sleep(1)
        net_io_counters = psutil.net_io_counters()
        up_speed_end = net_io_counters.bytes_sent / 1024
        dw_speed_end = net_io_counters.bytes_recv / 1024

        print("Upload: %.2f KB/s | Download: %.2f KB/s" % (round(up_speed_end - up_speed_start, 2), round(dw_speed_end - dw_speed_start, 2)), file=file)


read_system()
