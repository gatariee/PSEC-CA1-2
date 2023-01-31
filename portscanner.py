import nmap
import os
from colorama import Fore
from terminaltables import SingleTable
from ping3 import ping
class Scanner:
    """
    This class is used to scan a list of hosts using nmap.

    Args:
        targets (str): A string of hosts to scan. (e.g "localhost scanme.nmap.org")
        options (str): A string of nmap options to use. (e.g "-sU -sT --top-ports 10 -sV -sC --traceroute -O")
    """

    def __init__(self, targets: str, options: str):
        self.targets = targets
        self.options = options

    def clean_results(self, initial_scan: nmap.PortScanner) -> list:
        """
        Cleans the results of the initial scan into a format that is easier to work with

        Args:
            initial_scan (nmap.PortScanner): The initial scan results.

        Returns:
            list: A list of dictionaries containing the results of the scan
        """
        results = []
        for host in initial_scan.all_hosts():
            host_dict = {
                "host": host,
                "hostname": initial_scan[host].hostname(),
                "protocol": initial_scan[host].all_protocols(),
            }
            for protocol in host_dict['protocol']:
                host_dict[protocol] = {}
                for port in initial_scan[host][protocol].keys():
                    host_dict[protocol][port] = {
                        "port": port, 
                        "state": initial_scan[host][protocol][port]['state'], 
                        "product": initial_scan[host][protocol][port]['product'], 
                        "extrainfo": initial_scan[host][protocol][port]['extrainfo'], 
                        "reason": initial_scan[host][protocol][port]['reason'], 
                        "cpe": initial_scan[host][protocol][port]['cpe']
                        }
            results.append(host_dict)
        return results

    def perform_scan(self) -> list:
        """
        This function performs the port scan

        Returns:
            list: The results of the scan after being cleaned
        """
        nm = nmap.PortScanner()
        print(f"Type of nmScan: {type(nm)}")
        print(f"Scanning hosts: {self.scan_targets}")
        print("Beginning scan...")
        initial_result = nm.scan(hosts = self.scan_targets, arguments = self.options)
        print(f"Type of results: {type(initial_result)}")
        print(f"Scanning options used: {self.options}")
        scan_results = self.clean_results(initial_scan=nm)
        return scan_results

    def generate_table(self, scan_results: list) -> None:
        """
        Generates and prints a table of the scan results

        Args:
            scan_results (list): A table containing the results of the scan
        """
        table_data = [
            ['Host', 'Hostname', 'Protocol', 'Port ID', 'State', 'Product', 'Extra Info', 'Reason', 'CPE']
        ]
        for host in scan_results:
            for protocol in host['protocol']:
                for port in host[protocol].keys():
                    table_data.append
                    (
                        [
                        host['host'],
                        host['hostname'],
                        protocol,
                        host[protocol][port]['port'],
                        host[protocol][port]['state'],
                        host[protocol][port]['product'],
                        host[protocol][port]['extrainfo'][:12 if len(host[protocol][port]['extrainfo']) > 20 else len(host[protocol][port]['extrainfo'])],
                        host[protocol][port]['reason'],
                        host[protocol][port]['cpe'][7:]
                    ]
                )
        TABLE: SingleTable = SingleTable(table_data)
        TABLE.inner_row_border = 1
        for row in TABLE.table_data:
            if row[4] == 'open':
                row[4] = Fore.GREEN + row[4] + Fore.RESET
            elif row[4] == 'closed':
                row[4] = Fore.RED + row[4] + Fore.RESET
            elif row[4] == 'filtered':
                row[4] = Fore.YELLOW + row[4] + Fore.RESET
            elif row[4] == 'open|filtered':
                row[4] = Fore.CYAN + row[4] + Fore.RESET
        print(TABLE.table)

    def is_alive(self) -> bool:
        """
        Checks if the hosts are alive.

        Returns:
            bool: If at least one host is alive, returns True. Otherwise, returns False.
        """
        alive = ""
        table_data = [
            ['Host', 'Status']
        ]
        for host in self.targets.split(' '):
            response = ping(host, timeout=1)
            if(response is not None and response is not False):
                alive = alive + host + " "
                table_data.append([host,Fore.GREEN + "Alive" + Fore.RESET])
            else:
                table_data.append([host,Fore.RED + "Dead" + Fore.RESET])
        TABLE: SingleTable = SingleTable(table_data)
        print(TABLE.table)
        if(len(alive) == 0):
            return False
        else:
            self.scan_targets = alive
            return True
    def run(self):
        """
        Starts the scan
        """
        print("Checking status of hosts...")
        live_hosts = self.is_alive()
        if(live_hosts is True):
            scan_results = self.perform_scan()
            # with open('results.txt', 'w') as f:
            #     f.write(str(scan_results))
            # generate sample test results
            # with open('results.txt', 'r') as f:
            #     scan_results = f.read()
            self.generate_table(scan_results)
        else:
            print("Host is either dead or blocking ICMP packets.")
            input("Press enter to continue...")
            os.system('cls')
