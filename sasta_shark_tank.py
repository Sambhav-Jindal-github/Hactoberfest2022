try:
	t = int(input())
	for i in range(t):
		a,b = map(int, input().split())
		if 100*a>50*b:
			print("FIRST")
		elif 100*a<50*b:
			print("SECOND")
		else:
			print("ANY")
except:
	pass