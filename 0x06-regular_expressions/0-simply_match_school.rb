#!/usr/bin/env ruby

# Accept one argument
input = ARGV[0]

# Print the matched string to the standard output
puts ARGV[0].scan(/School/).join
