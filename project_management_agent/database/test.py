from project_management_agent.database.database import database_manager

tasks = database_manager.list_tasks()

print(tasks)
print(type(tasks))