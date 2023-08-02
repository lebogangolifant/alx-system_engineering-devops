#!/usr/bin/env ruby

# Accept the log entry as a command-line argument
log_entry = ARGV[0]

# Define a regular expression to extract the required information
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Use the regular expression to extract sender, receiver, and flags
matches = log_entry.match(regex)

# Check if a match was found before accessing the elements
if matches
  puts "#{matches[1]},#{matches[2]},#{matches[3]}"
else
  puts "No match found in the log entry."
end
