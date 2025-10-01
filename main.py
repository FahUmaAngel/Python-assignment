# main.py

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Start monitoring")  #storage data CPU, RAM, Disk
        print("2. List monitoring") # show current CPU, RAM, Disk usage
        print("3. Create alarm")    # create alarm for CPU, RAM, Disk usage
        print("4. Show alarms")     # list all alarms
        print("5. Start monitoring mode") # continuously monitor and trigger alarms
        print("6. Remove alarm")    # remove an existing alarm
        print("7. Exit program")   # exit the program
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            print("Starting monitoring")    # TODO: Add monitoring logic here
        elif choice == '2':
            print("List monitoring")        # TODO: Add listing current monitoring data here
        elif choice == '3':
            print("Create alarm")            # TODO: Add create alarm logic here
        elif choice == '4':
            print("Show alarms")            # TODO: Add show alarms logic here
        elif choice == '5':
            print("Start monitoring mode")   # TODO: Add continue monitoring logic here
        elif choice == '6':
            print("Remove alarm")            # TODO: Add remove alarm logic here
        elif choice == '7':
            print("Exiting program.")   
            break
        else:
            print("Invalid choice. Please try again.")  # End of while loop

if __name__ == "__main__":
    main_menu()
# Note: The actual monitoring, alarm creation, listing, and removal logic needs to be implemented.
