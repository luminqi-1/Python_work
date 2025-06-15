for num in range(1,21):
	print (num)

lists = list(range(1, 1000001))
print (min(lists))
print(max(lists))
print(sum(lists))

single=list(range(1,20,2))
for num in single:
	print (num)

three=list(range(3,31,3))
for num in three:
	print (num)

sq = []
for num in range(1,11):
	sq.append(num**3)
	print (sq)
for the in sq:
	print(the)

sqs = [num**3 for num in range(1,11)]
print (sqs)
