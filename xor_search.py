#@TACIXAT
#term you want to serch for goes in search variable
#suspected encrypted message goes in encrypted variable

search = 'secret'
encrypted = ')54.}4.}<}.8>/8)}08..<:8'

search_diff = ""
enc_diff = ""

prev = ""
for char in search:
	if prev != "":
		search_diff += chr(ord(char) ^ prev)
	prev = ord(char)
	
prev = ""
for char in encrypted:
	if prev != "":
		enc_diff += chr(ord(char) ^ prev)
	prev = ord(char)

index = -1
message = ''

try:
	index = enc_diff.index(search_diff)
	key = ord(encrypted[index]) ^ ord(search[0])
	
	print "key found:",
	print hex(key)
	
	print "decrypted:",
	for char in encrypted:
		message += chr(ord(char) ^ key)
	print message
except ValueError:
	print "PROG_ERR: search term not found in encrypted message"
	
