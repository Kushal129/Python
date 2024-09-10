import ipaddress
from colorama import Fore, Style, init

# Initialize colorama for color formatting on all platforms
init(autoreset=True)


def calculate_cidr(subnet_mask):
    return sum([bin(int(x)).count("1") for x in subnet_mask.split(".")])


def determine_ip_range(ip_address, subnet_mask):
    cidr = calculate_cidr(subnet_mask)
    network = ipaddress.IPv4Network(f"{ip_address}/{cidr}", strict=False)
    return network


def show_intro():
    print(Fore.CYAN + Style.BRIGHT + " ")
    print("----------------------------------------------------------------------")
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "                 Welcome to the IP Range Calculator!\n"
    )
    print(
        Fore.WHITE
        + "This tool will help you calculate the network IP range based on your\nIP Address and Subnet Mask."
    )
    print("----------------------------------------------------------------------")
    print(Fore.GREEN + Style.BRIGHT + "To identify your IP Address and Subnet Mask:")
    print(Fore.CYAN + " - On Windows: Open CMD Prompt, run 'ipconfig'.")
    print(Fore.CYAN + " - On macOS/Linux: Open Terminal, run 'ifconfig' or 'ip addr'.")
    print("----------------------------------------------------------------------")
    print(Fore.MAGENTA + Style.BRIGHT + "Example of network details you can enter:")
    print(Fore.MAGENTA + "IPv4 Address: 192.168.0.106")
    print(Fore.MAGENTA + "Subnet Mask: 255.255.255.0")
    print("----------------------------------------------------------------------")


def get_user_input():
    print(Fore.BLUE + Style.BRIGHT + "\nPlease enter your network details.")
    ip_address = input(Fore.CYAN + "IPv4 Address: ")
    subnet_mask = input(Fore.CYAN + "Subnet Mask: ")
    return ip_address, subnet_mask


def display_ip_range(network):
    print(Fore.BLUE + f"=====================================================")
    print(Fore.YELLOW + Style.BRIGHT + "            Network Details:")
    print(Fore.BLUE + f"=====================================================")
    print(Fore.GREEN + f"Network Address   : {network.network_address}")
    print(Fore.GREEN + f"Broadcast Address : {network.broadcast_address}")
    print(
        Fore.GREEN
        + f"Usable IP Range   : {network.network_address + 1} to {network.broadcast_address - 1}"
    )
    print(Fore.GREEN + f"Total Hosts       : {network.num_addresses - 2}")
    print(Fore.GREEN + f"CIDR Notation     : {network.with_prefixlen}\n")


if __name__ == "__main__":
    show_intro()

    ip_address, subnet_mask = get_user_input()

    network = determine_ip_range(ip_address, subnet_mask)

    display_ip_range(network)
