import parted
import os
import sys
import re

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

'''for device in parted.getAllDevices():
    os.system("clear")
    success = False
    if re.match("^([^0-9]+)$", os.path.basename(device.path)):
        print(device)
        print(device.model + " - " + sizeof_fmt(device.length * device.sectorSize) + " (" + device.path + ")")
        #disk = parted.newDisk(device)
    #print(device.probeFileSystem(device.biosGeometry))
    #print(disk)
    input()
'''

device = parted.getDevice("/dev/sda")
#disk = parted.freshDisk(device, "msdos")
disk = parted.newDisk(device)
print(device.length * device.sectorSize)
print(disk.maxPrimaryPartitionCount)
partitionList = list()
for primaryPartition in disk.getPrimaryPartitions():
    #print("Primary")
    #print("Name: " + primaryPartition.path + " Type: Primary " + "Size: " + sizeof_fmt(primaryPartition.getSize(unit="b")) + " Filesystem: " + primaryPartition.fileSystem.type)
    #print(primaryPartition)
    #print(primaryPartition.geometry)
    partitionList.append((0, primaryPartition))
if disk.getExtendedPartition():
    #print("Extended:")
    #print(disk.getExtendedPartition())
    partitionList.append((1, disk.getExtendedPartition()))
partitionList.sort(key=lambda item: item[1].geometry.start)
partitionsPrimaryExtendedOnly = list(filter(lambda item : item[0] == 0 or item[0] == 1, partitionList))
for freePartition in disk.getFreeSpacePartitions():
    #print("Free:")
    #print(freePartition)
    #print(freePartition.geometry)
    #print(sizeof_fmt(freePartition.getSize(unit="b")))
    if not partitionsPrimaryExtendedOnly: # No partitions found
        partitionList.append((2, freePartition))
    elif freePartition.geometry.end < partitionsPrimaryExtendedOnly[0][1].geometry.start and partitionsPrimaryExtendedOnly[0][1].geometry.start > (1024 * 1024 / device.sectorSize):
        partitionList.append((2, freePartition))
    elif freePartition.geometry.end > partitionsPrimaryExtendedOnly[-1][1].geometry.end and (device.length - 1 - partitionsPrimaryExtendedOnly[-1][1].geometry.end) >= (1024 * 1024 / device.sectorSize):
        partitionList.append((2, freePartition))
partitionList.sort(key=lambda item: item[1].geometry.start)
for partition in partitionList:
    print("------")
    if partition[0] == 0:
        print("PRIMARY")
    elif partition[0] == 1:
        print("EXTENDED")
    elif partition[0] == 2:
        print("FREE")
    #print(partition[1])
    print(partition[1].type)
    print(os.path.basename(partition[1].path))
    print(sizeof_fmt(partition[1].getSize(unit="b")))
    print("------")
print()