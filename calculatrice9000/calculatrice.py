# On utilise la fontion --def calculatrice()--. cette fonction définit la fonction calculatrice.
def calculatrice():
    #  Nous devons créer une liste vide. Cette liste est utilisée pour stocker l'historique des calculs effectués par l'utilisateur dans la calculatrice.
    historique = []
    # On débute un bloc nommée try pour gérer les erreurs potentielles.
    while True:
        try:
        # On demande à l'utilisateur d'entrer deux nombres
        # La fonction float est utilisée pour convertir l'entrée en un nombre décimal.
            nombre1 = float(input("Cher utilisateur, le premier chiffre/nombre : "))
        # On demande à l'utilisateur d'entrer le deuxième nombre de manière similaire au premier.
            nombre2 = float(input("Cher utilisateur, le deuxième chiffre/nombre : "))
        # On demande à l'utilisateur d'entrer l'opération souhaitée
            operation = input("Cher utilisateur, l'opération (+, -, *, /) : ")
        # Nous demandons une série de conditions pour déterminer l'opération à effectuer en fonction de ce qui a été entré par l'utilisateur.
        # Effectuer le calcul en fonction de l'opération
            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
            # Gérer la division par zéro : gestion spéciale pour la division par zéro.Nous Vérifiions également si le deuxième nombre est égal à zéro.
                if nombre2 == 0:
                # L'instruction raise est utilisée pour déclencher une exception de manière explicite.
                # Elle permet au programmeur de signaler qu'une condition exceptionnelle s'est produite.
                # Lorsqu'une exception est levée, le flux normal du programme est interrompu,
                # et le contrôle est transféré au bloc d'instructions associé à la gestion de cette exception.
                # raise ValueError("Erreur : Division par zéro n'est pas autorisée.") : Si c'est le cas, lève une exception ValueError avec le message d'erreur approprié.
                    raise ValueError("Erreur d'opération : La Division par zéro n'existe pas !.")
                resultat = nombre1 / nombre2
            else:
                raise ValueError("Erreur : Opération non valide.")
             # Ajouter le calcul à l'historique gràce à (append).
            historique.append(f"{nombre1} {operation} {nombre2} = {resultat}")

        # Afficher le résultat
            print(f"Résultat : {resultat}")
        # Demander à l'utilisateur s'il veut effacer l'historique
        #.lower()est utilisée sur des chaînes de caractères pour convertir tous les caractères de la chaîne en minuscules.
            effacer_historique = input("Voulez-vous effacer l'historique? (Oui/Non) : ").lower()
            if effacer_historique == 'oui':
                historique = []  # Effacer l'historique

    # Capture une exception de type ValueError et affiche le message d'erreur spécifique.
        except ValueError as e:
            print(f"Erreur : {e}")
    # Capture une exception de type Exception (toutes les autres exceptions) et affiche un message générique pour toute autre erreur inattendue.
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

         # Afficher l'historique
        print("Liste des calculs effectués :")
        for calcul in historique:
            print(calcul)

# Appelle la fonction calculatrice pour exécuter le programme.
calculatrice()

# En résumé, ce programme crée une calculatrice simple qui prend en compte la possibilité d'erreurs,
# notamment la division par zéro et des opérations non valides, en affichant des messages d'erreur appropriés.