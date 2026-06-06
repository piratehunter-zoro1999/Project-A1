from modules.task_manager import *


print("A1 Active")
while True:
    
    
    command = input("A1 >")

    if command == "show":
        show_tasks()

    elif command == "add":
        title=input("Enter title:")  
        add_task(title)

    elif command == "complete":
        ID=int(input("Enter task ID:"))
        complete_task(ID)  
        
    elif command == "delete":
        ID=int(input("Enter task ID"))
        delete_task(ID)
    
    elif command == "exit":
        print("A1 Terminated")
        break 

    elif command == "help":
        print("""commands:
              show
              add
              delete
              complete
              help
              exit""")
    else:
        print("unkown command. Try help :)")    
                   
