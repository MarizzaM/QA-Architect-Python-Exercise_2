matrix = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]
min_el = 0
for i in range(len(matrix)):
    rows = [oneList[i] for oneList in matrix if i < len(oneList)]
    for j in rows:
        if j < min_el:
            min_el = j
print(min_el)
