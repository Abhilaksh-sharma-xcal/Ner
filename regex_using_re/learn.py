import re

text = "Hello World 123"
result = re.search(r"World", text)
# print(result)  # inp : text = "Hello World 123", out :<re.Match object; span=(6, 11), match='World'>


numbers = re.findall(r"\d", text)
print(numbers)  # ['5', '3']


# words = re.findall(r"\w+", text)
# print(words) 
# input text = "I have 5 cats and 3 dogs. @hr", out: ['I', 'have', '5', 'cats', 'and', '3', 'dogs', 'hr']

text = """I have 5 cats and 3 dogs.   
@hr"""
spaces = re.findall(r"\s", text)
print(spaces) # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n'] 


x = re.findall(r"https?://", "Visit http://example.com or https://example.com")
y = re.findall(r"hii (abhilaksh|abhi)", "hii abhi how are you? also hii abhilaksh") # ['abhilaksh', 'abhi']
print(y)
y = re.findall(r"(laksh|abhi)", "hii abhi how are you? also hii abhilaksh") # ['abhi', 'abhi', 'laksh']
print(y)
y = re.findall(r"hii [abhi][abhilaksh]?", "hii abhi how are you?") #['hii ab']
y = re.findall(r"hii (abhi(laksh)?)", "hii abhilaksh") # [('abhilaksh', 'laksh')]
print(x)
print(y)