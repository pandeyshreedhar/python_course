w="welcome"
#print(w.find('e'))
#print(w.find('e'2))# result -1
#print(w.find('a'))
print(w.index('c',2))
#print(w.index('a')) #error not found

s="welcome12345"
print(s.isalpha()) # check all alphabetics only
print(s.isdigit())#  check all digit only

q="welcome"
r="12345"
print(q.isalpha())#true
print(r.isdigit()) #true
print(r.isalpha()) #false

x="welcome123"
print(x.isalnum()) #true