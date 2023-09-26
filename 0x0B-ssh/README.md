# 0x0B. SSH




This project focuses on SSH configuration and key management, enabling secure remote access to servers using SSH key pairs and configuring the SSH client for improved usability and security.


## Requirements
- Ubuntu 20.04 LTS

## Dependencies
- Bash shell
- OpenSSH for SSH key generation and client configuration


## Tasks

| File Name                 | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| 0-use_a_private_key       | Bash script for SSH connection using a private key.             |
| 1-create_ssh_key_pair     | Bash script for generating an RSA key pair.                     |
| 2-ssh_config              | SSH client configuration file for key-based authentication.     |
| 3-add_ssh_public_key                 | manually adding an SSH public key to the `ubuntu` user's authorized keys on the server.             |
|100-puppet_ssh_config.pp| Puppet manifest for configuring SSH client with key-based auth.|

