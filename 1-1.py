# day 1 part 1

# open
text = open("1-1-input.txt",'r')
inpt = text.read().split()
measurements = [int(line) for line in inpt]

# count number of higher measurements
count = 0
prev = measurements[0]
for measurem in measurements[1:]:
   if measure > prev
      count +=1 
   prev = measuremnt

print(count)
