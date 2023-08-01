#!/usr/bin/env ruby

# Accept one argument
input = ARGV[0]

# Find the fixed string pattern in the input
puts input.scan(/^h.n$/).join
