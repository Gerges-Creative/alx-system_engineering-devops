#!/usr/bin/env ruby

#sender = ARGV[0].scan(/from:(\S[A-Za-z0-9]+)/)
#receiver = ARGV[0].scan(/to:(\S[0-9]+)/)
#flags = ARGV[0].scan(/flags:([-1,0:]+)/)

puts ARGV[0].scan(/from:(\S[A-Za-z0-9]+)\] \[to:(\S[0-9]+)\] \[flags:([-1,0:]+)/).join","
