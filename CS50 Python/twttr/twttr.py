x = input("Input: ")
vowels = 'aeiouAEIOU'
y = "".join([char for char in x if char not in vowels])
print("Output: ",y)