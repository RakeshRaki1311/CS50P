import inflect
p = inflect.engine()

text = ["Adieu",'adieu']
while True:
    try:
        n = input("name: ")
    except EOFError:
        print()
        break
    text.append(n)
text[2] = "to " + text[2]
if len(text) == 3:
    new_text = p.join(text,conj = '')
elif len(text) == 4:
    new_text = p.join(text,final_sep= '')
else:
    new_text = p.join(text)
print(new_text)