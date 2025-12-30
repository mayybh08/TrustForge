from agent.intent_detector import detect_intent
from agent.workflow_planner import get_workflow

from apps.crm_app import create_crm_entry
from apps.sheets_app import update_sheet
from apps.calendar_app import schedule_meeting
from apps.email_app import send_email

from apps.expense_app import verify_receipt, check_policy, update_finance_sheet
from apps.support_app import fetch_ticket, fetch_order, resolve_ticket

from audit.audit_log import log_audit


def run_agent(task):
    print("\nTask Received:", task)

    intent = detect_intent(task)
    print("Detected Intent:", intent)

    workflow = get_workflow(intent)
    print("Planned Workflow:", workflow)

    if not workflow:
        print("❌ No workflow found for this task")
        return

    for step in workflow:
        if step == "create_crm_entry":
            create_crm_entry()
        elif step == "update_sheet":
            update_sheet()
        elif step == "schedule_meeting":
            schedule_meeting()
        elif step == "verify_receipt":
            verify_receipt()
        elif step == "check_policy":
            check_policy()
        elif step == "update_finance_sheet":
            update_finance_sheet()
        elif step == "fetch_ticket":
            fetch_ticket()
        elif step == "fetch_order":
            fetch_order()
        elif step == "resolve_ticket":
            resolve_ticket()
        elif step == "send_email":
            send_email()
        elif step == "audit_log":
            log_audit()

    print("\n✅ Task Completed Successfully")
