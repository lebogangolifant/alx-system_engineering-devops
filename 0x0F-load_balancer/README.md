# 0x0F. Load balancer

This project aims to automate the configuration of a load balancer and web servers for improved redundancy and reliability. It uses bash scripts and configuration files to achieve infrastructure setup.

## Dependencies

- Ubuntu 16.04 LTS
- Puppet 

## Installation

1. **Ubuntu 16.04 LTS:** 

2. **Install Bash and Puppet:**
   ```
   sudo apt-get update
   sudo apt-get install bash puppet
   ```
3. **Install Nginx:**
   ```
   sudo apt-get install nginx
   ```
4. **Set Up SSH Key:** Ensure that SSH key is set up correctly for file transfers.

## Project Tasks

| Filename                                 | Description                                                  |
| ---------------------------------------- | ------------------------------------------------------------ |
| `0-custom_http_response_header`          | Bash script to configure Nginx with a custom HTTP response header. |
| `1-install_load_balancer`                | Bash script to install and configure HAProxy for load balancing. |
| `2-puppet_custom_http_response_header.pp` | Puppet manifest to automate the creation of a custom HTTP header response in Nginx. |

