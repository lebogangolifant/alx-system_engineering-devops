# 0x0A. Configuration management

This project focuses on configuration management using Puppet, DevOps practices, system administration, scripting, and CI/CD.

## Requirements

- Ubuntu 20.04 LTS
- Puppet 5.5
- Puppet lint 2.1.1

### Installation

Install __Puppet__ and __Puppet-lint__ using the following commands:

```bash
# Install Puppet
sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades
sudo apt-get install -y ruby-augeas
sudo apt-get install -y ruby-shadow
sudo apt-get install -y puppet

# Install Puppet lint
gem install puppet-lint
```

## Project Tasks


| File Name               | Description                                  |
| ----------------------- | -------------------------------------------- |
| 0-create_a_file.pp      | Create a file in `/tmp` with specific attributes. |
| 1-install_a_package.pp  | Install Flask version 2.1.0 using pip3.      |
| 2-execute_a_command.pp  | Terminate a process named "killmenow."      |
| README.md               | Project documentation        |

## Usage

Run the Puppet manifests using the `puppet apply` command. 

## Example:

```bash
sudo puppet apply 0-create_a_file.pp
```
