import socket

def dns_lookup(input_value):
    try:
        # Try to interpret input as an IP address
        ip_address = socket.gethostbyname(input_value)
        print(f"Input: {input_value}\nType: IP Address\nResult: {ip_address}")
    except socket.herror:
        try:
            # Try to interpret input as a domain name
            host_name, _, ip_addresses = socket.gethostbyaddr(input_value)
            print(f"Input: {input_value}\nType: Domain Name\nResult: {host_name}\nIP Address: {ip_addresses}")
        except socket.herror:
            print(f"Unable to perform DNS lookup for input: {input_value}")

if __name__ == "__main__":
    user_input = input("Enter an IP address or a domain name: ")
    dns_lookup(user_input)
