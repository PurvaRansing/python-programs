n = int(input("Enter number of employees: "))

for i in range(n):
    sal = float(input("Enter salary: "))

    bonus = sal * 0.10
    tax = sal * 0.05

    final = sal + bonus - tax

    print("Bonus =", bonus)
    print("Tax =", tax)
    print("Final Salary =", final)