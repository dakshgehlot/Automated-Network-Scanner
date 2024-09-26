import subprocess
import re

class AutomatedNetworkScanner:

    # Function to run shell commands
    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            return result.stdout
        except Exception as e:
            return str(e)


    # Function to perform whois
    def whois_scan(self, target):
        print("Running whois...")
        whois_output = self.run_command(f"whois {target}")

        # Extract from "Domain Name" onwards using regex
        match = re.search(r"Domain Name:*", whois_output)

        if match:
            # Extract the portion starting from "Domain Name"
            return whois_output[match.start():]
        else:
            return "No 'Domain Name' section found in the whois data."


    # Function to perform nslookup
    def nslookup_scan(self, target):
        print("Running nslookup...")
        return self.run_command(f"nslookup {target}")


    # Function to run whatweb
    def whatweb_scan(self, target):
        print("Running whatweb...")
        return self.run_command(f"whatweb {target}")


    # Function to perform harvester
    def harvester_scan(self, target):
        print("Running harvester...")
        harvester_output = self.run_command(f"theHarvester -d {target} -l 500 -b yahoo")

        # Extract from "Domain Name" onwards using regex
        match = re.search(r"\[\*\] Target:*", harvester_output)

        if match:
            # Extract the portion starting from "Domain Name"
            return harvester_output[match.start():]
        else:
            return "No 'Domain Name' section found in the whois data."


    # Function to perform nmap host discovery
    def nmap_host_discovery(self, target):
        print("Running nmap host discovery...")
        return self.run_command(f"nmap -PE -sn {target}")


    # Function to perform nmap port scanning
    def nmap_port_scanning(self, target):
        print("Running nmap port scanning...")
        return self.run_command(f"nmap -p 80 {target}")


    # Main function
    def network_scan(self, target):
        print(f"Scanning {target}...\n")

        # Perform all scans
        whois_result = self.whois_scan(target)
        nslookup_result = self.nslookup_scan(target)
        whatweb_result = self.whatweb_scan(target)
        harvester_result = self.harvester_scan(target)
        nmap_host_discovery_result = self.nmap_host_discovery(target)
        nmap_port_scanning_result = self.nmap_port_scanning(target)

        # Print the results
        print("\n\n=================================\n\n")
        print("\nWHOIS Result:\n\n", whois_result)
        print("\n\n=================================\n\n")
        print("\nNSLOOKUP Result:\n\n", nslookup_result)
        print("\n\n=================================\n\n")
        print("\nWHATWEB Result:\n\n", whatweb_result)
        print("\n\n=================================\n\n")
        print("\nHarvester Result:\n\n", harvester_result)
        print("\n\n=================================\n\n")
        print("\nNMap Host Discovery Result:\n\n", nmap_host_discovery_result)
        print("\n\n=================================\n\n")
        print("\nNMap Port Scanning Result:\n\n", nmap_port_scanning_result)
        print("\n\n=================================\n\n")


# Driver code
scanner = AutomatedNetworkScanner()
target = input("\n\nEnter the website to scan: ")
print("\n\n=================================\n\n")
scanner.network_scan(target)