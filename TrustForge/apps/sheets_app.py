import json

def update_sheet():
    record = {
        "client": "Rahul",
        "stage": "Meeting Scheduled"
    }

    with open("data/sheets.json", "r+") as f:
        data = json.load(f)
        data.append(record)
        f.seek(0)
        json.dump(data, f, indent=2)

    print("📊 Sheets App: Onboarding sheet updated and saved")
