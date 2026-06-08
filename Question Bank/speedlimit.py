speed = int(input(" enter the speed: "))

if(speed >= 40):
    print(" Safe ")
elif( speed >40 and speed<=80):
    print(" Normal ")
elif( speed > 80 and speed<=120):
    print(" Warning!!")
else:
    print(" Challan + license suspension ")