with open('sowpods.txt', 'r') as f:
  	line = f.readline()
  	while line:
  		print(line)
  		line = f.readline()