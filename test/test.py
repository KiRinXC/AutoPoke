import wmi
c = wmi.WMI()
for item in c.Win32_ComputerSystemProduct():
    print(item.UUID)