"""
de la tastatura se citesc patru cuvinte, fiecare cuvant fiind citit intr-o singura variabila, un cuvant va fi format din minim 3 caractere.
Elaborati un program care va forma un cuvant nou, in felul urmator :din primul cuvant va adauga primele 2 caractere,din al doilea cuvant va
adauga primul caracter ,primele trei caractere din cuvantul al treilea si n/2 caractere din cuvantul patru(n-lungimea cuvantului). La ecran
se vor afisa cuvintele citite cat si cuvantul format.
"""
a=input("introdu primul cuvant:")
b=input("introdu al doilea cuvant:")
c=input("introdu al treilea cuvant:")
d=input("introdu al patrulea cuvant:")
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print("Error")
l1=a[:2]
l2=b[0]
l3=c[:3]
l4=d[:(len(d)//2)]
print("Cuvintele: ",a,b,c,d,sep="  ")
print("Cuvantul format",l1+l2+l3+l4)