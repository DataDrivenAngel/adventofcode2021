# day 1 part 1

# open
text = open("1-1-input.txt",'r')
inpt = text.read().split()
measurements = [int(line) for line in inpt]

# count number of higher measurements
count = 0
prev = measurements[0]
for measure in measurements[1:]:
   if measure > prev:
      count +=1 
   prev = measure

print(count)
#returns 1462
#which is correct