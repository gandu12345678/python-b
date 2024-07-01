tasks = []

def add_task():
    task=input("enter a new task:  ")
    tasks.append(task)
    print("task added sucessfully.")
    
def view_task():
    if len(tasks)==0:
        print("no tasks")
    else:
        print("List of tasks:\n")
        for i,task in enumerate(tasks):
            print(f"{i+1}>{task}")

def delete_task():
    if len(tasks)==0:
        print("no tasks to delete")
    else:
        print("tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}>{tasks}")
        choice=int(input("enter the task number to delete: "))
        
        if 0<choice<=len(tasks):
            del tasks[choice-1]
            print("task deleted successfully")
        else:
            print("invalid task number")
            
def main():
    while True:
        print("\n=== To-do list ===")
        print("1> add tasks")
        print("2> view tasks")
        print("3> delete tasks")
        print("4> quit")
        
        choice=int(input("enter your choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("thank you for operating this to_do list")
            break
        else:
            print("invalid choice.please try again")        
        
if __name__ =="__main__":
    main()
    
