def collatz(num):
    sequence=[num]

    while (num)!=1:
        if (num%2==0):
            num=num/2
        else:
            num=3*num+1
        sequence.append(num)

    return sequence

if __name__=="__main__":

    print(collatz(12))

