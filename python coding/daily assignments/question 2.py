# count many times a appers using enumerate
s=str(input('enter a word'))
count=0
for index,char in enumerate(s):
    if char == "a":
        count+=1
print("count of 'a':",count)