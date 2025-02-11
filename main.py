import openpyxl
import json

# Load filtered JSON data
file_path = "filtered_gen7randombattle.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Create an Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add headers
sheet.append(["POKEMON NAME"])
sheet.append(["POSSIBLE ITEMS"])
sheet.append(["POSSIBLE ABILITIES"])
sheet.append([])  # Empty row for spacing

# Iterate through Pokémon
for mon in data:
    # Append Pokémon name
    sheet.append([mon])

    # Extract item and ability data
    items = ", ".join(data[mon].get("items", [])) if data[mon].get("items") else "None"
    abilities = ", ".join(data[mon].get("abilities", [])) if data[mon].get("abilities") else "None"

    # Append possible items and abilities
    sheet.append([items])
    sheet.append([abilities])

    # Process roles and moves
    if "roles" in data[mon]:
        roles = data[mon]["roles"]

        # Extract all role names
        role_names = list(roles.keys())

        # Find the max number of moves across all roles
        max_moves = max(len(roles[role]["moves"]) for role in roles) if roles else 0

        # Create the first row for role names
        sheet.append(role_names)

        # Write moves row-wise
        for i in range(max_moves):
            row = []
            for role in role_names:
                moves = roles[role]["moves"]
                row.append(moves[i] if i < len(moves) else "")  # Fill empty space if fewer moves
            sheet.append(row)

    # Add spacing after each Pokémon
    sheet.append([])

# Save the Excel file
workbook.save("PNOrandbats.xlsx")
