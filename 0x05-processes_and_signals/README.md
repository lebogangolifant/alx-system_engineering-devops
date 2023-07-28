
# 0x05. Processes and signals

This project contains a set of Bash scripts and C programs that demonstrate various concepts related to processes and signals in Unix-like operating systems.

### Tasks description

| Task                                           | Description                                                                                                                                              | Usage                                          |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| **0. 0-what-is-my-pid**                      | Write a Bash script that displays its own PID.                                                                                                          | `./0-what-is-my-pid`                           |
| **1. 1-list_your_processes**                 | Write a Bash script that displays a list of currently running processes.                                                                               | `./1-list_your_processes`                      |
|                                               | - Must show all processes, for all users, including those which might not have a TTY                                                                   |                                                |
|                                               | - Display in a user-oriented format                                                                                                                     |                                                |
|                                               | - Show process hierarchy                                                                                                                                 |                                                |
| **2. 2-show_your_bash_pid**                  | Using the previous exercise command, write a Bash script that displays lines containing the word "bash," allowing you to easily get the PID of your Bash process. | `./2-show_your_bash_pid`                      |
| **3. 3-show_your_bash_pid_made_easy**        | Write a Bash script that displays the PID and process name of processes whose name contains the word "bash."                                          | `./3-show_your_bash_pid_made_easy`            |
| **4. 4-to_infinity_and_beyond**              | Write a Bash script that displays "To infinity and beyond" indefinitely with a sleep of 2 seconds between each iteration.                              | `./4-to_infinity_and_beyond`                  |
| **5. 5-dont_stop_me_now**                    | Write a Bash script that stops the process started by the `4-to_infinity_and_beyond` script.                                                          | `./5-dont_stop_me_now`                        |
| **6. 6-stop_me_if_you_can**                  | Write a Bash script that stops the process started by the `4-to_infinity_and_beyond` script without using `kill` or `killall`.                          | `./6-stop_me_if_you_can`                      |
| **7. 7-highlander**                          | Write a Bash script that displays "To infinity and beyond" indefinitely and "I am invincible!!!" when receiving a SIGTERM signal.                       | `./7-highlander`                              |
|                                               | Create a copy of the `6-stop_me_if_you_can` script named `67-stop_me_if_you_can`, which kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one. | `./67-stop_me_if_you_can`                    |
| **8. 8-beheaded_process**                    | Write a Bash script that kills the process started by the `7-highlander` script.                                                                      | `./8-beheaded_process`                        |
| **9. 100-process_and_pid_file**              | Write a Bash script that creates the file `/var/run/myscript.pid` containing its PID, displays "To infinity and beyond" indefinitely, and responds to specific signals.| `sudo ./100-process_and_pid_file`             |
| **10. 101-manage_my_process**                | Write a Bash script that manages the `100-process_and_pid_file` script with the options: start, stop, and restart.                                     | `sudo ./101-manage_my_process {start|stop|restart}` |
| **11. 102-zombie.c**                         | Write a C program that creates 5 zombie processes and displays their PIDs.                                                                             | `gcc 102-zombie.c -o zombie` <br> `./zombie`   |
