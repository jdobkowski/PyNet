
#!/usr/bin/env python
#
# class 1 exe 8 using function
#
'''
Use the ciscoconfparse library to find the crypto maps that are using pfs group2
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Use the ciscoconfparse library to find the crypto maps that are using pfs
    group2
    '''
    cisco_file = 'RTR-cfg.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', # looks for crypto-map name CRYPTO
                                                 childspec=r'pfs group2') # looks for fps gorup2 in crypto-map
    print "\nCrypto Maps using PFS group2:" 
    for entry in crypto_maps:
        print "  {0}".format(entry.text)
    print

if __name__ == "__main__":
    main()

