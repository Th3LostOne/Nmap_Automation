**Nmap Automated Scanner**

This project provides a Python script to automate scanning for active IPs and MAC addresses in a given subnet using **Nmap**. 
It identifies devices, their MAC addresses, and their vendors, and saves the results into a file while avoiding duplicate entries.

## Features
- Scans a specified subnet to detect active IPs, MAC addresses, and vendors.
- Automatically stores unique results in a text file.
- Provides an easy-to-understand output format for scanned devices.

## Prerequisites

Before using this script, ensure the following are installed on your system:

1. **Python 3.x**
2. **Nmap** command-line tool
   - Install Nmap via the package manager for your OS:
     - **Ubuntu/Debian**:
       ```bash
       sudo apt install nmap
       
     - **Windows**: Download from the [official website](https://nmap.org/).
3. Necessary Python libraries (these are included in the standard library):
   - `subprocess`
   - `re`
   - `os`

## Usage

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script**
   - Specify the subnet to scan in the `subnet_ip` variable (e.g., `172.16.3.0/24`).
   - Execute the script:
     ```bash
     python Nmap_Automated.py
     ```

3. **Results**
   - The script scans the specified subnet and prints active IPs, MAC addresses, and vendors to the terminal.
   - Unique results are saved to a file named `active_ips_and_macs.txt` in the script's directory.

---

## How It Works

1. **Subnet Scanning**
   - The script uses the `nmap -sP` command to ping all devices in the specified subnet.

2. **Output Parsing**
   - It parses Nmap's output to extract:
     - IP addresses
     - MAC addresses
     - Vendor information

3. **Result Management**
   - Compares scanned results with existing entries in `active_ips_and_macs.txt`.
   - Adds only new entries to avoid duplicates.

---

## Example Output

Terminal Output:
```
Active IPs and MACs found:
IP: 172.16.3.10, MAC: AA:BB:CC:DD:EE:FF, Vendor: Dell Inc.
IP: 172.16.3.15, MAC: 11:22:33:44:55:66, Vendor: Apple, Inc.
```

File (`active_ips_and_macs.txt`):
```
172.16.3.10 - AA:BB:CC:DD:EE:FF - Dell Inc.
172.16.3.15 - 11:22:33:44:55:66 - Apple, Inc.
```

---

## Limitations

- Requires `sudo`/administrator privileges to run Nmap.
- May not detect all devices if they block ping requests or hide their MAC addresses.

---

## License

This project is open-source and available under the MIT License.

---

Feel free to update this file as your project evolves!
