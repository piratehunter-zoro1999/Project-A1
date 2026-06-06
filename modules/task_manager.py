import json

def load_tasks():
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
    
    data = load_tasks() # data => dict
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


def show_tasks():
    data = load_tasks()
    
    tasks = data["tasks"]

    if len(tasks) == 0:
        print("no tasks yet!")
    else:
        for task in tasks :
         print(
            "\nID:",task["id"],
            "\nTitle:",task["title"],
            "\nStatus:",task["status"]
              )
         print()



def complete_task(ID):
    data = load_tasks()
    tasks = data["tasks"]
    
    found = False
    for task in tasks:
        if task["id"] == ID:
            task["status"] = "completed"
            found = True
            break
    if found == False:
        print("task with ID",ID,"not found!")
        return    
    save_tasks(data)

def delete_task(ID):
    data = load_tasks()
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

    





    