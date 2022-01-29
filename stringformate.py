txt1="welcome to {fname} {lname}".format(fname="shreedhar", lname="channel")
print(txt1)
txt2="welcome to {1} {0}".format("shreedhar",100)
print(txt2)
txt3="welcome to {a} {b}".format(a="shreedhar",b=10)
print(txt3)
txt4="welcome to {b:10} to {a}".format(a=30,b=40) # take 8 space
print(txt4)
txt5="welcome to {b:^10} to {a}".format(a=30,b=40) # take 8 space
print(txt5)
txt6="welcome to {b:>10} to {a}".format(a=30,b=40) # take 8 space
print(txt6)

#< =10 -------- left space
#^ = ----10---- center
#> = --------10 right