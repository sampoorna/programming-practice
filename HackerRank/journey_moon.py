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
        to_delete = astros[b]
        for i in countries[astros[b]]:
            if i not in countries[astros[a]]:
                countries[astros[a]].append(i)
            astros[i] = astros[a]
        del countries[to_delete]
    elif b in astros and a not in astros:
        astros[a] = astros[b]
        countries[astros[b]].append(a)
    elif a in astros and b not in astros:
        astros[b] = astros[a]
        countries[astros[a]].append(b)

singles = len(set(range(N)) - set(astros.keys()))
#print countries

result = 0
# Compute the final result using the inputs from above

for i in countries:
    for j in range(i+1, country):
        if j not in countries:
            continue
        #print i, j
        result += len(countries[i]) * len(countries[j])
if singles > 0: 
    print result + singles*(len(astros.keys())) + ((singles * (singles - 1))/2)
else:
    print result