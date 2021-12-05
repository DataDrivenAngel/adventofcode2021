# day 1 part 2

# open
text = open("1-1-input.txt",'r')
inpt = text.read().split()
measurements = [int(line) for line in inpt]

# count number of higher measurements
count = 0
window_front = 3
window_back = 0
prev = measurements[window_back:window_front]

for measure in (measurements[1:]):
    
    window_front +=1
    window_back +=1
    window = measurements[window_back:window_front]

    window_sum = sum(window)
    prev_sum = sum(prev)
    if window_sum > prev_sum:
        count +=1
    prev = window
    

print(count)
# returns 1497
# which is correct
