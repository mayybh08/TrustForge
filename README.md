# TrustForge: Agentic Workflow Execution with Audit-Ready Integrity

---

## Overview
TrustForge is an early-stage prototype demonstrating how agentic AI workflows can interpret natural language commands and execute multi-step system actions with transparent logging and audit readiness.

This project is built as a Round-1 functional prototype, focusing on execution logic, workflow planning, and traceability rather than full production integrations.

###  Key Features

- **Natural Language Commands** – Simple English instructions
- **Multi-Step Agentic Execution** – Commands broken into sequential steps
- **Command Execution Engine** – Executes system-level or mocked service actions
- **Self-Recovery Logic** – Retries failed steps automatically
- **Audit-Ready Logging** – Generates execution hashes for traceability
- **Fast Automation** – Demonstrates reduction of manual effort
---
## Problem
Modern automation workflows suffer from:

- Manual coordination across multiple tools
- High execution time (20–40 minutes per task)
- Error-prone handoffs between systems
- Lack of transparent execution records

**Result**: Low productivity and limited trust in automation systems.

---
## Solution
TrustForge demonstrates one-command workflow execution using an agentic approach.

Example Input:

Onboard new client Rahul and schedule a call

**Agent Execution Flow**:
- Parse intent
- Plan workflow steps
- Execute commands sequentially
- Retry on failure
- Generate audit log hash
### **Execution Time**: < 1 minute (prototype simulation)
---
## Architecture Flow
Natural Language Input
→ Intent Detection
→ Workflow Planning
→ Step-by-Step Execution
→ Logging & Audit Hash Generation

This architecture aligns with multi-step agentic workflow principles and is designed to be extended using platforms like Weilliptic SDK and Icarus in future stages.

---
## Tech Stack
- **Backend**: Node.js
- **Agent Logic**: Rule-based + command execution
- **Interface**: CLI-based execution
- **Integrations**: Mocked services (for demo purposes)
- **Logging**: Structured logs + simulated on-chain hash

**Note**: External services and blockchain components are intentionally mocked for Round-1 evaluation.

---
## Supported Workflows
- Client onboarding (simulated)
- Expense approval (simulated)
- Support ticket resolution (simulated)
---
## Installation & Setup
- git clone https://github.com/mayybh08/TrustForge
- cd TrustForge
- npm install
- npm run cli

---
## Example Commands 
1. Onboard new client Rahul and schedule a call
2. Approve travel expense of 2000 rupees
3. Resolve refund ticket for order 123
- **Output**:Step-by-step execution logs with success/failure status and audit hash.
---
## Hackathon Context:
**This repository represents a Round-1 prototype submission demonstrating:**

- Agentic workflow execution
- Sequential command orchestration
- Auditability foundations

**Planned Enhancements (Next Rounds):**

- Weilliptic SDK integration
- Deployment on Icarus
- On-chain verification
- Real API integrations
---
## Team

- **Project Lead** - Mayuri Bhaladhare
- **AI/ML Engineer** - Khushi Meshram
- **Backend Developer** - Purva Khandare
- **Frontend Developer** - Amruta Bedre



