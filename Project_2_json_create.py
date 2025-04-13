import json

tasks = [
        {
            
            "title": "Task 1",
            "description": "Complete task 1 by tomorrow",
            "due date": "05/9/2023",
            "status": "in progress"
        },
        {
            
            "title": "Task 2",
            "description": "Submit report by end of the week",
            "due date": "05/10/2023",
            "status": "incomplete"
        },
        {
            
            "title": "Task 3",
            "description": "Call client for follow-up",
            "due date": "05/11/2023",
            "status": "completed"
        }
        ]

file = open ("Project_2_json.json","w")   # write data
json.dump(tasks,file,indent=2)
file.close()