import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
interfaces = data.get("imdata", [])
print("Interface Status")
print("=" * 30)
print("DN")
print("-" * 30)
for item in interfaces:
    dn_value = item.get("l1PhysIf", {}).get("attributes", {}).get("dn", "N/A")
    print(dn_value)