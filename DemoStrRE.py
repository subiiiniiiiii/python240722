#DemoStrRe.py

data = "<< spam and ham >>>"

result = data.strip("<> ")
print(data)
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())

#정규 표현식
import re

result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

result = re.search("apple","this is apple")
print(result)
print(result.group())

result = re.search("\d{4}","올해는 2024년입니다.")
print(result)
print(result.group())
