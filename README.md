
**Easy Android PayLoad Maker (EAPM) - Version 1.0**

Empower your security testing with Easy Android PayLoad Maker (EAPM) – a versatile tool designed to streamline the creation of payload APK files for Android devices. EAPM combines simplicity with power, offering an intuitive interface that simplifies the process of generating payloads while leveraging the robust capabilities of the Metasploit Framework.

**Key Features:**

🚀 **Effortless Payload Generation:** With EAPM, creating payload APK files is a breeze. Customize parameters such as IP address and port with ease, tailoring payloads to your specific needs.

🌐 **Seamless Integration with Apache2:** EAPM seamlessly integrates with Apache2, allowing you to move generated APK files to the `/var/www/html` directory effortlessly. Your payloads are instantly accessible via the Apache2 web server, streamlining deployment.

🔧 **Convenient Apache2 Service Management:** Take control of the Apache2 service directly from EAPM. Start or stop the service with a simple command, eliminating the need for manual intervention.

**Prerequisites:**

To unleash the full potential of EAPM, ensure you have the following prerequisites installed:

- Python 3
- Colorama library
- Metasploit Framework
- Apache2

**Get Started:**

1. Launch EAPM and navigate through the intuitive menu.
2. Customize payload parameters or manage the Apache2 service effortlessly.
3. Access your generated APK files via the Apache2 web server for comprehensive testing and deployment.

**Credits:**

Easy Android PayLoad Maker (EAPM) is the brainchild of ShadowByte, crafted to elevate your security testing experience.

## Installation

To get started with Easy Android PayLoad Maker (EAPM), follow these simple steps:

### Prerequisites

Ensure you have the following prerequisites installed:

- Python 3
- Colorama library
- Metasploit Framework
- Apache2

### Installation Script

Run the provided installation script to automatically install the prerequisites:

```bash
# Make the installation script executable
chmod +x install_prerequisites.sh

# Run the installation script with sudo
sudo ./install_prerequisites.sh
```

### Manual Installation

If you prefer manual installation, follow these steps:

1. Install Python 3:

```bash
# For Debian-based systems (e.g., Ubuntu)
sudo apt update
sudo apt install python3
```

2. Install Colorama library:

```bash
pip3 install colorama
```

3. Install Metasploit Framework:

```bash
sudo apt update
sudo apt install -y metasploit-framework
```

4. Install Apache2:

```bash
sudo apt install -y apache2
```

## Usage

Easy Android PayLoad Maker (EAPM) offers a user-friendly interface for generating payload APK files and managing the Apache2 service. Follow these steps to get started:

1. Launch EAPM by running the main script with sudo:

```bash
sudo python3 EAPM.py
```

2. Navigate through the intuitive menu and select the desired option:

   - **Create Payload APK**: Generate payload APK files with customizable parameters.
   - **Move APK to /var/www/html**: Move generated APK files to the `/var/www/html` directory for easy access via Apache2.
   - **Manage Apache2 Service**: Start or stop the Apache2 service directly from EAPM.

3. Follow the prompts to customize payload parameters or manage the Apache2 service.

4. Access your generated APK files via the Apache2 web server for testing and deployment.
