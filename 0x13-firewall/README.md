# 0x13. Firewall

This project involves configuring a firewall and implementing port forwarding on the web servers. The goal is to ensure proper network security and efficient forwarding of network traffic.

## Requirements

- This project assumes you have access to Linux-based web servers.
- Knowledge of the `ufw` firewall and basic network configuration.

## Tasks

| File Name            | Description                                |
| -------------------- | ------------------------------------------ |
| 0-block_all_incoming_traffic_but | Configure `ufw` to block all incoming traffic, except for ports 22 (SSH), 80 (HTTP), and 443 (HTTPS). |
| 100-port_forwarding   | Implement port forwarding on `web-01` to redirect incoming traffic from port 8080 to port 80. |

