from modules.task_manager import *


print("A1 Active")
while True:
    
    
    command = input("A1 >")
    
    parts = command.split()

    if len(parts) == 0:
        continue

    if parts[0] == "show":
        show_tasks()
    
    elif parts[0] == "add":
          if(len(parts) == 1):
              title=input("Enter title:")   
          else:
              title=" ".join(parts[1:]) 
          add_task(title)  
          print("task added")

    elif parts[0] == "complete":
        if len(parts) == 1:
          ID=int(input("Enter task ID:"))
        else:
          ID=int(parts[1])    
        complete_task(ID) 
        print("task completed") 
        
    elif parts[0] == "delete":
        if len(parts) == 1:
            ID=int(input("Enter task ID"))
        else:
            ID=int(parts[1])   
        delete_task(ID)
        print("task dleted")
    
    elif parts[0] == "exit":
        print("A1 Terminated")
        break 

    elif parts[0] == "help":
        print("""commands:
              show
              add
              delete
              complete
              help
              exit""")
    else:
        print("unkown command. Try help :)")    
                   
