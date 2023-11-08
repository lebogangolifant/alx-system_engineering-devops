# 0x17. Web stack debugging #3

This project focuses on web stack debugging and configuration management using Puppet. It includes identifying and resolving issues with an Apache web server returning a 500 Internal Server Error and automating the fix using Puppet manifests.


## Dependencies

- An Ubuntu 14.04 LTS environment.
- Puppet v3.4 installed on the system.
- The `puppet-lint` tool (version 2.1.1) installed for linting Puppet code.

## Installations
Command to install `puppet-lint`:

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
## Debugging
#### Debugging with `tmux`

Use `tmux` for concurrent debugging.
* Command to install tmux:

```
sudo apt-get install tmux
```
#### Debugging with `strace`

To debug issues with Apache returning a 500 error, you can use `strace` to trace system calls and signals. Here's how you can use it:

1. Attach to a currently running Apache process:

```
sudo strace -p <apache_process_id>
```

2. While `strace` is running, you can use `curl` or a web browser to trigger the 500 error in another terminal.

## Project Task:

The project directory contains the following files:

- `0-strace_is_your_friend.pp`: A Puppet manifest for fixing the Apache 500 error issue.

## Usage

1. Clone the project repository to your Ubuntu 14.04 LTS system.

2. Navigate to the project directory:

```
$ cd path/to/your/project/directory
```

3. Apply the Puppet manifest to fix the Apache 500 error issue:

```
$ puppet apply 0-strace_is_your_friend.pp
```
