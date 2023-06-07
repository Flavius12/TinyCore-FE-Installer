import parted
import os
import sys

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.2f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.2f} Y{suffix}"

euid = os.geteuid()
if euid != 0:
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print(parted.getAllDevices())
for device in parted.getAllDevices():
    print(device)
    print(device.model + " - " + sizeof_fmt(device.length * device.sectorSize) + " (" + device.path + ")")
device = parted.getDevice("/dev/sdb")
disk = parted.freshDisk(device, "msdos")
#disk = parted.newDisk(device)
print(device.length * device.sectorSize)
print(disk.maxPrimaryPartitionCount)
print()