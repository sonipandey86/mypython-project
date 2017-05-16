import random
with open('D:\Python\sowpods.txt') as f:
	words = list(f)
print(random.choice(words).strip())