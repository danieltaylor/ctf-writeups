import os, time

# Running this script will print a demo of the steps to manually solve a many-time pad using a starting point.  See the README.md for more information.

class colors:
	reset = '\033[0m'
	bold = '\033[1m'
	underline = '\033[4m'
	black = '\033[30m'
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	magenta = '\033[35m'
	cyan = '\033[36m'
	white = '\033[37m'

states = [
('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
'LKAHEIIWPQPGQCUOXHIQFIUBXEHJBRU',
'RQXJTVSYVJVDJPASBLDQGIWWHPWISKT',
'DTKXPPECBFVHWLIEQXDNCFWCIYPXYFB'),

(colors.red + 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' + colors.reset,
'LKAHEIIWPQPGQCUOXHIQFIUBXEHJBRU',
'RQXJTVSYVJVDJPASBLDQGIWWHPWISKT',
'DTKXPPECBFVHWLIEQXDNCFWCIYPXYFB'),

(colors.green +'KMGFLEELPFEDQLABXPPWOEWJEWPEQRB' + colors.reset,
colors.magenta +'BYUCTEELALLDARUNASTUREYSTISFLAT' + colors.reset,
colors.magenta +'HEREIRONGERATEAREWOUSEANDTHECTS' + colors.reset,
colors.magenta +'THESELARMAREGAIDTIOROBATECATIOA' + colors.reset),

('KMGFLEELPFEDQLABXPPWOEWJEWPEQRB',
'BYUCT' + colors.red +'E' + colors.reset + 'ELALLDARUNASTUREYSTISFLAT',
'HEREIRONGERATEAREWOUSEANDTHECTS',
'THESELARMAREGAIDTIOROBATECATIOA'),

('KMGFL' + colors.magenta + 'D' + colors.reset + 'ELPFEDQLABXPPWOEWJEWPEQRB',
'BYUCT' + colors.green +'F' + colors.reset + 'ELALLDARUNASTUREYSTISFLAT',
'HEREI' + colors.magenta + 'S' + colors.reset + 'ONGERATEAREWOUSEANDTHECTS',
'THESE' + colors.magenta + 'M' + colors.reset + 'ARMAREGAIDTIOROBATECATIOA'),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLABXPPWOEWJEWPEQRB',
'BYUCT' + colors.cyan +'F' + colors.reset + 'ELALLDARUNASTUREYSTISFLAT',
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEAREWOUSEANDTHECT' + colors.red + 'S' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAIDTIOROBATECATIOA'),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLABXPPWOEWJEWPEQR' + colors.magenta + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARUNASTUREYSTISFLA' + colors.magenta + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEAREWOUSEANDTHECT' + colors.green + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAIDTIOROBATECATIO' + colors.magenta + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLABXPPWOEWJEWPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARUNASTUREYSTISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEAREWOUSEANDTHECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAIDTIOROB' + colors.red + 'ATE' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLABXPPWOE' + colors.magenta + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARUNASTURE' + colors.magenta + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEAREWOUSE' + colors.magenta + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAIDTIOROB' + colors.green + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLABXPPWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARU' + colors.red + 'NAS' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEAREWOUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAIDTIOROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLA' + colors.magenta + 'MXS' + colors.reset + 'PWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARU' + colors.green + 'CAP' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + 'ONGERATEA' + colors.magenta + 'GET' + colors.reset + 'OUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAI' + colors.magenta + 'STF' + colors.reset + 'OROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + 'ELPFEDQLA' + colors.cyan + 'MXS' + colors.reset + 'PWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + 'ELALLDARU' + colors.cyan + 'CAP' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + colors.red + 'ONG' + colors.reset + 'ERATEA' + colors.cyan + 'GET' + colors.reset + 'OUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + 'ARMAREGAI' + colors.cyan + 'STF' + colors.reset + 'OROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + colors.magenta + 'AKJ' + colors.reset + 'FEDQLA' + colors.cyan + 'MXS' + colors.reset + 'PWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + colors.magenta + 'IMG' + colors.reset + 'LLDARU' + colors.cyan + 'CAP' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + colors.green + 'SOM' + colors.reset + 'ERATEA' + colors.cyan + 'GET' + colors.reset + 'OUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + colors.magenta + 'ESS' + colors.reset + 'AREGAI' + colors.cyan + 'STF' + colors.reset + 'OROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + colors.cyan + 'AKJ' + colors.reset + 'FEDQLA' + colors.cyan + 'MXS' + colors.reset + 'PWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + colors.cyan + 'IMG' + colors.reset + 'L' + colors.red + 'L' + colors.reset + 'D' + colors.red + 'AR' + colors.reset + 'U' + colors.cyan + 'CAP' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + colors.cyan + 'SOM' + colors.reset + 'ERATEA' + colors.cyan + 'GET' + colors.reset + 'OUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + colors.cyan + 'ESS' + colors.reset + 'AREGAI' + colors.cyan + 'STF' + colors.reset + 'OROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),

