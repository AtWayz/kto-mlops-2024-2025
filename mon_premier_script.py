#message = "C'est (pas) mon premier script !!!"
#print(message)

#je_change_de_type = 1
#print(type(je_change_de_type))
#je_change_de_type = "coucou"
#print(type(je_change_de_type))

#def saluer(nom: str) -> str:
#    return "Bonjour " + nom

#print(saluer("Alice"))  # Affiche : Bonjour Alice


# Exercice d'évaluation
import unittest
from typing import List

def count_names_with_more_than_seven_letters(names: List[str], seuil: int) -> int:
    """
    Compte le nombre de prénoms ayant plus de lettres qu'un seuil spécifié.

    Paramètres :
    names (List[str]) : Une liste de prénoms à vérifier.
    seuil (int) : Le nombre de lettres à comparer pour chaque prénom.

    Retour :
    int : Le nombre de prénoms ayant plus de lettres que le seuil spécifié.
    """
    count = 0
    for name in names:
        if len(name) > seuil:
            count += 1
    return count

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        test_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_with_more_than_seven_letters(test_names, seuil=7)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
