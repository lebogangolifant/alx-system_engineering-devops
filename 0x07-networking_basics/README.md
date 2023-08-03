
# 0x07. Networking basics #0

This project contains a collection of Bash scripts that provide information about networking basics. Related to networking concepts such as the OSI model, MAC and IP addresses, TCP and UDP protocols, and network port analysis.

### Usage:

- Ensure that all script files have the proper execution permissions to be executable.

    ```bash
    $  chmod +x 0-OSI_model
    ```

 - Execute the scripts: To run a specific task's script, simply execute the script file along with any necessary command-line arguments. **Example:**

   ```bash
   $ sudo ./4-TCP_and_UDP_ports
   ```

*Replace the script name and arguments as needed for other tasks.*



### Tasks description


| Script Name                      | Description                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| 0-OSI_model                      | Explains the OSI model and its organization. Includes correct answers to the following questions:<br>1. What is the OSI model?<br>   a) Set of specifications that network hardware manufacturers must respect<br>   b) The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology<br>   c) The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology<br>2. How is the OSI model organized?<br>   a) Alphabetically<br>   b) From the lowest to the highest level<br>   c) Randomly  |
| 1-types_of_network               | Provides information about different types of networks (LAN, WAN, Internet). Includes correct answers to the following questions:<br>1. What type of network a computer in local is connected to?<br>   a) Internet<br>   b) WAN<br>   c) LAN<br>2. What type of network could connect an office in one building to another office in a building a few streets away?<br>   a) Internet<br>   b) WAN<br>   c) LAN<br>3. What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?<br>   a) Internet<br>   b) WAN<br>   c) LAN  |
| 2-MAC_and_IP_address             | Explains MAC addresses and IP addresses and their respective functions. Includes correct answers to the following questions:<br>1. What is a MAC address?<br>   a) The name of a network interface<br>   b) The unique identifier of a network interface<br>   c) A network interface<br>2. What is an IP address?<br>   a) Is to devices connected to a network what postal address is to houses<br>   b) The unique identifier of a network interface<br>   c) Is a number that network devices use to connect to networks  |
| 3-UDP_and_TCP                    | Provides information about TCP and UDP protocols. Includes correct answers to the following questions:<br>1. Which statement is correct for the TCP box?<br>   a) It is a protocol that is transferring data in a slow way but surely<br>   b) It is a protocol that is transferring data in a fast way and might lose data along in the process<br>2. Which statement is correct for the UDP box?<br>   a) It is a protocol that is transferring data in a slow way but surely<br>   b) It is a protocol that is transferring data in a fast way and might lose data along in the process<br>3. Which statement is correct for the TCP worker?<br>   a) Have you received boxes x, y, z?<br>   b) May I increase the rate at which I am sending you boxes?  |
| 4-TCP_and_UDP_ports              | Displays listening ports along with the PID and program name.                                    |
| 5-is_the_host_on_the_network     | Pings an IP address passed as an argument to check if the host is available on the network.    |

