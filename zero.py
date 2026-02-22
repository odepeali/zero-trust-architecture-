# Import module for colored output
from colorama import Fore, Style, init
init(autoreset=True)

class User:
    def __init__(self, name, role, device_compliant):
        self.name = name
        self.role = role
        self.device_compliant = device_compliant

# Define network zones with allowed roles and VLAN IDs
NETWORK_ZONES = {
    "Finance": {"roles": ["CFO", "Accountant"], "vlan": 10},
    "Engineering": {"roles": ["Engineer", "DevOps"], "vlan": 20},
    "HR": {"roles": ["HR_Manager"], "vlan": 30}
}

def access_zone(user, zone):
    print(f"\n{user.name} trying to access {zone} zone (VLAN {NETWORK_ZONES[zone]['vlan']})...")
    
    if not user.device_compliant:
        print(Fore.RED + "ACCESS DENIED: Device non-compliant" + Style.RESET_ALL)
        return
    
    if user.role in NETWORK_ZONES[zone]["roles"]:
        print(Fore.GREEN + f"ACCESS GRANTED → VLAN {NETWORK_ZONES[zone]['vlan']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "ACCESS DENIED: Role not authorized" + Style.RESET_ALL)

# Simulated users
users = [
    User("Alice", "Engineer", True),
    User("Bob", "CFO", True),
    User("Charlie", "HR_Manager", False)
]

# Test access for each user to each zone
for user in users:
    for zone in NETWORK_ZONES.keys():
        access_zone(user, zone)
