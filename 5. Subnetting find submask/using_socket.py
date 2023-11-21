import socket

def calculate_subnet(ip_address):
    try:
        ip_parts = list(map(int, ip_address.split(".")))
        check_class = ip_parts[0]

        if 0 < check_class <= 127:
            mask = "255.0.0.0"
            print("Class A IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 128 <= check_class <= 191:
            mask = "255.255.0.0"
            print("Class B IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 192 <= check_class <= 223:
            mask = "255.255.255.0"
            print("Class C IP Address")
            print("SUBNET MASK:\n" + mask)
        elif 224 <= check_class <= 239:
            mask = "255.0.0.0"
            print("Class D IP Address Used for multicasting")
        elif 240 <= check_class <= 254:
            mask = "255.0.0.0"
            print("Class E IP Address Experimental Use")

        network_addr = ".".join(map(str, ip_parts[:3] + [0]))
        last_addr = ".".join(map(str, ip_parts[:3] + [255]))

        print("Network Address:", network_addr)
        print("Last Address:", last_addr)

    except ValueError:
        print("Invalid IP address format")

if __name__ == "__main__":
    ip_address = input("ENTER IP: ")
    calculate_subnet(ip_address)


# output

# ENTER IP: 192.168.10.1
# Class C IP Address
# SUBNET MASK:
# 255.255.255.0
# Network Address: 192.168.10.0
# Last Address: 192.168.10.255