from scapy.all import ARP, Ether, srp, conf
from colorama import init, Fore, Style
from tabulate import tabulate

init()

# Set Scapy to use Npcap for Windows

conf.iface = "Wi-Fi"  # or Ethernet
conf.use_pcap = True


def scan_network(ip_range, timevalue):
    # First Create a ARP Request packet

    arp = ARP(pdst=ip_range)
    # pdst - Protocol Destination : This is the destination IP address or range that the ARP request is querying.

    # Create an Ethernet frame to encapsulate the ARP packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Now Combine the Ethernet frame and ARP packet
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=int(timevalue), verbose=False)[0]
    # srp :- Send and Receive Packets at Layer 2 (Data Link Layer).
    # verbose=False : Disables detailed logging of the process.
    # [0]: Accesses the first part of the result, which contains the responses from the devices that received the ARP packet.

    # List to store discovered devices
    devices = []
    for sent, received in result:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})

    return devices
    # - devices = [] : Initializes an empty list to store information about discovered devices.
    # - for sent, received in result:: Iterates through the results of the ARP request. Each result contains a sent packet and a received response.
    # - devices.append({'ip': received.psrc, 'mac': received.hwsrc}): Adds a dictionary to the devices list containing the IP address (received.psrc) and MAC address (received.hwsrc) of each device found.


def colorize_table(table_str):
    # Split the table into lines
    lines = table_str.split("\n")

    header_color = Fore.CYAN + Style.BRIGHT

    row_color = Fore.GREEN

    border_color = Fore.MAGENTA

    colored_lines = [header_color + lines[0] + Style.RESET_ALL]
    colored_lines.append(header_color + lines[1] + Style.RESET_ALL)

    for line in lines[2:]:
        if any(border in line for border in ["=", "┼", "╭", "╮", "╰", "╯"]):
            colored_lines.append(border_color + line + Style.RESET_ALL)
        else:
            colored_lines.append(row_color + line + Style.RESET_ALL)

    return "\n".join(colored_lines)


def display_devices(devices):
    print(Fore.CYAN + "----------------------------------------" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "          Discovered Devices:" + Style.RESET_ALL)
    print(Fore.CYAN + "----------------------------------------" + Style.RESET_ALL)

    # If there are devices found, print them in a table
    if devices:
        table = tabulate(devices, headers="keys", tablefmt="fancy_grid")
        colored_table = colorize_table(table)
        print(colored_table)
    else:
        print(Fore.RED + "No devices found." + Style.RESET_ALL)


if __name__ == "__main__":
    # Get IP range input
    ip_range = input(
        Fore.BLUE
        + Style.BRIGHT
        + "Enter IP Address Range (ex. 192.168.0.0/24): "
        + Style.RESET_ALL
    )

    timevalue = input(
        Fore.BLUE
        + Style.BRIGHT
        + "Enter Scanning Time in Seconds (ex. 1, 2, 3 - Recommend: 5): "
        + Style.RESET_ALL
    )

    devices = scan_network(ip_range, timevalue)

    display_devices(devices)
