import re

with open("rarities.txt", "rb") as r:
	pat = re.compile(b"\w+: (\d+)\n")

	line = r.readline()
	commons = int(pat.match(line).group(1))

	line = r.readline()
	uncommons = int(pat.match(line).group(1))

	line = r.readline()
	scarces = int(pat.match(line).group(1))

	line = r.readline()
	rares = int(pat.match(line).group(1))

	line = r.readline()
	epics = int(pat.match(line).group(1))

	line = r.readline()
	total = int(pat.match(line).group(1))


if total > 0:
	print("Commons, Uncommons, Scarces, Rares, Epics, Total:")
	print(commons, uncommons, scarces, rares, epics, total)
	print("{0:.2f}%, {1:.2f}%, {2:.2f}%, {3:.2f}%, {4:.2f}%, {5:.2f}%".format(\
		commons/total*100, uncommons/total*100, scarces/total*100, rares/total*100, epics/total*100, 100))
else:
	print("No packs opened.")
	
Common = ["c", "C"]
Uncommon = ["u", "U"]
Scare = ["s", "S"]
Rare = ["r", "R"]
Epic = ["e", "E"]
Quit = ["q", "Q"]

while True:
	command = input("Command: ")
	total += 1
	if command in Common:
		commons += 1
	elif command in Uncommon:
		uncommons += 1
	elif command in Scare:
		scarces += 1
	elif command in Rare:
		rares += 1
	elif command in Epic:
		epics += 1
	elif command in Quit:
		exit(0)
	else:
		print("Invalid Command.")
		total -= 1
		if total < 1:
			total = 1
	
	with open("rarities.txt", 'wb'): pass

	with open("rarities.txt", "at") as f:
		f.write("Commons: {}\n".format(commons)), 
		
		f.write("Uncommons: {}\n".format(uncommons)), 
		
		f.write("Scarces: {}\n".format(scarces)), 
		
		f.write("Rares: {}\n".format(rares)), 
		
		f.write("Epics: {}\n".format(epics)), 

		f.write("Total: {}\n".format(total)), 

	print(commons, uncommons, scarces, rares, epics, total)
	print("{0:.2f}%, {1:.2f}%, {2:.2f}%, {3:.2f}%, {4:.2f}%, {5:.2f}%".format(\
		commons/total*100, uncommons/total*100, scarces/total*100, rares/total*100, epics/total*100, 100))
