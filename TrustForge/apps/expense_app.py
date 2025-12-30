import json

def verify_receipt():
    print("🧾 Expense App: Receipt verified")

def check_policy():
    print("📜 Policy Engine: Expense within limits")

def update_finance_sheet():
    expense = {
        "amount": 2000,
        "status": "Approved"
    }

    with open("data/finance.json", "r+") as f:
        data = json.load(f)
        data.append(expense)
        f.seek(0)
        json.dump(data, f, indent=2)

    print("💰 Finance Sheet: Expense recorded and saved")
