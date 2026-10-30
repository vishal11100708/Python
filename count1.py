a= input("Enter the string: ")
count = 0
b = a.split()  
vowels = "AEIOUaeiou"
for word in b:
    if any(vowels in word for vowel in vowels):
        count += 1
print("Words:", b)
print("Number of words containing vowels:", count)
