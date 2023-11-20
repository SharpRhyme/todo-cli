import pandas as pd

print("Welcome to the CLI todo list")

while True:
    command = input("""
          a - add todo
          d - delete todo
          v - view todo
          c - mark todo as checked
          q - quit
          
          Enter Command: """)
    
    if command == "a":
        df = pd.read_csv("todo.csv")
        
        chore = input("\nEnter new thing to do: ")
        df.loc[-1, "To Do"] = chore
        df.loc[-1, "Done?"] = "No"
        df.to_csv("todo.csv", index=False)
                
        print(f"\n{chore} was added to your list")
        
    elif command == "d":
        df = pd.read_csv("todo.csv")
        print(df.to_string())
        
        delete = input("\nEnter index of item to delete: ")
        
        try:
            delete = int(delete)
        except ValueError:
            print("Not an integer")

        df = df.drop(delete)

        df.to_csv("todo.csv", index=False)

    elif command == "v":
        df = pd.read_csv("todo.csv")
        print(df.to_string())
        
    elif command == "c":
        df = pd.read_csv("todo.csv")
        print(df.to_string())

        check = input("\nEnter index of item to mark done: ")

        try:
            check = int(check)
        except ValueError:
            print("Not an integer")
        df.loc[check, "Done?"] = "Yes"

        df.to_csv("todo.csv", index=False)

    elif command == "q":
        df.to_csv("todo.csv", index=False)
        break
    else:
        print("\nInvalid Command")
        
        
