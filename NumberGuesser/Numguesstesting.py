import random
int
# for the randrange  the second number is upper limit
# will not generate the upper number only those
# below it, use .randint to include the upper number


r = random.randint(-5, 11)
print(r)
while r != 11:
    r = random.randint(-5, 11)
    print(r)

print("finnaly 11")

    


    
