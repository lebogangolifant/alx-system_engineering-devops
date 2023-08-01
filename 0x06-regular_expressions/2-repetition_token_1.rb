#!/usr/bin/env ruby

# Accept one argument
input = ARGV[0]

# Use repetition token to find the pattern in the input
puts input.scan(/hb{1}?tn/).join
