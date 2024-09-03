import random
import string
import nltk
from nltk.corpus import words

# Télécharger les mots si nécessaire
nltk.download('words')

word_list = words.words()

# Fonction pour générer un mot ayant du sens
def generer_mot_sensé():
    while True:
        # Générer une longueur de mot aléatoire
        longueur_mot = random.randint(3, 10)
        mot_aleatoire = ''.join(random.choice(string.ascii_lowercase) for _ in range(longueur_mot))
        
        # Vérifier si le mot généré existe dans la liste des mots
        if mot_aleatoire in word_list:
            return mot_aleatoire

print("Welcome to HANGMAN GAME! \nYou will be guessing a word, you only have 4 chances! GOOD LUCK!")

# Générer et afficher un mot ayant du sens
word = generer_mot_sensé()
l = len(word)
mot_masqué = ['-'] * l
chances = 4

while chances > 0 and ''.join(mot_masqué) != word:
    letter = input(f"Try to guess the word, give your letter: {''.join(mot_masqué)} ").lower()
    
    # Assurez-vous que l'utilisateur ne peut entrer qu'une seule lettre
    if len(letter) != 1 or letter not in string.ascii_lowercase:
        print("Please enter a single valid letter.")
        continue
    
    if letter in word:
        # Révéler les lettres correctes dans le mot masqué
        for i in range(l):
            if word[i] == letter:
                mot_masqué[i] = letter
        print("Correct!")
    else:
        chances -= 1
        print(f"Wrong! You have {chances} chances left.")
    
    # Affiche le mot masqué après chaque essai
    print(f"Current guess: {''.join(mot_masqué)}")

if ''.join(mot_masqué) == word:
    print("Congratulations! You have successfully guessed the word!")
else:
    print(f"GAME OVER :( \nSorry, you have failed to guess the word. The correct word was: {word}")
