import sys

#Checking octets
def subnet_mask_validity(subnet):
    subnet_valid = [0,128, 192, 224, 240, 248, 252, 254, 255]
    octet_list = subnet.split('.')
   
        
    if (len(octet_list) == 4) and (int(octet_list[0]) in subnet_valid) and (int(octet_list[1]) in subnet_valid
        ) and (int(octet_list[2]) in subnet_valid) and (int(octet_list[3]) in subnet_valid) and (int(octet_list[0])
        ) >= (int(octet_list[1])) >= (int(octet_list[2])) >= (int(octet_list[3])):
        return
        
             
    else:
        print('\n* That was an invalid subnet mask: {} :(\n'.format(subnet))
        sys.exit()


