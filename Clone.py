filename = 'Clone.py'
filehandle = open(filename)
replicate = filehandle.read()
x = 1
while x > 0:
   x = x + 1
   f = open(str(x) + ".py","w+")
   f.write(str(replicate))
   f.close()
