import subprocess
import re
import os


def scan_active_ips_and_macs(subnet_ip):
    try:
        # Running the command onto the cmd or terminal
        # this commands will output the mac, ip and OS
        result = subprocess.run(['sudo', 'nmap', '-sP', subnet_ip], capture_output=True, text=True)

        # if any error occur this will catch it
        if result.returncode != 0:
            print(f"Error running nmap: {result.stderr}")
            return []

        # taking the ip and mac from the output command
        pattern_ip = re.compile(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)')
        pattern_mac = re.compile(r'MAC Address: ([0-9A-Fa-f:]+) \((.+)\)')

        # creating a dynamic list to keep all outputs collected
        active_ips_and_macs = []
        lines = result.stdout.splitlines()

        for i, line in enumerate(lines):
            ip_match = pattern_ip.search(line)
            if ip_match:
                ip = ip_match.group(1)
                mac = None
                vendor = None

                # Look ahead for MAC address information
                if i + 1 < len(lines):
                    mac_match = pattern_mac.search(lines[i + 1])
                    if mac_match:
                        mac = mac_match.group(1)
                        vendor = mac_match.group(2)

                active_ips_and_macs.append((ip, mac, vendor))

        # Print the results
        print("Active IPs and MACs found:")
        for ip, mac, vendor in active_ips_and_macs:
            print(f"IP: {ip}, MAC: {mac}, Vendor: {vendor}")

        return active_ips_and_macs

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def load_existing_entries(file_path):
    """Load existing IP-MAC pairs from the file if it exists."""
    if not os.path.exists(file_path):
        return set()

    with open(file_path, "r") as file:
        return set(file.read().splitlines())


def save_new_entries(file_path, entries):
    """Save new IP-MAC pairs to the file."""
    with open(file_path, "a") as file:
        for ip, mac, vendor in entries:
            file.write(f"{ip} - {mac or 'Unknown'} - {vendor or 'Unknown'}\n")


if __name__ == "__main__":
    # Define the subnet to scan
    subnet_ip = "172.16.3.0/24"
    file_path = "active_ips_and_macs.txt"

    # Load existing entries
    existing_entries = load_existing_entries(file_path)
    print(f"Existing entries in file: {existing_entries}")

    # Scan for active IPs and MACs
    active_ips_and_macs = scan_active_ips_and_macs(subnet_ip)

    # Format new entries as strings for comparison
    formatted_entries = {f"{ip} - {mac or 'Unknown'} - {vendor or 'Unknown'}" for ip, mac, vendor in
                         active_ips_and_macs}

    # Determine new entries to add
    new_entries = formatted_entries - existing_entries
    if new_entries:
        print("New entries to add:")
        for entry in new_entries:
            print(entry)

        # Save new entries to file
        save_new_entries(file_path, [entry.split(' - ') for entry in new_entries])
        print("New entries have been saved to the file.")
    else:
        print("No new entries found.")
