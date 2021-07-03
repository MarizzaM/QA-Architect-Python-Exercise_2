s = 'Hello World!'

i_first = s.find('o')+1
i_last = s.rfind('o')+1
print(i_first + i_last)

print(s[:i_first-1])

print(s[i_last:])
