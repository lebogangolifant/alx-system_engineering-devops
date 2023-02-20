
# 0x02. Shell, I/O Redirections and filters

#### Using bash command line, scripting to automate common tasks.

## Resources

__read__ or __watch__:

- Learn [Shell, I/O Redirection](https://intranet.alxswe.com/rltoken/fGOQQXRKbvOcd1qLRxHzLQ)

OR  

- Youtube 
- Tutorial articles and more...

__man__ or __help__:

- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`
- `passwd (5)` (i.e. `man 5 passwd`)

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
|[0-hello_world](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world)| Write a script that prints “Hello, World”, followed by a new line to the standard output.|
|[1-confused_smiley](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley)|Write a script that displays a confused smiley `"(Ôo)'`.|
|[2-hellofile](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile)|Display the content of the `/etc/passwd` file.|
|[3-twofiles](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles)|Display the content of `/etc/passwd` and `/etc/hosts`|
|[4-lastlines](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines)|Display the last 10 lines of `/etc/passwd`|
|[5-firstlines](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines)|Display the first 10 lines of `/etc/passwd`|
|[6-third_line](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line)|Write a script that displays the third line of the file `iacta`. The file `iacta` will be in the working directory. You’re not allowed to use `sed`|
|[7-file]()|Write a shell script that creates a file containing the text `Best School` ending by a new line.|
|[8-cwd_state](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state)|Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.|
|[9-duplicate_last_line](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line)|Write a script that duplicates the last line of the file `iacta`. The file `iacta` will be in the working directory|
|[10-no_more_js](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js)|Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.|
|[11-directories](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories)|Write a script that counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted|
|[12-newest_files](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files)|Create a script that displays the 10 newest files in the current directory. Requirements: One file per line Sorted from the newest to the oldest|
|[13-unique](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique)|Create a script that takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word Words should be sorted|
|[14-findthatword](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword)|Display lines containing the pattern “root” from the file `/etc/passwd`|
|[15-countthatword](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword)|Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`|
|[16-whatsnext](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext)|Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.|
|[17-hidethisword](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword)|Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.|
|[18-letteronly](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly)|Display all lines of the file `/etc/ssh/sshd_config` starting with a letter. include capital letters as well|
|[19-AZ](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ)|Replace all characters `A` and `c` from input to `Z` and `e` respectively.|
|[20-hiago](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago)|Create a script that removes all letters `c` and `C` from input.|
|[21-reverse](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse)|Write a script that reverse its input.|
|[22-users_and_homes](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes)|Write a script that displays all users and their home directories, sorted by users. Based on the the `/etc/passwd` file|
|[100-empty_casks](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/100-empty_casks)|Write a command that finds all empty files and directories in the current directory and all sub-directories.|
|[101-gifs](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/101-gifs)|Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.|
|[102-acrostic](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/102-acrostic)|An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval.Create a script that decodes acrostics that use the first letter of each line.|
|[103-the_biggest_fan](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x02-shell_redirections/103-the_biggest_fan)|Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.|











