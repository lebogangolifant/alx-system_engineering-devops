# 0x06. Regular expression

This project contains a collection of Ruby scripts that utilize Oniguruma regular expressions (regex) library to perform pattern matching on text data, extract specific information from text messages transactions and produce useful statistics.

### Usage:

- Clone the repository

- Install Ruby

- Ensure that all script files have the proper execution permissions to be executable.

    ```bash
    $  chmod +x script_name.rb
    ```

 - Execute the scripts: To run a specific task's script, simply execute the Ruby script file along with any necessary command-line arguments. **Example:**

   ```bash
   $ ./0-simply_match_school.rb "School Best School"
   ```

*Replace the script name and arguments as needed for other tasks.*



### Tasks description


| Script File | Description | Pattern Type |
|-------------|-------------|--------------|
| 0-simply_match_school.rb | create a Ruby script that accepts one argument and matches the word "School" in the input string | Fixed Pattern |
| 1-repetition_token_0.rb |  create a Ruby script that accepts one argument to find and print strings containing the pattern "hbttn," where there can be one or more "t" characters between "h" and "n." | Repetition |
| 2-repetition_token_1.rb | create a Ruby script that accepts one argument to find and print strings containing the pattern "hbtn" or "hbtttn," where there can be zero or more "t" characters between "h" and "n." | Repetition |
| 3-repetition_token_2.rb | create a Ruby script that accepts one argument to find and print strings containing the pattern "hbn," "hbtn," "hbttn," or "hbtttn," where there can be one or more "t" characters between "h" and "n."  | Repetition |
| 4-repetition_token_3.rb | create a Ruby script that accepts one argument to find and print strings containing the pattern "hbn," "hbtn," "hbttn," "hbtttn," or "hbttttn," where there can be zero or more "t" characters between "h" and "n." | Repetition |
| 5-beginning_and_end.rb | create a Ruby script that accepts one argument to find and print strings that start with "h" and end with "n," with any single character in between | Fixed Pattern |
| 6-phone_number.rb | create a Ruby script that accepts one argument to find and print 10-digit phone numbers  | Fixed Pattern |
| 7-OMG_WHY_ARE_YOU_SHOUTING.rb | create a Ruby script that accepts one argument to find and print capitalized words in the input string | Character Class |
| 100-textme.rb | create a Ruby script that accepts a log file containing TextMe app text messages transactions. The script uses regular expressions to extract information such as sender, receiver, and flags from each log entry | Grouping and Capture |

