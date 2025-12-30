def get_workflow(intent):
    if intent == "client_onboarding":
        return [
            "create_crm_entry",
            "update_sheet",
            "schedule_meeting",
            "send_email",
            "audit_log"
        ]

    if intent == "expense_approval":
        return [
            "verify_receipt",
            "check_policy",
            "update_finance_sheet",
            "send_email",
            "audit_log"
        ]

    if intent == "customer_support":
        return [
            "fetch_ticket",
            "fetch_order",
            "resolve_ticket",
            "send_email",
            "audit_log"
        ]

    return []
