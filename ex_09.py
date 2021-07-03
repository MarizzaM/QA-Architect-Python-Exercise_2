import statistics

l = [8, 1000, -3, 2, 5]

print('**********')
print(sum(l))

print('**********')
print(max(l))

print('**********')
print(min(l))

print('**********')
print(statistics.mean(l))

print('**********')
del l[int(len(l) / 2)]
print(l)

print('**********')
l.sort()
print(l)

print('**********')
i = 1
while i <= 5:
    print(l)
    i += 1

print('**********')
del l[0]
print(l)

print('**********')
l = [8, 1000, -3, 2, 5]
l_final = []
[l_final.append(x) for x in l if x < statistics.mean(l)]
print(l_final)
