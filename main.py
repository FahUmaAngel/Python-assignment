# main.py
import threading  # import module for create and manage threads, can work many threads in one precess
import os         # to work with OS, can manage Path or folder.

from monitor import get_cpu_percent, get_memory_info, get_disk_info  # import functions from monitor.py
from alarm import Alarm         # import Alarm class
from storage import save_alarms, load_alarms  # import functions to load and save alarms
from logger import AppLogger  # import AppLogger class for logging


ALARM_FILE = os.path.join('data', 'alarms.json')  # Path to store alarms

METRIC_LABEL = {                    # Mapping for metric labels, used to create alarm
    'cpu': 'CPU',
    'memory': 'Memory',
    'disk': 'Disk'
}   


class MonitoringApp:
    def __init__(self):
        self.monitoring_enabled = False  # Flag to indicate if monitoring is active
        self.alarms = []                 # List to store alarms
        self.logger = AppLogger()        # Logger instance for logging events
        
        # last triggered keep track which threshold was last truggered for each metric
        self.last_triggered = {'cpu': None, 'memory': None, 'disk': None}
        
        self._load_alarms_on_start()      # Load existing alarms from file
        
    def _load_alarms_on_start(self):
        if os.path.exists(ALARM_FILE):                              # Check if alarm file exists    
            print("Loading previously configured alarms...")
            self.alarms = load_alarms(ALARM_FILE)                   # Load alarms from file 
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
        # set the correct flag name (monitoring_enabled)
        self.monitoring_enabled = True
        print("Monitoring started.")
        self.logger.log("Started monitoring.")  # safe log activities to log file
    
    # back to main menu directly
    
# call from choice 2
    def _list_active_monitoring(self):
        if not self.monitoring_enabled:
            print("No monitoring is active.")
        else:    # show current CPU, RAM(memory), Disk usage
            cpu = get_cpu_percent()
            mem_per, mem_used, mem_total = get_memory_info()
            disk_per, disk_used, disk_total = get_disk_info()
            
            print(f"CPU Usage: {cpu:.0f}%")
            print(f"Memory Usage: {mem_per}% ({mem_used} GB out of {mem_total} GB used)")
            print(f"Disk Usage: {disk_per}% ({disk_used} GB out of {disk_total} GB used)")
            
            input("\nPress Enter to return to the main menu")

