# monitor.py
import psutil  # import psutil to get system information


def get_cpu_percent():
    return psutil.cpu_percent(interval=1)  # return CPU usage percentage over 1 second interval

def get_memory_info():                  # get memory usage details
    mem = psutil.virtual_memory()  # get virtual memory details
    used_gb = mem.used / (1024 ** 3)  # convert used memory to GB
    total_gb = mem.total / (1024 ** 3)  # convert total memory to GB
    return mem.percent, used_gb, total_gb  # return memory usage percentage, used GB, total GB

def get_disk_info():                    # get disk usage details
    disk = psutil.disk_usage('/')  # get disk usage details for root directory
    used_gb = disk.used / (1024 ** 3)  # convert used disk space to GB
    total_gb = disk.total / (1024 ** 3)  # convert total disk space to GB
    return disk.percent, used_gb, total_gb  # return disk usage percentage, used GB, total GB


