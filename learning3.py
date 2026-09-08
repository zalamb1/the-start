w=int(input("what is your weight?: "))
t=input("(k)g or (L)bs: ")
if (t.upper()=="L"):
    w=w/2.2
    print("weight in kg: ", w)
elif( t.upper()=="k"):
    w=w*2.2
    print ("weight in Lbs: ", w)