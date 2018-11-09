i = 0
s = 0
d = 0
prons = ["I", "we", "you", "he", "she", "it", "they"]
prons_other = ["my", "their", "our", "her", "his"]
nouns = []
verbs = ["am", "is", "are", "do", "does", "have", "can", "could"] 
preps = ["an", "the", "a", "at", "to", "by", "from", "for", "up", "down", "beside", "behind"]
adverb = ["always", "usually", "often", "seldom", "rarely", "never"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
while i < 20:
	print("Say something !")
	z =  input() 
	lst = z.split()
	while s < len(lst):
		if (lst[s] == "Every") or (lst[s] == "every"):
			adverb.append(lst[s])
			adverb.append(lst[s+1])
		if lst[s] in prons:
			if lst[s+1] in adverb:
				verbs.append(lst[s+2])
				nouns.append(lst[s+3])
			else:
				verbs.append(lst[s+1])
				if lst[s+2] == "to":
					verbs.append(lst[s+3])
				if "s" in lst[s+2]:
					nouns.append(lst[s+2])
				else:
					verbs.append(lst[s+2])
					nouns.append(lst[s+3])
			nouns.append(lst[s+1])
		if lst[s] in preps:
			nouns.append(lst[s+1])
			if lst[s+1] in preps:
				nouns.append(lst[s+2])
			elif lst[s+1] in num:
				nouns.append(lst[s+2])
		s+=1
	print(adverb, nouns, verbs)
	i+=1