import random

def simulGame(n):
	numWins = 0
	for i in range(n):
		Luigi = getDirection()
		Peach = getDirection()
		Mario = getDirection()
		Wario = getDirection()

		if (Luigi != Peach and Luigi != Mario and Luigi != Wario): numWins += 1

	return float(numWins)/n	

def getDirection():
	rand = random.randint(1,10)
	if (rand <= 2): return "forward"
	elif (rand <= 4): return "up"
	elif (rand <= 6): return "down"
	elif (rand <= 8): return "left"
	else:
		return "right"

print (simulGame(10))
print (simulGame(100))
print (simulGame(1000))		