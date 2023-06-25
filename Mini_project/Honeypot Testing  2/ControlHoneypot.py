import subprocess
import sys

def start_honeypot():
    print('Starting honeypot...')
    subprocess.run(['python', 'C:/users/joyab/Documents/Programming/Mini_project/Test2/Honeypot.py'])

def stop_honeypot():
    print('Stopping honeypot...')
    subprocess.run(['taskkill', '/F', '/IM', 'python.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def menu():
    print('Honeypot control menu:')
    print('1. Start honeypot')
    print('2. Stop honeypot')
    print('3. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        start_honeypot()
    elif choice == 2:
        stop_honeypot()
    elif choice == 3:
        sys.exit(0)
    else:
        print('Invalid choice')
    menu()

if __name__ == '__main__':
    menu()