#!/usr/bin/env ruby

# Accept one argument 
input = ARGV[0]
 
# Find the matching string in the input
puts input.scan(/hbt{2,5}n/).join
