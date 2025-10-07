from movies.create_movie import add_movie, remove_movie
from movies.create_movie import movie

while True:
    print("\n===== MENU =====")
    print("1. Ajouter un film")
    print("2. Supprimer un film")
    print("3. Noter un film")
    print("4. Trier par note")
    print("5. Lister les films")
    print("Q. Quitter")
    print("================")

    choix = input("Votre choix : ").strip().upper()

    match choix:
        case "1":
            add_movie()
        case "2":
            remove_movie()
        case "3":
            print("NOTE")
        case "4":
            print("TRIER NOTE")
        case "5":
            for film in movie:
                print(film)
        case "Q":
            print("Au revoir !")
            break
        case _:
            print("Choix invalide. Veuillez réessayer.")
