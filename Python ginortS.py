s = input()
l = []
u = []
o = []
e = []


for i in s:
    if i >= chr(97) and i <= chr(122):
        l.append(i)
    elif i >= chr(65) and i <= chr(90):
        u.append(i)
    elif i >= chr(48) and i <= chr(57):
        if ord(i) % 2 == 1:
         o.append(i)
        if ord(i) % 2 == 0:
         e.append(i)               


print(''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e)))
