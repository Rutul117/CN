import socket

def dns_lookup(input_value):
    try:
        ip_address = socket.gethostbyname(input_value)
        result_type = "IP Address"
    except socket.herror:
        host_name, _, ip_addresses = socket.gethostbyaddr(input_value)
        ip_address = ip_addresses[0]
        result_type = "Domain Name"

    print(f"Input: {input_value}\nType: {result_type}\nResult: {ip_address}")

if __name__ == "__main__":
    user_input = input("Enter an IP address or a domain name: ")
    dns_lookup(user_input)
