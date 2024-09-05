

def transfer():
    while True:
        c1 = input("Type 'done' or enter the first number: ")
        
        if c1 == "done":
            print("Goodbye!")
            break
        else: x1 = int(c1)

        x2 = int(input("Enter the second number: "))
        trans = int(input("Enter the amount: "))

        if trans < x1:
            sum1 = x1 - trans
            sum2 = x2 + trans
        else:
            sum1 = 0
            sum2 = x1 + x2

        print(sum1, sum2)
        continue

def change():
    while True:
        a = input("Type 'done' or enter the amount: ")
        if a == "done":
            print("Goodbye!")
            break
        else:
            amount = 1000 - int(a)

        if amount >= 500 :
            c1 = amount // 500
            amount = amount - 500 * c1
            s1 = "500, " + str(c1) + ";"
        else:
            s1 =  ""
        if amount >= 100:
            c2 = amount // 100
            amount = amount - 100 * c2
            s2 = "100, " + str(c2) + ";"
        else:
            s2 = ""
        if amount >= 50:
            c3 = amount // 50
            amount = amount - 50 * c3
            s3 = "50, " + str(c3) + ";"
        else:
            s3 = ""
        if amount >= 10:
            c4 = amount // 10
            amount = amount - 10 * c4
            s4 = "10, " + str(c4) + ";"
        else:
            s4 = ""
        if amount >= 5:
            c5 = amount // 5
            amount = amount - 5 * c5
            s5 = "5, " + str(c5) + ";"
        else:
            s5 = ""
        if amount >= 1:
            c6 = amount // 1
            amount = amount - 1 * c6
            s6 = "1, " + str(c6)
        else:
            s6 = ""

        print(s1, s2, s3, s4, s5, s6)
        continue

def main():
    ProgrammeChoice = input("Choose your programme: 'transfer' or 'change': ")
    ProgrammeChoice = ProgrammeChoice.lower()
    if ProgrammeChoice == "transfer":
        transfer()
    elif ProgrammeChoice == "change":
        change()
    else:
        print("Invalid input")

main()