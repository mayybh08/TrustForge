from agent.orchestrator import run_agent

if __name__ == "__main__":
    print("=== Universal Multi-App Task Orchestration Agent ===")
    task = input("Enter task command: ")
    run_agent(task)
