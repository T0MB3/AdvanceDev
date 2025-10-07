from create_movie import movie

def remove_movie():
    titre = input("Titre du film à supprimer : ")
    if titre in movie:
        movie.remove(titre)
        print(f"Le film '{titre}' a été supprimé.")
    else:
        print(f"Le film '{titre}' n'existe pas dans la liste.")