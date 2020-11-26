"""
De la tastatura se citeste un sir de caractere.Elaborati un program care va determina:
A)numarul de majuscule din sir;
B)numarul de cifre din sir;
C)numarul de caractere speciale(paranteze,operatori aritmetici) din sir;
"""
s=input("introdu sirul: ")
nrm=0
nr=0
ns=0
for i in s:
    if ord(i) in range(65,91):
        nrm+=1
print(nrm)
for i in s:
    if ord(i) in range(97,123):
        nr+=1
print(nr)
for i in s:
    if ord(i) in range(33,42):
        ns+=1
print(ns) 