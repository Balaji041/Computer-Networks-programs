import random
def get_ip():
    f=open("mac.txt","r")
    macl=[]
    macl=f.readlines()
    macn=random.randrange(0,len(macl))
    mac=macl[macn]
    mac=mac.replace('\n','')
    mac1=mac
    mac=mac.replace('-','')
    octets = [mac[i:i+2] for i in range(0, len(mac), 2)]
    ipn = [int(i, 16) for i in reversed(octets)]
    ipn.reverse()
    ip = '.'.join(str(i) for i in ipn)
    f2=open("ip.txt","r")
    ipl=[]
    ipl=f2.readlines()
    for i in range(len(ipl)):
        ipl[i]=ipl[i].replace('\n','')
        if ip==ipl[i]:
            print("for the mac address",mac1,"ip address is",ip,"found at index",i)
        else:
            continue
get_ip()
