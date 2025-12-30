def detect_intent(task):
    task = task.lower()

    if "onboard" in task:
        return "client_onboarding"
    elif "expense" in task or "reimburse" in task or "approve" in task:
        return "expense_approval"
    elif "refund" in task or "ticket" in task or "support" in task:
        return "customer_support"
    else:
        return "unknown"
