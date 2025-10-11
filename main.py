# main.py
import threading  # import module for create and manage threads, can work many threads in one precess
import os         # to work with OS, can manage Path or folder.

ALARM_FILE = os.path.join('data', 'alarms.json')  # Path to store alarms

class MonitoringApp:
    def __init__(self):
        self.monitoring_enabled = False  # Flag to indicate if monitoring is active
        self.alarms = []                 # List to store alarms
        self.logger = AppLogger()        # Logger instance for logging events
        
        # last triggered keep track which threshold was last truggered for each metric
        self.last_triggered = {'cpu': None, 'memory': None, 'disk': None}
        
        self._load_alarms_on_start()      # Load existing alarms from file
        
    def _load_alarms_on_start(self):
        if os.path.exists(ALARM_FILE):
            print("Loading previously configured alarms...")
            self.alarms = load_alarms(ALARM_FILE)
            self.logger.log("Loading_previously_configured_alarms")
        else:
            self.alarms = []
    
    def save_alarms(self):
        save_alarms(ALARM_FILE, self.alarms)
        self.logger.log("Alarms_saved_to_file")

# Main menu function
def start(self):
    #main menu loop
    while True:
        print("\n=== Main Menu ===")
        print("1. Start monitoring")  #storage data CPU, RAM, Disk
        print("2. List monitoring") # show current CPU, RAM, Disk usage
        print("3. Create alarm")    # create alarm for CPU, RAM, Disk usage
        print("4. Show alarms")     # list all alarms
        print("5. Start monitoring mode") # continuously monitor and trigger alarms
        print("6. Remove alarm")    # remove an existing alarm
        print("7. Exit program")   # exit the program
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            self._start_monitoring_flag()    # TODO: Add monitoring logic here, def _start_monitoring_flag(self):
        elif choice == '2':
            self._list_active_monitoring()   # TODO: Add listing current monitoring data here, def _list_active_monitoring(self):
        elif choice == '3':
            self._create_alarm_menu()        # TODO: Add create alarm logic here, def _create_alarm_menu(self):
        elif choice == '4':
            self._show_alarms()              # TODO: Add show alarms logic here, def _show_alarms(self):
        elif choice == '5':
            self._start_monitoring_mode()    # TODO: Add continue monitoring logic here, def _start_monitoring_mode(self):
        elif choice == '6':
            self._remove_alarm()               # TODO: Add remove alarm logic here, def _remove_alarm(self):
        elif choice == '7':
            self._exit_program()              # TODO: Add exit program logic here, def _exit_program(self):   
            break
        else:
            print("Invalid choice. Please try again.")  # End of while loop

# call from choice 1
def _start_monitoring_flag(self):
    self.monitoring_enable = True
    print("Monitoring started.")
    self.logger.log("Started monitoring.")  # safe log to log file
    
    # back to main menu directly
    
# call from choice 2
def _list_active_monitoring(self):
    if not self.monitoring_enabled:
        print("No monitoring is active.")
    else:    # show current CPU, RAM(memory), Disk usage
        cpu = get_cpu_percent()
        mem_p, mem_used, mem_total = get_memory_info()
        disk_p, disk_used, disk_total = get_disk_info()
        
        print(f"\nCPU Usage: {cpu}%")
        print(f"Memory Usage: {mem_p}% ({mem_used} GB out of {mem_total} GB used)")
        print(f"Disk Usage: {disk_p}% ({disk_used} GB out of {disk_total} GB used)")
        
        input("\nPress Enter to return to the main menu")

# call from choice 3
def _create_alarm_menu(self):
    

# call from choice 4
def _show_alarms(self):



# call from choice 5
def _start_monitoring_mode():

# call from choice 6
def _remove_alarm(self):


# call from choice 7
def _exit_program(self):


if __name__ == "__main__":
    app = MonitoringApp()
    app.start()
# Note: The actual monitoring, alarm creation, listing, and removal logic needs to be implemented.
