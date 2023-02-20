
# 0x03. Shell, init files, variables and expansions

#### Using bash command line, scripting to automate common tasks.

## Resources

__read__ or __watch__:

- [Expansion](https://intranet.alxswe.com/rltoken/oXnzBjLBA9t9dr7WuftdmQ)
- [Shell initialization files](https://intranet.alxswe.com/rltoken/tqud57kjsSYgDfeZDlwl3g)

OR  

- Youtube 
- Tutorial articles and more...

__man__ or __help__:

- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`

## General Requirements

- Editors: [emacs](https://www.gnu.org/software/emacs/), [vi, vim](https://www.vim.org/)
- Scripts tested on: __Ubuntu 20.04 LTS__
- The first line of all your files should be: `#!/bin/bash`
- Scripts should be two lines long: $ `wc -l <filename>`
- Make file executable, use command: `chmod u+x <filename>`

## Usage/Examples
###### *Example of line count and first line*

```

  lebogang@ubuntu:/projects$ wc -l 12-file_type 
  2 12-file_type
  lebogang@ubuntu:/projects$ head -n 1 12-file_type 
  #!/bin/bash
  lebogang@ubuntu:/projects$ 

```

###### *Example to make file executable, use the command: `chmod u+x file`*
```

  lebogang@ubuntu:/projects$ ls
  0x001-file
  0x002-print
  lebogang@ubuntu:/projects$chmod u+x 0x002-file #  make file executable
  lebogang@ubuntu:/projects$ ls -l 0x002-print
  -rwxrw-r-- 1 lebogang lebogang 08 Feb 23 09:05  0x002-print
  lebogang@ubuntu:/projects$ ./0x002-print #  prints script result in terminal
  0x001-file
  0x002-print
  lebogang@ubuntu:/projects$

```

## Project Tasks

| TASK FILE                      | DESCRIPTION      | 
|  -----------                   |  -----------     |
|[0-alias](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias)|Create a script that creates an alias.|
|[1-hello_you](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you)|Create a script that prints `hello user`, where user is the current Linux user.|
|[2-path](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path)|Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.|
|[3-paths](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths)|Create a script that counts the number of directories in the `PATH`.|
|[4-global_variables](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables)|Create a script that lists environment variables.|
|[5-local_variables](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables)|Create a script that lists all local variables and environment variables, and functions.|
|[6-create_local_variable](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable)|Create a script that creates a new local variable.|
|[7-create_global_variable](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable)|Create a script that creates a new global variable.|
|[8-true_knowledge](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge)|Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.|
|[9-divide_and_rule](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule)|Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.|
|[10-love_exponent_breath](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath)|Write a script that displays the result of `BREATH` to the power `LOVE`|
|[11-binary_to_decimal](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal)|Write a script that converts a number from base 2 to base 10. The number in base 2 is stored in the environment variable `BINARY`. The script should display the number in base 10, followed by a new line|
|[12-combinations](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations)|Create a script that prints all possible combinations of two letters, except `oo`. Letters are lower cases, from `a` to `z`. One combination per line. The output should be alpha ordered, starting with `aa`. Do not print `oo`. Your script file should contain maximum 64 characters|
|[13-print_float](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float)|Write a script that prints a number with two decimal places, followed by a new line. The number will be stored in the environment variable `NUM`.|
|[100-decimal_to_hexadecimal](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/100-decimal_to_hexadecimal)|Write a script that converts a number from base 10 to base 16. The number in base 10 is stored in the environment variable `DECIMAL`. The script should display the number in base 16, followed by a new line|
|[101-rot13](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/101-rot13)|Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.|
|[102-odd](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/102-odd)|Write a script that prints every other line from the input, starting with the first line.|
|[103-water_and_stir](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/103-water_and_stir)|Write a shell script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result. `WATER` is in base `water`. `STIR` is in base `stir`. The result should be in base `bestchol`|











