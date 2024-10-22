print("-----Calculator 1488-----")
first = int(input("First number: "))
znak = input("+-*/=><? ")
if znak == "=":
    pass
else:
    twice = int(input("Twice number: "))
Answer = 0
if znak == "+":
    Answer = first + twice
    print("Answer is: ", Answer)
elif znak == "-":
    Answer = first - twice
    print("Answer is: ", Answer)
elif znak == "*":
    Answer = first * twice
    print("Answer is: ", Answer)
elif znak == "/":
    if twice == 0:
        print("You cannot do it by 0!")
    else:
        Answer = first / twice
        print("Answer is: ", int(Answer))
elif znak == "=":
    Answer = first * 2
    print("Answer is: ", Answer)
elif znak == ">":
    Answer = first > twice
    print("Answer is: ", bool(Answer))
elif znak == "<":
    Answer = first < twice
    print("Answer is: ", bool(Answer))