import parted
import os
import sys

euid = os.geteuid()
if euid != 0:
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print(parted.getAllDevices())
for device in parted.getAllDevices():
    print(device)
    print(device.model + " - " + str(device.length) + " GB (" + device.path + ")")
device = parted.getDevice("/dev/sdb")
disk = parted.freshDisk(device, "msdos")
#disk = parted.newDisk(device)
print(device.length * device.sectorSize)
print(disk.maxPrimaryPartitionCount)
print()