import psutil
from prometheus_client import Gauge

cpu_usage_gauge = Gauge("system_cpu_usage_percent", "CPU usage percent")
memory_usage_gauge = Gauge("system_memory_usage_percent", "Memory usage percent")
disk_usage_gauge = Gauge("system_disk_usage_percent", "Disk usage percent")

def collect_system_metrics():
    cpu_usage_gauge.set(psutil.cpu_percent())
    memory_usage_gauge.set(psutil.virtual_memory().percent)
    disk_usage_gauge.set(psutil.disk_usage('/').percent)