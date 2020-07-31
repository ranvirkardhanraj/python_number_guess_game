import random
import time
userper=[]
computerno=[]
userinput=[]
ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


print("Hello this is Dhanraj and i will tell your guess power")
player=input("Please Enter Your Name:")
print("Thank you ",player)
print("Please Read Game Instruction:")
print("computer give you a random Number from 0,20 you guess which number is that.\n than I tell you how your guess power ")
no_attempt=int(input("Please say that 'How many attempts do you want?'\nAns:-"))
i=0

while i < no_attempt:
    comgive = random.choice(ls)
    computerno.append(comgive)
    print("Enter a Number in between 1 to 20 ")
    userin=int(input("Enter your guess Number:-"))
    if userin == comgive:
        userper.append(100)
        userinput.append(userin)
    elif userin < comgive and userin > comgive - 4:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin < comgive - 4 and userin > comgive - 8:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin < comgive - 8 and userin > comgive - 12:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin < comgive - 12 and userin > comgive - 16:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin > comgive and userin < comgive + 4:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin > comgive - 4 and userin < comgive + 8:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin > comgive - 8 and userin < comgive + 12:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    elif userin > comgive - 12 and userin < comgive + 16:
        if userin > comgive:
            ans=(comgive*100)/userin
            userper.append(ans)
        else:
            ans=(userin*100)/comgive
            userper.append(ans)
        userinput.append(userin)
    else:
        userper.append(0)
    i=i+1

if no_attempt==0:
    print("If you do not want to attempt then")
    print("Game is quit")
    time.sleep(2)
    exit(0)
sum1=0
for total in userper:
    sum1=sum1+total

per=sum1/no_attempt


print("Computer given Numbers:")
print(computerno)
print("you Entered Numbers:")
print(userinput)
print("Your guess power is ",per,"% \n thank you ",player," for playing game \n see you!")
