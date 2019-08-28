s = 'boobgobobozobobbobbhboboboobbobbo'
bob = 'bob'
count = 0
n = len(s)
for i in range(len(s)):
    if s[i:i+3] == bob:
        count += 1
print('Number of times bob occurs is:',count)
