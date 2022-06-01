import os
from string import printable
from collections import deque

flag = ''
encrypted_flag =  deque(['depaints', 'dexterous', 'dilution', 'droseras', 'dissecting', 'driveways', 'depaints', 'droughtier', 'diluted', 'demigods', 'diluter', 'beefing', 'dogey', 'dogfights', 'diligently', 'dusky', 'beefing', 'dogey', 'dogfights', 'desand', 'beefing', 'dilution', 'duenna', 'ditto', 'duenna', 'dockworkers', 'departments', 'dislocates', 'drawbars', 'beefing', 'dogey', 'dogfights', 'diligently', 'dusky', 'beefiest', 'eloigned', 'demigods', 'deteriorations', 'edge', 'defecation', 'deadpanned', 'dits', 'diluted', 'des', 'detentes', 'dementing', 'desanded', 'duelling', 'demes', 'deodorizing', 'deafnesses', 'devotees', 'combusting', 'capitalists', 'embruting', 'beefing', 'dogey', 'dogfights', 'diligently', 'dusky', 'beefing', 'dogey', 'dogfights', 'duskier', 'beefing', 'dogey', 'dogfights', 'desand', 'doweling', 'derangements', 'departments', 'dislocates', 'drawbars', 'disprized', 'depaints', 'demigods', 'decrypted'])

key = dict()

blink = True

for a in printable:
	f = open('flag.txt', 'w')
	letter_pairs = []
	for b in printable:
		f.write(a + b)
		letter_pairs.append(a + b)
	f.close()
	os.system('go run encrypt.go > output.txt')
	f = open('output.txt', 'r')
	words = f.read().split()
	f.close()
	for i in range(len(words)):
		key[words[i]] = letter_pairs[i]
		print(words[i], '=', letter_pairs[i])
	if len(encrypted_flag) > 0 and encrypted_flag[0] in key:
		flag += key[encrypted_flag.popleft()]

	if len(encrypted_flag) == 0:
		if  blink:
			print('!!! FLAG = ' + flag + ' !!!')
		blink = not blink
	else:
		print('*** FLAG = ' + flag + ' ***')

while len(encrypted_flag) != 0:
	if encrypted_flag[0] in key:
		flag += key[encrypted_flag.popleft()]

print('!!! FLAG = ' + flag + ' !!!')
