def looknsay():
	displaynum = []
	displaynum.append(1)
	print("1")
	lastitem = 1
	countlast = 0
	while True:
		for x in displaynum:
			if x is lastitem:
				countlast += 1
			else:
				displaynum.append(countlast)
				countlast = 1
				lastitem = x
		displaynum.append(countlast)
		print(displaynum)