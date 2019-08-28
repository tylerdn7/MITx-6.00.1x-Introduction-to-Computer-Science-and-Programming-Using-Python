s = 'abcbcd'
current = ''
longest = ''
n = 0

for i in range(len(s)):
    if s[i] >= s[i-1]:
        current += s[i]
    else:
        current = s[i]
    if len(current) > n:
        longest = current
        n = len(current)

print('Longest substring in alphabetical order is:',longest)
