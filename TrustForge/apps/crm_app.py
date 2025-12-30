import json

def create_crm_entry():
    client = {
        "name": "Rahul",
        "status": "Onboarded"
    }

    with open("data/crm.json", "r+") as f:
        data = json.load(f)
        data.append(client)
        f.seek(0)
        json.dump(data, f, indent=2)

    print("📇 CRM App: Client entry created and saved")