# call from choice 3
    def _create_alarm_menu(self):
        while True:
            print("\n Create Alarm")
            print("1. CPU Usage Alarm")
            print("2. Memory Usage Alarm")
            print("3. Disk Usage Alarm")
            print("4. Back to Main Menu")
            sub_choice = input("Choose an option (1-4): ").strip()
            
            mapping = {'1': 'CPU', '2': 'Memory', '3': 'Disk'}
            
            if sub_choice == '4':
                return
            if sub_choice not in mapping:
                print("Invalid choice. Please try again.")
                continue
            
            score_percent = mapping[sub_choice]
            level = input("Set alarm level (1-100): ").strip()      # ask threshold's level % 'string, threshold: user set value% for set alert, if over this value, alert.

            try:                                            # try ... except = protrect program from error crash
                level_i = int(level)
                if not (0 <= level_i <= 100):
                    raise ValueError
            except ValueError:
                print("Incorrect entry. Please enter a number between 1-100.")
                continue        

    # create alarm
            alarm = Alarm(metric=score_percent.lower(), threshold=level_i)
            self.alarms.append(alarm)                               # add new alarm to list
            self.save_alarms()                                      # save alarms to file

            # log and print using the resolved metric label
            self.logger.log(f"{score_percent}_Usage_Alarm_Configured_at_{level_i}_Percent")
            print(f"{score_percent} usage set to {level_i}%")    # confirm to user alarm was created
            return


    # call from choice 4
    def _show_alarms(self):
        if not self.alarms:
            print("No configured alarms.")
        else:
            sorted_alarms = sorted(self.alarms, key=lambda x: (x.metric, x.threshold))    # sort alarms by metric and threshold
            def format(x):
                label = METRIC_LABEL.get(x.metric, x.metric)                # get metric label or use metric if not found
                return f"{label} alarm {x.threshold}%"
            lines = list(map(format, sorted_alarms))                        # format each alarm for display
            print("\n --- Configured Alarms ---")                           # display all alarms
            for line in lines:                                              # print each alarm line
                print(line)
                input("\n Press Enter to return to the main menu")


    # call from choice 5
    def _start_monitoring_mode(self):
        print("Monitoring is active. Press Enter to return to the main menu.")
        self.logger.log("Monitoring_mode_started")                          # log monitoring mode start
        
        stop_event = threading.Event()                                     # create event to signal thread to stop
        monitoring_thread = threading.Thread(target=self._monitoring_loop, args=(stop_event,), daemon=True)   # create monitoring thread
        monitoring_thread.start()                                          # start monitoring thread
        
        # wait for user to press Enter to stop monitoring
        try:
            input()                         # wait for user to press Enter
        except KeyboardInterrupt:
            pass                            # ignore Ctrl+C interrupts
        stop_event.set()                   # signal thread to stop
        monitoring_thread.join()            # wait for thread to finish
        print("Exiting monitoring mode.")
        
    def _monitoring_loop(self, stop_event):      # monitoring loop running in separate thread
        while not stop_event.is_set():           # loop until stop event is set
            cpu = get_cpu_percent()               # get current CPU usage
            mem_per, mem_used, mem_total = get_memory_info()
            disk_per, disk_used, disk_total = get_disk_info()
            
            print("\n --- Current Status ---")
            print(f"CPU Usage: {cpu}%")    # show current CPU usage
            print(f"Memory Usage: {mem_per}% ({mem_used} GB out of {mem_total} GB used)")
            print(f"Disk Usage: {disk_per}% ({disk_used} GB out of {disk_total} GB used)")
            
            # check alarms for each metric
            self._check_alarm_for_metric('cpu', cpu)
            self._check_alarm_for_metric('memory', mem_per)
            self._check_alarm_for_metric('disk', disk_per)
            
            if stop_event.wait(0.5):  # wait 0.5 seconds or until stop event is set
                break
            
    def _check_alarm_for_metric(self, metric, usage_percent):       # check alarms for a specific metric
        thresholds = [a.threshold for a in self.alarms if a.metric == metric]
        if not thresholds:                        # no alarms for this metric
            if self.last_triggered.get(metric) is not None:
                self.last_triggered[metric] = None      # reset last triggered if no alarms
            return
        valid = [t for t in thresholds if t<= usage_percent]  # find thresholds that are exceeded
        triggered = max(valid) if valid else None  # get highest exceeded threshold
        
        if triggered is not None and self.last_triggered.get(metric) != triggered:   # only trigger if different from last
            label = METRIC_LABEL.get(metric, metric).upper()            # get metric label or use metric if not found
            message = f"***ALERT, {label} USAGE EXCEEDS {triggered}%)***"
            print(message)                                             # print alert message
            
            self.logger.log(f"Alarm_Triggered_{label}_{triggered}_Percent")  # log alarm trigger
            self.last_triggered[metric] = triggered                    # update last triggered threshold
        elif triggered is None:                                        # no thresholds exceeded
            self.last_triggered[metric] = None                         # reset last triggered
            
            
            
    # call from choice 6
    def _remove_alarm(self):
        if not self.alarms:
            print("No alarms to remove.")
            return
        sorted_alarms = sorted(self.alarms, key=lambda x: (x.metric, x.threshold))
        print("\n Select an alarm to remove:")
        for index, a in enumerate(sorted_alarms, start=1):          # order alarm -> CPU, Memory, Disk
            label = METRIC_LABEL.get(a.metric, a.metric)            # get metric label or use metric if not found
            print(f"{index}.{label} Alarm {a.threshold}%")          # print each alarm with index
        select_remove = input("Choose an alarm to remove (or empty to cancel): ").strip()
        if select_remove == '':
            print("Alarm removal cancelled.")
            return
        
        try:
            select_i = int(select_remove)
            if not (1 <= select_i <= len(sorted_alarms)):           # check if input is valid index
                raise ValueError
        except ValueError:
            print("Wrong choice")
            return
        
        to_remove = sorted_alarms[select_i - 1]                     # get the alarm to remove    
        self.alarms = [a for a in self.alarms if a != to_remove]    # remove the selected alarm
        self.save_alarms()                                           # save updated alarms to file        
        self.logger.log(f"Alarm_Remove_{METRIC_LABEL[to_remove.metric]}_{to_remove.threshold}_Percent")  # log alarm removal
        print("Alarm removed.")
        

    # call from choice 7
    def _exit_program(self):
        self.save_alarms()                  # save alarms before exiting
        self.logger.log("Program_Exited")  # log program exit
        print("Program Exited.")        

if __name__ == "__main__":
    app = MonitoringApp()
    app.start()
# Note: The actual monitoring, alarm creation, listing, and removal logic needs to be implemented.
