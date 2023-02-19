
# 0x00. Shell, basics 

#### Using bash command line, scripting to automate common tasks.

## Resources

__read__ or __watch__:

- Learn [Linux](http://linuxcommand.org)

OR  

- Youtube 
- Tutorial articles and more...

__man__ or __help__:

- `cd`
- `ls`
- `pwd`
- `less`
- `file`
- `ln`
- `cp`
- `mv`
- `rm`
- `mkdir`
- `type`
- `which`
- `help`
- `man`

## General Requirements

- Editors: [emacs](https://www.gnu.org/software/emacs/), [vi, vim](https://www.vim.org/)
- Scripts tested on: __Ubuntu 20.04 LTS__
- The first line of all your files should be: `#!/bin/bash`
- Scripts should be two lines long: $ `wc -l <filename>`
- Make file executable, use command: `chmod u+x <filename>`

## Usage/Examples
###### *Example of line count and first line*

```json
{
  lebogang@ubuntu:/projects$ wc -l 12-file_type 
  2 12-file_type
  lebogang@ubuntu:/projects$ head -n 1 12-file_type 
  #!/bin/bash
  lebogang@ubuntu:/projects$ 
}
```

###### *Example to make file executable, use the command: `chmod u+x file`*
```json
{
  lebogang@ubuntu:/projects$ ls
  0x001-file
  0x002-file
  lebogang@ubuntu:/projects$chmod u+x 0x002-file #    make file executable
  lebogang@ubuntu:/projects$ ls -l 0x002-file
  -rwxrw-r-- 1 lebogang lebogang 08 Feb 23 09:05  0x002-file
  lebogang@ubuntu:/projects$ ./0x002-file
  0x001-file
  0x002-file
  lebogang@ubuntu:/projects$
}
```

## Projects Tasks

| TASK FILE                      | DESCRIPTION      | 
|  -----------                   |  -----------     |
| [0-current_working_directory](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory) | Write a script that prints the absolute path name of the current working directory.            |
|[1-listit](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)|Display the contents list of your current directory. |
|[2-bring_me_home](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)|Write a script that changes the working directory to the user’s home directory.|
|[3-listfiles](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)|Display current directory contents in a long format|
|[4-listmorefiles](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)|Display current directory contents, including hidden files (starting with .). Use the long format.|
|[5-listfilesdigitonly](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)| Display current directory contents.Long format, with user and group IDs displayed numerically, And hidden files, (starting with .) |
|[6-firstdirectory](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)|Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.|
|[7-movethatfile](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)|Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.|
|[8-firstdelete](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)|Delete the file `betty`. The file `betty` is in `/tmp/` `my_first_directory`|
|[9-firstdirdeletion](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)|Delete the directory `my_first_directory` that is in the `/tmp` directory.| 
|[10-back](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/10-back)|Write a script that changes the working directory to the previous one.|
|[11-lists](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)|Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format|
|[12-file_type](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type)|Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.|
|[13-symbolic_link](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)|Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.|
|[14-copy_html](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)|Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can consider that all HTML files have the extension `.html`|
|[100-lets_move](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/100-lets_move)|Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`. You can assume that the directory `/tmp/u` will exist when we will run your script|
|[101-clean_emacs](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/101-clean_emacs)|Create a script that deletes all files in the current working directory that end with the character `~`.|
|[102-tree](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/102-tree)|Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory. You are only allowed to use two spaces (and lines) in your script, not more.|
|[103-commas](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/103-commas)|Write a command that lists all the files and directories of the current directory, separated by commas (`,`).Directory names should end with a slash (`/`). Files and directories starting with a dot (`.`) should be listed. The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first. You can assume that all the files we will test with will have at least one letter or one digit.The listing should end with a new line.|
|[school.mgc](https://github.com/lebogangolifant/alx-system_engineering-devops/blob/master/0x00-shell_basics/school.mgc)|Create a magic file `school.mgc` that can be used with the command file to detect School data files. School data files always contain the string `SCHOOL` at offset `0`.|    











