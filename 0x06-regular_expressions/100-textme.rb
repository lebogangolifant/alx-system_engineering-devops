#!/usr/bin/env ruby

# Accept the log file path as a command-line argument
log_file_path = ARGV[0]

# Read the log file
log_content = File.read(log_file_path)

puts "Log Content:"
puts log_content

# Define a regular expression to extract the required information
regex = /from:(?<sender>.*?)\], to:(?<receiver>.*?)\], flags:(?<flags>.*?)$/

# Scan the log content and extract the information using the regex
matches = log_content.scan(regex)

# Output the extracted information
puts "SENDER,RECEIVER,FLAGS"

matches.each do |match|
  sender = match[0].strip
  receiver = match[1].strip
  flags = match[2].strip
  puts "#{sender},#{receiver},#{flags}"
end
