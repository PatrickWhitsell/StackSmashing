# Similar to Metasloit's ruby script: pattern_create.rb
import sys

def create_pattern(length):
	caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lows = "abcdefghijklmnopqrstuvwxyz"
	nums = "0123456789"

	string = ""
	a = 0
	b = 0
	c = 0

	while len(string) < length:
	    string += caps[a] + lows[b] + nums[c]
	    c += 1
	    if c == len(nums):
	    	c = 0
	    	b += 1
	    if b == len(lows):
	    	b = 0
	    	a += 1
	    if a == len(caps):
	    	a = 0

	return string

def find_pattern(hexstr):
	asciiStr = ""
	for i in range(0, len(hexstr)):
		if i % 2 != 0:
			continue
		asciiStr += str(hexstr[i:i+2].decode('hex'))

	notFound = True
	length = 32
	while notFound:
		pattern = create_pattern(length)
		loc = pattern.find(asciiStr)

		if loc > -1:
			notFound = False

		length *= 2

	return loc


if len(sys.argv) != 2:
	print "[Usage 1:] python %s <length>" % sys.argv[0]
	print "[Usage 2:] python %s <hex pattern>" % sys.argv[0]
	sys.exit(1)

try:
	if sys.argv[1][:2] == '0x':
		hexstr = str(sys.argv[1][2:])
		fp = True
	else:
		length = int(sys.argv[1])
		fp = False
except:
	print "[Usage 1:] python %s <length>" % sys.argv[0]
	print "[Usage 2:] python %s 0x<hex>" % sys.argv[0]
	sys.exit(1)

if fp:
	loc = find_pattern(hexstr)
	print "-------------------------------------------------------------------------"
	print "First location:", loc #output the location of the pattern
	print "-------------------------------------------------------------------------"
else:
	string = create_pattern(length)
	print "-------------------------------------------------------------------------"
	print string[:length]
	print "-------------------------------------------------------------------------"