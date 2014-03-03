def sortcat(n, *args):
	maxLen = 0
	for i in range(len(args)):
		if len(args[i]) > maxLen: maxLen = len(args[i])

	concatStr = ""	

	if (n == -1):
		while (maxLen > 0):
			for i in range(len(args)):
				if len(args[i]) == maxLen: concatStr += args[i]
			maxLen -= 1	
	else:
		passes = 0
		while (passes < n):
			for i in range(len(args)):
				if len(args[i]) == maxLen: concatStr += args[i]
			maxLen -= 1
			passes += 1	
	print concatStr		

sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')
