x = 0 
y = 0
z = 100
for i in range(5):
    score = int(input("Enter score out of 100 "+ str(i+1) + ": "))
    x += score
    if score > y:
        y = score 
    else:
        score = score
        
    if score < z:
        z = score
    else: 
        score = score

print ("Your average score is: " + str(x/5))
print ("Your best score is: " + str(y))
print ("Your worst score is: " + str(z))
