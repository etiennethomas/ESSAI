from random import randint

a="Hello, World"
print(type(a))

a=4+7
print(type(a))

#1+[2+3]

def entier_double(x:int) -> int:
    return 2*x

resultat=entier_double(3)
print(resultat)
resultat=entier_double("a")
print(resultat)

def tri_selection(tableau):
    tableau_trie = tableau[:]
    longueur = len(tableau_trie)
    for position in range(0, longueur):
        for j in range(position+1, longueur):
            if tableau_trie[j] < tableau_trie[position]:
                tableau_trie[position], tableau_trie[j] = tableau_trie[j], tableau_trie[position]
    return tableau_trie

def test_tri_selection(liste):
    for i in range(len(liste)-1):
        assert liste[i] <= liste[i+1]
        
"""def test_tri_selection():
    def est_triee(liste):
        for i in range(len(liste)-1):
            assert liste[i] <= liste[i+1]

    for i in range(100):
        # on génère des listes de longueur aléatoires allant de 1 à 50
        tableau = [randint(0, 100) for i in range(randint(1, 50))]
        #print(tableau)
        tableau_trie = tri_selection(tableau)
        #print(tableau_trie)
        est_triee(tableau_trie)"""


        
test_tri_selection(tri_selection([5,2,1,3,4]))
#test_tri_selection()
