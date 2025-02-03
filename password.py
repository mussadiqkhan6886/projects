def view():
    with open("password.txt", "r") as file:
        for l in file.readlines():
            l = l.rstrip()
            user, passw = l.split("|")
            print(f"User: {user}, password: {passw}") 

def add():
    add_pass = input()
    with open("password.txt", "a") as file:
        file.write(add_pass + "\n")

while True:
    mode = input("You wanna add password or view or q for quit:")
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Error in mode")
        