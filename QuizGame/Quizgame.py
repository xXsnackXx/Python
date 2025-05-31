# quiz game python tutorial 

score = 0

print("Welcome to my leauge quiz")

playing = input("Want to take my leauge quiz? ").lower().strip()

if playing != "yes":
    print("Then why did you open me!")
    quit()
print("Okay lets play")

answer = input("where did kaisa get her powers from? ").lower().strip()
if answer in ["void", "the void", "from the void"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")  
   
answer = input("What race is Tristana? ").lower().strip()
if answer in ["yordle"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!") 


answer = input("What area is Darius from? ").lower().strip()
if answer in ["noxus"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")
   
answer = input("what was the old 3v3 map called? ").lower().strip()
if answer in ["twisted treeline"]:
    print("Correct!")
    score += 1
else:
    print("Nope!")
    print("Nope!")

print(f"You got {score} of 4 questions correct! ({(score / 4) * 100}%)")
               
    
