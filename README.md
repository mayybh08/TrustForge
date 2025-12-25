# TrustForge: Where Agentic AI Meets On-Chain Integrity

---

## Overview
A **Universal AI Agent** that understands natural language commands and automatically executes complex, multi-app workflows without human intervention.

###  Key Features

- **Natural Language Processing** - Describe tasks in plain English
- **Multi-App Orchestration** - Seamlessly integrates Gmail, Calendar, Sheets, CRM, and more
- **Intelligent Workflow Planning** - Breaks down complex tasks into sequential steps
- **Self-Correcting AI Agent** - Detects errors and retries failed steps automatically
- **Audit Trail** - Complete logging of all actions with blockchain-ready hash generation
- **Time Efficiency** - Reduces 20-40 minute tasks to under 1 minute

---
## Problem
Enterprise workflows require constant app-switching:

- Manually juggling Email, Calendar, Sheets, CRM, Ticketing tools
- **Time-consuming**: Average 20-40 minutes per task
- **Error-prone**: High risk during manual data transfer
- **Fragmented**: No single system for end-to-end automation

**Result:** Massive productivity loss and operational inefficiency

---
## Solution
Our agent provides **one-command automation**:

User: "Onboard new client Rahul and schedule a call"

Agent Executes:
1. Create CRM entry ✓
2. Update onboarding spreadsheet ✓
3. Schedule calendar meeting ✓
4. Send confirmation email ✓
5. Generate audit hash ✓

Time: < 1 minute (vs 30 minutes manual)

---
## Architecture Flow
Natural Language Input → Intent Detection → Workflow Planning (MCP) 
→ App Orchestration → Sequential Execution → Audit Logging

---
## Tech Stack
**Backend:** Node.js, Express  
**AI/NLP:** Claude API (Anthropic), MCP (Model Context Protocol)  
**Frontend:** React (Web UI) / Commander.js (CLI)  
**Integrations (Mock):** Gmail API, Google Calendar, Sheets, CRM  
**Logging:** Winston, Simulated Blockchain Audit

---
## Supported Workflows

### 1. Client Onboarding
Apps Used: CRM, Sheets, Calendar, Email

### 2. Expense Approval
Apps Used: Receipt Verification, Policy Engine, Finance Sheet, Email

### 3. Customer Support Resolution
Apps Used: Ticket System, Order Database, Email

---
## Installation & Setup

### 1. Git Clone https://github.com/mayybh08/TrustForge

### 2. pip install -r requirements.txt

### 3. cd TrustForge

### 4. npm start , npm run cli 

---
## Example Commands 
### 1. Onboard new client Rahul and schedule a call
### 2. Approve travel expense of 2000 rupees
### 3. Resolve refund ticket for order 123

**Output:** Step-by-step execution display with real-time status updates


---
## Team

- **Project Lead** - Mayuri Bhaladhare
- **AI/ML Engineer** - Khushi Meshram
- **Backend Developer** - Purva Khandare
- **Frontend Developer** - Amruta Bedre



