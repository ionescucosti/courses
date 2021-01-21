# 256 Tema 22
# for
# PF - 06/10/2017 v3

"""
Scrieti un program care va numara cate caractere are un sir dat de utilizator
Aceata numarare sa se realizeze cu ajutorul unui for. La final afisati rezultatul
Similar sa numere cate cuvinte sunt in text
""" #
x=input("enter: ")

count = 0
words=0
for i in x:
    count+=1
print(count)

for i in x.split():
    words+=1
print(words)

