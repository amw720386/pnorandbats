import openpyxl
import json

file_path = "filtered_gen7randombattle.json"
with open(file_path, "r") as file:
    data = json.load(file)

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.append(["POKEMON NAME"])
sheet.append(["POSSIBLE ABILITIES"])
sheet.append([])  

for mon in data:
    sheet.append([mon])

    abilities = ", ".join(data[mon].get("abilities", [])) if data[mon].get("abilities") else "None"

    sheet.append([abilities])

    if "roles" in data[mon]:
        roles = data[mon]["roles"]

        role_names = list(roles.keys())
        role_items = [", ".join(roles[role].get("items", [])) if roles[role].get("items") else "None" for role in roles]

        sheet.append(role_names)

        sheet.append(role_items)

        max_moves = max(len(roles[role]["moves"]) for role in roles) if roles else 0

        for i in range(max_moves):
            row = []
            for role in role_names:
                moves = roles[role]["moves"]
                row.append(moves[i] if i < len(moves) else "")  
            sheet.append(row)

    sheet.append([])

workbook.save("PNOrandbats.xlsx")