('KMGFL' + colors.cyan + 'D' + colors.reset + colors.cyan + 'AKJ' + colors.reset + 'F' + colors.magenta + 'P' + colors.reset + 'D' + colors.magenta + 'SO' + colors.reset + 'A' + colors.cyan + 'MXS' + colors.reset + 'PWOE' + colors.cyan + 'RIQ' + colors.reset + 'WPEQR' + colors.cyan + 'O' + colors.reset,
'BYUCT' + colors.cyan + 'F' + colors.reset + colors.cyan + 'IMG' + colors.reset + 'L' + colors.green + 'A' + colors.reset + 'D' + colors.green + 'YO' + colors.reset + 'U' + colors.cyan + 'CAP' + colors.reset + 'TURE' + colors.cyan + 'DTH' + colors.reset + 'ISFLA' + colors.cyan + 'G' + colors.reset,
'HEREI' + colors.cyan + 'S' + colors.reset + colors.cyan + 'SOM' + colors.reset + 'E' + colors.magenta + 'G' + colors.reset + 'A' + colors.magenta + 'RB' + colors.reset + 'A' + colors.cyan + 'GET' + colors.reset + 'OUSE' + colors.cyan + 'FOR' + colors.reset + 'THECT' + colors.cyan + 'F' + colors.reset,
'THESE' + colors.cyan + 'M' + colors.reset + colors.cyan + 'ESS' + colors.reset + 'A' + colors.magenta + 'G' + colors.reset + 'E' + colors.magenta + 'EX' + colors.reset + 'I' + colors.cyan + 'STF' + colors.reset + 'OROB' + colors.cyan + 'FUS' + colors.reset + 'CATIO' + colors.cyan + 'N' + colors.reset),
]

for state in states:
	os.system('clear')
	print()
	print('  ' + '              Key')
	print('  ' + state[0])
	print()
	print('  ' + '           Plaintexts')
	print('  ' + state[1])
	print('  ' + state[2])
	print('  ' + state[3])
	print()
	time.sleep(1.5)

blink = [
('KMGFLDAKJFPDSOAMXSPWOERIQWPEQRO',
'BYUCTFIMGLADYOUCAPTUREDTHISFLAG',
'HEREISSOMEGARBAGETOUSEFORTHECTF',
'THESEMESSAGEEXISTFOROBFUSCATION'),

(colors.green + 'KMGFLDAKJFPDSOAMXSPWOERIQWPEQRO' + colors.reset,
colors.green + 'BYUCTFIMGLADYOUCAPTUREDTHISFLAG' + colors.reset,
colors.green + 'HEREISSOMEGARBAGETOUSEFORTHECTF' + colors.reset,
colors.green + 'THESEMESSAGEEXISTFOROBFUSCATION' + colors.reset)
]

for i in range(0,9):
	state = blink[0] if i % 2 else blink[1]
	os.system('clear')
	print()
	print('  ' + '              Key')
	print('  ' + state[0])
	print()
	print('  ' + '           Plaintexts')
	print('  ' + state[1])
	print('  ' + state[2])
	print('  ' + state[3])
	print()
	time.sleep(.2)
time.sleep(2)
