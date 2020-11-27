"""
Un sir de caractere introdus de la tastura trebuie sa reprezinte numele si prenumele unei persoane, initialele scrise cu majuscule, celelalte
caractere fiind litere mici. Stabiliti daca sirul dat este un nume corect de persoana
"""
s=input("Introdu prenumele si numele tau: ")
s1=s.split()
if((s1[0]==s1[0].title())and(s1[1]==s1[1].title())):
    print("Corecte")
else:
    print("Gresit")