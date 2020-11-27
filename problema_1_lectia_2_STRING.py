"""
Se citeste un cuvant si o litera. Sa se afiseze cuvantul alcatuit prin inlocuirea fiecarui caracter al cuvantului cu litera data.
"""
c=input("introdu cuvantul: ")
l=input("introdu litera: ")
for i in range(len(c)):
    print(c[:i]+l+c[i+1:])