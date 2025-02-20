import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print("Interface Status")
print("="*80)
print("DN                                                 Description           Speed    MTU")
print("-"*80)

for interface in data.get("interfaces", []):
    dn = interface.get("dn", "N/A")
    description = interface.get("description", "N/A")
    speed = interface.get("speed", "N/A")
    mtu = interface.get("mtu", "N/A")
    
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")