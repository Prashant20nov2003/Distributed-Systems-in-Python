#
# This file was automatically generated.

# Start state names
INITIAL = 0


# action 1 for pattern ":"
def action1(self) :
	return "COLON"
	

# action 2 for pattern "quit"
def action2(self) :
	return "QUIT" # Tok(self, "QUIT")
	

# action 3 for pattern "list"
def action3(self) :
	return "LIST"
	

# action 4 for pattern "inspect"
def action4(self) :
	return "INSPECT"
	

# action 5 for pattern "route"
def action5(self) :
	return "ROUTE"
	

# action 6 for pattern "watch"
def action6(self) :
	return "WATCH"
	

# action 7 for pattern "help"
def action7(self) :
	return "HELP"
	

# action 8 for pattern "{NUMBER}"
def action8(self) :
	try :
	        self.value = int(self.value)
	except ValueError :
	        print "Integer value too large", self.value
	        self.value = 0
	return "NUMBER"
	

# action 9 for pattern "[[:blank:]]"
def action9(self) :
	return
	

# action 10 for pattern "\n+"
def action10(self) :
	global lineno
	lineno += len(self.value)
	return
	
	

# action 11 for pattern "."
def action11(self) :
	print "Illegal character '%s'" % self.value
	return
	


rows = [ 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [2, 3, 4, 5, 6, 2, 2, 2, 2, 7, 8, 9, 2, 2, 2, 10, 11, 2, 2, 2, 12],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
acc = [[], [], [11], [9, 11], [10], [8, 11], [1, 11], [11], [11], [11], [11], [11], [11], [8], [], [], [], [], [], [], [], [], [], [], [], [], [7], [], [3], [2], [], [], [], [5], [6], [], [4]]
starts = [(1, 1)]
chr2uccl = {'\x00': 0, '\x83': 0, '\x04': 0, '\x87': 0, '\x08': 0, '\x8b': 0, '\x0c': 0, '\x8f': 0, '\x10': 0, '\x93': 0, '\x14': 0, '\x97': 0, '\x18': 0, '\x9b': 0, '\x1c': 0, '\x9f': 0, ' ': 1, '\xa3': 0, '$': 0, '\xa7': 0, '(': 0, '\xab': 0, ',': 0, '\xaf': 0, '0': 3, '\xb3': 0, '4': 3, '\xb7': 0, '8': 3, '\xbb': 0, '<': 0, '\xbf': 0, '@': 0, '\xc3': 0, 'D': 5, '\xc7': 0, 'H': 5, '\xcb': 0, 'L': 5, '\xcf': 0, 'P': 5, '\xd3': 0, 'T': 5, '\xd7': 0, 'X': 5, '\xdb': 0, '\\': 0, '\xdf': 0, '`': 0, '\xe3': 0, 'd': 5, '\xe7': 0, 'h': 9, '\xeb': 0, 'l': 11, '\xef': 0, 'p': 14, '\xf3': 0, 't': 18, '\xf7': 0, 'x': 5, '\xfb': 0, '|': 0, '\xff': 0, '\x80': 0, '\x03': 0, '\x84': 0, '\x07': 0, '\x88': 0, '\x0b': 0, '\x8c': 0, '\x0f': 0, '\x90': 0, '\x13': 0, '\x94': 0, '\x17': 0, '\x98': 0, '\x1b': 0, '\x9c': 0, '\x1f': 0, '\xa0': 0, '#': 0, '\xa4': 0, "'": 0, '\xa8': 0, '+': 0, '\xac': 0, '/': 0, '\xb0': 0, '3': 3, '\xb4': 0, '7': 3, '\xb8': 0, ';': 0, '\xbc': 0, '?': 0, '\xc0': 0, 'C': 5, '\xc4': 0, 'G': 5, '\xc8': 0, 'K': 5, '\xcc': 0, 'O': 5, '\xd0': 0, 'S': 5, '\xd4': 0, 'W': 5, '\xd8': 0, '[': 0, '\xdc': 0, '_': 5, '\xe0': 0, 'c': 7, '\xe4': 0, 'g': 5, '\xe8': 0, 'k': 5, '\xec': 0, 'o': 13, '\xf0': 0, 's': 17, '\xf4': 0, 'w': 20, '\xf8': 0, '{': 0, '\xfc': 0, '\x7f': 0, '\x81': 0, '\x02': 0, '\x85': 0, '\x06': 0, '\x89': 0, '\n': 2, '\x8d': 0, '\x0e': 0, '\x91': 0, '\x12': 0, '\x95': 0, '\x16': 0, '\x99': 0, '\x1a': 0, '\x9d': 0, '\x1e': 0, '\xa1': 0, '"': 0, '\xa5': 0, '&': 0, '\xa9': 0, '*': 0, '\xad': 0, '.': 0, '\xb1': 0, '2': 3, '\xb5': 0, '6': 3, '\xb9': 0, ':': 4, '\xbd': 0, '>': 0, '\xc1': 0, 'B': 5, '\xc5': 0, 'F': 5, '\xc9': 0, 'J': 5, '\xcd': 0, 'N': 5, '\xd1': 0, 'R': 5, '\xd5': 0, 'V': 5, '\xd9': 0, 'Z': 5, '\xdd': 0, '^': 0, '\xe1': 0, 'b': 5, '\xe5': 0, 'f': 5, '\xe9': 0, 'j': 5, '\xed': 0, 'n': 12, '\xf1': 0, 'r': 16, '\xf5': 0, 'v': 5, '\xf9': 0, 'z': 5, '\xfd': 0, '~': 0, '\x01': 0, '\x82': 0, '\x05': 0, '\x86': 0, '\t': 1, '\x8a': 0, '\r': 0, '\x8e': 0, '\x11': 0, '\x92': 0, '\x15': 0, '\x96': 0, '\x19': 0, '\x9a': 0, '\x1d': 0, '\x9e': 0, '!': 0, '\xa2': 0, '%': 0, '\xa6': 0, ')': 0, '\xaa': 0, '-': 0, '\xae': 0, '1': 3, '\xb2': 0, '5': 3, '\xb6': 0, '9': 3, '\xba': 0, '=': 0, '\xbe': 0, 'A': 5, '\xc2': 0, 'E': 5, '\xc6': 0, 'I': 5, '\xca': 0, 'M': 5, '\xce': 0, 'Q': 5, '\xd2': 0, 'U': 5, '\xd6': 0, 'Y': 5, '\xda': 0, ']': 0, '\xde': 0, 'a': 6, '\xe2': 0, 'e': 8, '\xe6': 0, 'i': 10, '\xea': 0, 'm': 5, '\xee': 0, 'q': 15, '\xf2': 0, 'u': 19, '\xf6': 0, 'y': 5, '\xfa': 0, '}': 0, '\xfe': 0}
actions = [None, action1, action2, action3, action4, action5, action6, action7, action8, action9, action10, action11]
eofactions = [None]

lexspec = (rows,acc,starts,actions,eofactions,chr2uccl)

tokens = (
        'COLON',
        'STRING','NUMBER',
        'QUIT', 'LIST', 'INSPECT', 'WATCH', 'HELP'
)

lineno = 1

class Tok :
        def __init__(self, l, type) :
                self.type = type
                self.lineno = lineno
                self.value = l.value
        def __str__(self) :
                return "Tok(%s,%r,%d)" % (self.type, self.value, self.lineno)


