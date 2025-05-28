# quiz game python tutorial 

score = 0

print("Welcome to my leauge quiz")

playing = input("Want to take my leauge quiz? ")

if playing != "yes".lower():
    print("fuck you")
    quit()
print("Okay lets play")

answer = input("where did kaisa get her powers from? ").lower()
if answer in ["void", "the void", "from the void"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")  
   
answer = input("What race is Tristana? ").lower()
if answer in ["yordle"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!") 


answer = input("What area is Darius from? ").lower()
if answer in ["noxus"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")
   
answer = input("what was the old 3v3 map called? ").lower()
if answer in ["twisted treeline"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")

print(f"You got {score} of 4 questions correct!")
               
    
