import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
interfaces = data.get("imdata", [])
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':15} {'Speed':10} {'MTU':10}")
print("-" * 80)


for item in interfaces:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn_value = attributes.get("dn", "N/A")
    description = attributes.get("name", "").strip()  
    speed = attributes.get("speed", "inherit")  
    mtu = attributes.get("mtu", "9150")  

    print(f"{dn_value:50} {description:15} {speed:10} {mtu:10}")