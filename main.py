user_input = ""
started = False
while True:
    user_input = input("> ").lower()
    if user_input == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started.....Ready to go\n")
    elif user_input == "stop":
        if not started:
            print("The car has already stopped")
        else:
            started = False
            print("Car stopped")
    elif user_input == "quit":
        break
    elif user_input == "help":
        print("start-To start the car.\nstop-To stop the car.\nquit-To exit program")
    else:
        print("i don't understand that")
