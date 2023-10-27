# 0x12. Web stack debugging #2

This project involves debugging web server configurations, focusing on running Nginx as the 'nginx' user and listening on port 8080.

## Requirements

- All files are interpreted on Ubuntu 20.04 LTS.
- All Bash script files are executable.
- Bash scripts pass Shellcheck without errors.
- Bash scripts run without error.
- The first line of all Bash scripts is `#!/usr/bin/env bash`.
- The second line of all Bash scripts contains a comment explaining the script's purpose.

## Usage

Execute the script, example:

```bash
./0-iamsomeoneelse username
```
Replace username with the user you want to run the whoami command as.

## Project Tasks

| File Name                | Description                                           |
|--------------------------|-------------------------------------------------------|
| 0-iamsomeoneelse         | Bash script to run `whoami` under the specified user. |
| 1-run_nginx_as_nginx     | Bash script to configure Nginx to run as 'nginx' user and listen on port 8080. |
| 100-fix_in_7_lines_or_less | Bash script to fix Nginx configuration in 7 lines or less. |

