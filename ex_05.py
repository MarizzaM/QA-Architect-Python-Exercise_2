words = ['world of coding', 'pen', 'python', 'hello']

for word in words:
    if len(word) < 4:
        break
    else:
        print(word.upper())
