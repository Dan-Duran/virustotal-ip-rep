import sys
import os
from includes.single_ip import display_ip_info
from includes.single_domain import display_domain_info
from includes.ip_domain_list import process_ip_or_domain_list

# Ensure the output directories exist
def ensure_directories():
    os.makedirs('output/single-ip', exist_ok=True)
    os.makedirs('output/single-domain', exist_ok=True)
    os.makedirs('output/domain-ip-lists', exist_ok=True)

def main():
    ensure_directories()
    
    while True:
        print("\n----------------")
        print("MENU")
        print("1. Single IP Address: All info of a single IP")
        print("2. Single Domain: All info of a single domain")
        print("3. IP/Domain List: reputation score, country, Stats for each IP/Domain in the list")
        print("4. Exit")
        print("----------------\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            ip = input("Enter IP address: ")
            display_ip_info(ip)
        elif choice == "2":
            domain = input("Enter domain: ")
            display_domain_info(domain)
        elif choice == "3":
            file_path = input("Type the input file (Example: input.txt): ")
            process_ip_or_domain_list(file_path)
        elif choice == "4":
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
