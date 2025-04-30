def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split() # creates an array
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:]) # capitalizes the first letter of every word from the second item in the array and on

s = "hello_split-this"
s = s.replace("-", " ").replace("_", " ")
s = s.split()
print(s)
for i in s[1:]:
    print(i)


