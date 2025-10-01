# Python-assignment
🎯 Final Individual Assignment – System Development in Python


**Deadline for submitting code (GitHub link) and report (PDF): October 24**
**Presentations: September 27 + September 29 (book slots).**

The task is to **write a monitoring application in Python**.
The application should collect information from the operating system and present it to a user.

The user will interact with the application via a **console menu** to view information such as:

* CPU usage
* Memory usage
* Disk usage

⚠️ Important: When the user is navigating the console menu, **no configured alarms should be triggered**.

---

## ✅ Requirements for "Pass" (Godkänd / G level)

When the program starts, the user should be presented with **five menu options** in the console:

---

### 1. Start Monitoring

* Begins monitoring CPU usage, memory usage, and disk usage.
* Note: Monitoring should **not** start automatically when the program launches.

---

### 2. List Active Monitoring

* Lists currently active monitoring and its current status.
* If no monitoring is active, display a message:
  `"No monitoring is active."`
* Otherwise, display something like:

```
CPU Usage: 35%  
Memory Usage: 65% (4.2 GB out of 8 GB used)  
Disk Usage: 80% (400 GB out of 500 GB used)  
```

* After displaying, prompt user:

```
Press Enter to confirm.  
Press any key to return to the main menu.  
```

---

### 3. Create Alarm

* Shows a submenu where the user can configure alarms:

```
Configure alarm:  
1. CPU usage  
2. Memory usage  
3. Disk usage  
4. Back to main menu  
```

* After choosing an option, the user sets a threshold level (0–100%). Example:

```
Set alarm level between 0–100.  
```

* Once configured, confirm:

```
CPU usage alarm set to 80%.  
```

* If the user enters invalid input (nonsense or outside 1–100), show an error.

---

### 4. Show Alarms

* Lists all configured alarms, sorted by type. Example:

```
CPU Alarm 70%  
Disk Alarm 95%  
Memory Alarm 80%  
Memory Alarm 90%  
```

* After displaying, prompt:

```
Press Enter to confirm.  
Press any key to return to the main menu.  
```

* Multiple alarms of the same type are allowed.

---

### 5. Start Monitoring Mode

* Activates continuous monitoring mode.
* Inform user:

```
Monitoring started.  
```

* Loop a message:

```
Monitoring is active, press any key to return to menu.  
```

* If an alarm is triggered during monitoring, display in console:

```
***WARNING, ALARM TRIGGERED, CPU USAGE EXCEEDS 80%***  
```

---

## 📋 Non-functional requirements for "Pass"

* Program must use **multiple files** (not all code in one file).
* Use **classes/objects** where appropriate.
* Use **functions**.
* Include **functional programming** at least once (e.g., sorting alarms).
* Code must be **well-structured** with clear names and comments.
* Must handle **invalid input** gracefully (input sanitization).
* Must be **bug-free**.

---

## ⭐ Requirements for "Pass with Distinction" (Väl Godkänd / VG level)

In addition to all "Pass" requirements:

### 1. Logging

* All events should be logged to a file.
* Log includes date, time, and event. Example:

```
20/9/2024_15:05_CPU_Usage_Alarm_Configured_80_Percent  
20/9/2024_15:09_Monitoring_Mode_Started  
20/9/2024_15:16_CPU_Usage_Alarm_Triggered_80_Percent  
```

* Each program run should create a **new log file**, named dynamically based on date and time.

---

### 2. Remove Alarm

* Add menu option to remove alarms.
* User sees a numbered list of alarms and can select one to delete:

```
Choose an alarm to remove:  
1. CPU Alarm 70%  
2. Memory Alarm 80%  
3. Memory Alarm 90%  
4. Disk Alarm 95%  
```

* After removal, return to main menu.

---

### 3. Persist Alarms (Save/Load from Disk)

* Alarms must be **saved in a file** (e.g., JSON).
* When the program starts, load previous alarms and display:

```
Loading previously configured alarms...  
```

* Both newly created and loaded alarms should appear in "Show Alarms".

---

## 📋 Non-functional requirements for VG

* Code must be **very well written and structured**.
* Example:

  * If multiple CPU alarms exist (60%, 70%, 80%) and usage jumps to 95%, only the **highest relevant alarm (80%)** should trigger.

---

## ➕ Optional Features (Bonus)

* Send email notifications when alarms trigger (using SendGrid).
* Version control with GitHub, trunk-based development, feature branches.
* Add a simple **graphical interface** (GUI) showing active alarms and live usage.



