# 0x1B. Web stack debugging #4

This project involves debugging and optimizing a web server setup featuring Nginx. The goal is to address performance issues under load, fix configuration problems, and ensure that users can log in without encountering errors.

## Dependencies:

- Nginx
- Ubuntu 14.04 LTS

## Testing web server setup

### Issue:

The web server setup is facing performance issues under load, resulting in a significant number of failed requests during benchmarking with ApacheBench.

### Solution:

#### File: `0-the_sky_is_the_limit_not.pp`

- The Puppet manifest file modifies the Nginx configuration to improve performance and reduce failed requests.

### Execution:

```
$ puppet apply 0-the_sky_is_the_limit_not.pp
```

## Change the OS configuration

### Issue:

Logging in as the holberton user and attempting to open a file results in "Too many open files" errors.

### Solution:

#### File: `1-user_limit.pp`

- The Puppet manifest file changes the OS configuration, allowing login for the holberton user without encountering file limit errors.

### Execution:

```
$ puppet apply 1-user_limit.pp
```
