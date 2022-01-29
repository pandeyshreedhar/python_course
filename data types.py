a=5 # intger no
print(a,type(a))
a=5.5 #float no
print(a,type(a))
a=2+5j #complex no
print(a,type(a))

s='hello@123'
print(s,type(s))
a='''
hello 
welcome 
shreedhar pandey
'''
print(a, type(a))
b='10'
print(b, type(b))

#list
l=[10,'ws',20,5.5]
print(l,type(l))
l[2]=1 #list value change in 3 no 0,1,2,3.... 20 is change to no 1 replace
print(l,type(l))

#tuple
t=(10,20,'hello',10+2j)
print(t, type(t))
t=(10)
print(t, type(t))
t=('hello')
print(t, type(t))
t=(10+2j)
print(t, type(t))

#Dictonary
d={'course_name':'python',
   'course_duration':'2 months'
   }
print(d,type(d))

#set
my_set={1,2,3}
print(my_set, type(my_set))

s={10,20,30,5,10}
print(s, type(s))