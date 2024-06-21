x = input("camelCase: ").strip()
res = x[0] + ""
for c in x[1:]:
    if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        res = res + '_' +c
    else:
        res += c
print("snake_case: ",res.lower())