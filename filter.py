import json

file_path = "gen7randombattle.json"
with open(file_path, "r") as file:
    data = json.load(file)

berry_items = []

z_crystals = [
    "Buginium Z", "Darkinium Z", "Dragonium Z", "Electrium Z", "Fairium Z",
    "Fightinium Z", "Firium Z", "Flyinium Z", "Ghostium Z", "Grassium Z",
    "Groundium Z", "Icium Z", "Normalium Z", "Poisonium Z", "Psychium Z",
    "Rockium Z", "Steelium Z", "Waterium Z", "Decidium Z", "Eevium Z",
    "Kommonium Z", "Lunalium Z", "Lycanium Z", "Marshadium Z", "Mewnium Z",
    "Pikanium Z", "Pikashunium Z", "Primarium Z", "Snorlium Z", "Solganium Z",
    "Tapunium Z", "Ultranecrozium Z"
]

def only_berries_or_z_crystals(items):
    return all(item in berry_items or item in z_crystals for item in items)

filtered_data = {}

for mon, details in data.items():
    filtered_roles = {
        role: role_data for role, role_data in details.get("roles", {}).items()
        if not only_berries_or_z_crystals(role_data.get("items", []))
    }

    new_items = [item for item in details.get("items", []) if item not in berry_items and item not in z_crystals]

    if filtered_roles or new_items:
        filtered_data[mon] = {**details, "items": new_items, "roles": filtered_roles}

output_path = "filtered_gen7randombattle.json"

with open(output_path, "w") as output_file:
    json.dump(filtered_data, output_file, indent=4)