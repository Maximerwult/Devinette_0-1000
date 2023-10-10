#Par Maxime
# TP2


#on importe le randomiseur pour avoir un choix aléatoire de chiffre
import random


# on définit la fonction de jouer une parite et le nb d'essais
def play_game():
    target_number = random.randint(0, 1000)
    attempts = 0

# on demande au joueur de "guess" un nombre entre 0 et 1000
    while True:
        guess = int(input("Entrez un nombre entre 0 et 1000 : "))
        attempts += 1

# on dit si le nombre est plus grand ou plus petit que celui que l'on cherche
        if guess < target_number:
            print("Le nombre est plus grand.")
        elif guess > target_number:
            print("Le nombre est plus petit.")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre en {attempts} essais.")
            break
    
    return attempts

def main():
    while True:
        attempts = play_game()
        choice = input(" Voulez-vous faire une nouvelle partie ? (Oui/Non) ").lower()

        if choice != 'oui':
            print(" Merci d'avoir joué.")
            break

if __name__ == "__main__":
    main()
