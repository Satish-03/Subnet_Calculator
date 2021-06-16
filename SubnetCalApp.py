from ip_addr_valid import ip_addr_valid
from subnet_mask_validity import subnet_mask_validity
from sub_calculator1 import sub_calculator1
import sys
ip = input("Enter an ip address :")
try:
    ip_addr_valid(ip)

except KeyboardInterrupt:
    print("\n\n Program aborted by user. Exting :( ")
    sys.exit()

subnet_mask = input("Enter a subnet mask :")
try:
    subnet_mask_validity(subnet_mask)

except KeyboardInterrupt:
    print("\n Program aborted by user. Exting :( ")
    sys.exit()


sub_calculator1()
    

    

