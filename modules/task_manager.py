import json

def load_data():
    with open("data/tasks.json","r") as file:
        data = json.load(file)

    return data

def save_tasks(data):
    with open("data/tasks.json","w") as file:
        json.dump(data,file,indent=4)


def add_task(title):

    if not title:
        print("Title cannot be empty!")
        return
    
    data = load_data() # data => dict
    tasks = data["tasks"]
    
    if(len(tasks) == 0):
        new_id =1
    else:
        new_id=max(task["id"] for task in tasks)+1 

    new_task = {
        "id" : new_id,
        "title" : title,
        "status" : "pending"
    }

    tasks.append(new_task)
    save_tasks(data)    


def show_tasks(filter=None):

    data = load_data()
    
    tasks = data["tasks"]

    found = False
    if len(tasks) == 0:
        print("no tasks yet!")
        return
    
    if filter is None:
        for task in tasks :
          
          print(
            "\nID:",task["id"],
            "\nTitle:",task["title"],
            "\nStatus:",task["status"]
              )
          print()
        return   
    else:
        for task in tasks:
            if task["status"] == filter:
                found = True
                print(
            "\nID:",task["id"],
            "\nTitle:",task["title"],
            "\nStatus:",task["status"]
              )
                print()
        
        
    if not found :
         print("no",filter,"tasks found!")
    
   

            


def complete_task(ID):
    data = load_data()
    tasks = data["tasks"]
    
    found = False
    for task in tasks:
        if task["id"] == ID:
            task["status"] = "completed"
            found = True
            break
    if not found:
        print("task with ID",ID,"not found!")
        return    
    save_tasks(data)

def delete_task(ID):
    data = load_data()
    tasks = data["tasks"]

    found = False

    for task in tasks:
         if task["id"] == ID:
             tasks.remove(task)
             found = True
             break

    if not found:
        print("task with ID",ID,"not found!")
        return     
    
    save_tasks(data)

    
def show_study_mode():

    data = load_data()
    study_tasks=data.get("study_mode",[])

    if len(study_tasks) == 0:
        print("No study items found!")
        return
    i=1
    print("\nToday's Focus")
    print("-" * 15)

    for task in study_tasks:
       print(f"{i}. {task}")
       i += 1

    print()







    