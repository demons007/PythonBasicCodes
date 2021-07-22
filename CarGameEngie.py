# Car Game Engine:
# help
# unknown
# start
# stop
# quit
started = False
name = input("Enter the gamer name :: ").upper()
print(f"Welcome gamer {name}")
while True:
    command = input(">> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already Stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
start - to start a car
stop - to stop a car
quit - to exit       
        """)
    elif command == "quit":
        print("exiting the game")
        break
    else:
        print("Unknown input")

