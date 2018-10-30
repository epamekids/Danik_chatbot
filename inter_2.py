i = 0
s = 0
d = 0
gr = []
par = []
while i < 20:
	print("Say something !")
	z =  input() 
	v = input("If you greet me, type 'gr', otherwise 'par'  ")
	if v == 'gr':
		if s == 0:
			gr.append(z)
			print(z)
		elif s > 0:
			if z in gr:
				print(z-1, "you have already wrote this")
			else:
				gr.append(z)
				print(z-1)
		s+=1
	elif v == 'par':
		if d == 0:
			par.append(z)
			print(z)
		elif d > 0 :
			if z in par:
				print(z-1, "you have already wrote this")
			else:
				par.append(z)
				print(z-1)
		d+=1
	else:
		print("I'm buzy right now, let's talk another time")
	i+=1