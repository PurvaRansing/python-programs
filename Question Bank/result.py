c = int(input("C marks: "))
java = int(input("Java marks: "))
dms = int(input("DBMS marks: "))
html = int(input("HTML marks: "))
react = int(input("React marks: "))

if c < 35 or java < 35 or dms < 35 or html < 35 or react < 35:
    print("Fail")
else:
    total = c + java + dms + html + react
    per = total / 500 * 100

    print("Percentage =", per)

    if per >= 90:
        print("Grade A")
        print("Topper Status")
    elif per >= 75:
        print("Grade B")
    elif per >= 50:
        print("Grade C")
    else:
        print("Pass")