import re
name = "Институт точной механики оптики"
# name = "Российский государственный университет нефти газа"

#Вариант решения через re.findall
print("".join(re.findall(r"\b\w{1}",name)).upper())
#Вариант решения через re.sub

t = re.sub(r" ",r"", re.sub(r"\b(\w)*\b",r"\1",name)).upper()
print(t)