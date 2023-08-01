#!/usr/bin/env ruby

# Accept one argument
input = ARGV[0]

# Find the character class pattern in the input
puts input.scan(/[A-Z]/).join
