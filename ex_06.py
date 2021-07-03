s = 'Marina Pavlova'

print(s[-5:])

print(s[:int(len(s)/3)])

print(s.count('a'))

print('b' in s)

lst = s.split()
print(lst)

lst.reverse()
print(lst)

last_name = lst[0].upper()
print(last_name)

name = lst[1]
middle = int(len(name)/2)
if len(name) % 2 == 0:
    nameNew = name[:middle-1] + name[middle+1:]
else:
    nameNew = name[:middle] + name[middle + 1:]
print(nameNew)

final_str = nameNew + ' ' + last_name
print(final_str)
