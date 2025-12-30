import hashlib
import time

def log_audit():
    data = str(time.time())
    audit_hash = hashlib.sha256(data.encode()).hexdigest()
    print("🔐 Audit Log Hash:", audit_hash)
