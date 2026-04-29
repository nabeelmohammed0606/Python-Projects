phrase = input("Please enter the phrase that you want to reverse: ")

def reverse(x):
    return x[::-1]

return_text = reverse(f"{phrase}")
print(return_text)
