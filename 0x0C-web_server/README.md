# 0x0C. Web server
#### Configuration with DevOps and SysAdmin

This project focuses on configuring a web server using various tools and techniques, including Bash scripting and Puppet manifests. Mainly setting up an Nginx web server on an Ubuntu machine and configure it.

## Dependencies

- Ubuntu 16.04 LTS
- Bash
- Puppet
- Nginx

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


| File Name                             | Description                                |
| ------------------------------------- | ------------------------------------------ |
| [0-transfer_file](./0-transfer_file)   | Transfer a file from client to server.     |
| [1-install_nginx_web_server](./1-install_nginx_web_server) | Install and configure Nginx. |
| [2-setup_domain](./2-setup_domain)     | Configure DNS for a domain.               |
| [3-redirection](./3-redirection)       | Configure Nginx for a 301 redirect.        |
| [4-not_found_page_404](./4-not_found_page_404) | Configure Nginx for a custom 404 page. |
| [7-puppet_install_nginx_web_server.pp](./7-puppet_install_nginx_web_server.pp) | Use Puppet to install and configure Nginx. |

