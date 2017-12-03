# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())
countries = {}
country = 0
astros = {}
 
for i in xrange(l):
    a, b = map(int,raw_input().split())
    # Store a and b in an appropriate data structure
    if a not in astros and b not in astros:
        countries[country] = [a, b]
        astros[a] = country
        astros[b] = country
        country += 1
    elif a in astros and b in astros and astros[a] != astros[b]:
        s1 = set(countries[astros[a]])
        s2 = set(countries[astros[b]])
        s = s1.union(s2)
        countries[astros[a]] = list(s)
        del countries[astros[b]]
        for i in s2:
            astros[i] = astros[a]
    elif b in astros and a not in astros:
        astros[a] = astros[b]
        countries[astros[b]].append(a)
    elif a in astros and b not in astros:
        astros[b] = astros[a]
        countries[astros[a]].append(b)
for n in range(N):
    if n not in astros:
        astros[n] = country
        countries[country] = [n]
        country += 1
print countries

result = 0
# Compute the final result using the inputs from above

for i in countries:
    for j in range(i+1, country):
        if j not in countries:
            continue
        #print i, j
        result += len(countries[i]) * len(countries[j])
    
print result