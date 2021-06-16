#importing the necessary modules
import sys
import random

def sub_calculator(ip, subnet_mask):
        #Converting mask to binary strings
    sub_octet = subnet_mask.split('.')
    bin_sub = []
    for i in sub_octet:
        b = ("{0:b}".format(int(i)))
        bin_sub.append(b.zfill(8))
    binary_subnet = "".join(bin_sub)
    
    
        #Counting the number of host bits in the mask and calculating the number of hots and subnet#method1
    host_bit = []
    for i in bin_sub:
        for v in i:
            host_bit.append(v)

    num_host_bit = host_bit.count('0')
    num_sub_bit = 32 - num_host_bit
    num_host = abs(2**num_host_bit - 2)

        ##Counting the number of host bits in the mask and calculating the number of hots and subnet#method2
        #binary_mask = "".join(bin_sub)
        #num_host_bit = binary_mask.count('0')
        #num_sub_bit = 32 - num_host
        #num_host = abs(2**num_host_bit - 2)

        #Obtaining the wildcard mask
    wildcard_octet = []
    for octet in sub_octet:
        wild_octet = 255 - int(octet)
        wildcard_octet.append(str(wild_octet))

    wildcard_mask = ".".join(wildcard_octet)

        #Converting ip to binary strings
    ip_octet = ip.split('.')
    bin_ip = []
    for i in ip_octet:
        b = ("{0:b}".format(int(i)))
        bin_ip.append(b.zfill(8))
    binary_ip = "".join(bin_ip)

        #Calculation the network add and broadcast address
    net_addr_bin = binary_ip[:(num_sub_bit)] + "0"*num_host_bit

    broad_addr_bin = binary_ip[:(num_sub_bit)] + "1"*num_host_bit

        #Converting evrything back to decimal
        #Converting the broadcast back to decimal
    net_ip_octet = []
    for bit in range(0,32,8):
        octet = net_addr_bin[bit:bit+8]
        net_ip_octet.append(octet)
    
    net_ip_addr = []
    for octet in net_ip_octet:
        dec_octet = int(octet,2)
        net_ip_addr.append(str(dec_octet))

    network_ip_addr = ".".join(net_ip_addr)

        #Converting the broadcast back to decimal

    broad_ip_octet = []
    for bit in range(0,32,8):
        octet = broad_addr_bin[bit:bit+8]
        broad_ip_octet.append(octet)
    
    broad_ip_addr = []
    for octet in broad_ip_octet:
        dec_octet = int(octet,2)
        broad_ip_addr.append(str(dec_octet))

    broadcast_ip_addr = ".".join(broad_ip_addr)

        #Printing thr results for selected IP/mask
    print("\n")
    print("Network address is: %s" %network_ip_addr)
    print("Broadcast address is: %s" %broadcast_ip_addr)
    print("Number of valid hosts per subnet: %s" %num_host)
    print("Wildcast mask: %s" %wildcard_mask)
    print("Mask bits: %s" %num_sub_bit)
    print("\n")
 


        
    

        
        
    



        
        
