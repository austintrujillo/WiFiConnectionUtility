#!/bin/python3

# Netctl WiFi Connection Utility
# Austin Trujillo
# Created 2018 April 02
# Updated 2018 April 03


import os, sys

networks = [f for f in os.listdir('/etc/netctl/') if os.path.isfile(os.path.join('/etc/netctl', f))]


def selectNetwork():
    print('WiFi Connection Utility\n')
    for i, n in enumerate(networks):
        print('[' + str(i) + ']' + ' ' + n)

    try:
        userinput = input('\nSelect a network: ')
        
        if 0 <= int(userinput) <= len(networks):
            connectToNetwork(int(userinput))
        else:
            raise ValueError

    except ValueError:
        print("\nInvalid Input. Exiting...\n")


def connectToNetwork(n):
    print('\nAttempting to connect to %s...\n' % (networks[n]))

    try:
        os.system('sudo killall dhcpcd 2> /dev/null')
        os.system('sudo netctl stop-all 2> /dev/null')
        os.system('sudo killall wpa_supplicant 2> /dev/null')
        os.system('sudo systemctl stop NetworkManager.service 2> /dev/null')
        os.system('sudo netctl start ' + networks[n])
        print('\nSuccessfully connected to ' + networks[n] + '\n')
    except StandardError:
        print('\nUnable to Connect to ' + networks[n] + '. Exiting...\n')


os.system('clear')

if len(sys.argv) > 1:
    argnet = str(sys.argv[1]).lower()

    if argnet in networks:
        connectToNetwork(networks.index(argnet))
    else:
        print('Network not saved! Please run wifi-menu')

else:
    selectNetwork()
