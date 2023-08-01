#!/usr/bin/env ruby

# Accept one argument
input = ARGV[0]

# Find the fixed-length string pattern in the input
puts input.scan(/^\d{10}$/).join
