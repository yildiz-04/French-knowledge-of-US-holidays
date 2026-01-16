# Lecture du fichier CSV
import os
chemin_fichier = os.path.join(os.path.dirname(__file__), "..", "data", "hallothanks.csv")
with open(chemin_fichier, "r") as f:
   
    lignes_brutes = f.readlines()
    print (lignes_brutes)

# Nettoyage des données
donnees_propres = []
for ligne in lignes_brutes:
    ligne_propre = ligne.strip().split(";")
    donnees_propres.append(ligne_propre)

# Séparer l'en-tête et les données
entete = donnees_propres[0]
donnees = []

# Filtrer pour ne garder que les lignes avec des données individuelles
for i in range(1, len(donnees_propres)):
    ligne = donnees_propres[i]
   
    if len(ligne) > 0 and ligne[0] and '-' in ligne[0]:
        donnees.append(ligne)

# Afficher le nombre de données trouvées pour debug
print(f"Nombre de lignes de données trouvées : {len(donnees)}")

# Calculer les scores pour les différentes utilisations
scores = []
for ligne_donnee in donnees:
    # Score /20 est la 26ème colonne, donc index 25
    if len(ligne_donnee) > 25:
        score_str = ligne_donnee[25]
        
        score_str = score_str.strip()
        if score_str.isdigit():
            scores.append(int(score_str))
        else:
            # Essayer de convertir même si ce n'est pas juste des chiffres
            try:
                scores.append(int(float(score_str)))
            except:
                print(f"Score non valide pour {ligne_donnee[0]}: '{score_str}'")

# Afficher les scores trouvés pour debug
print(f"Scores trouvés : {scores}")

# Nombre de répondants
nombre_repondants = len(donnees)

# Calculer l'âge moyen
ages_moyens = []

correspondance_age = {
    '7–11': 9,
    '12–18': 15,
    '12 18': 15,
    '19–25': 22,
    '26–45': 35.5,
    '46–65': 55.5,
    '65+': 70
}

for ligne_donnee in donnees:
    if len(ligne_donnee) > 1:
        groupe_age = ligne_donnee[1]
        if groupe_age in correspondance_age:
            ages_moyens.append(correspondance_age[groupe_age])
        else:
            print(f"Groupe d'âge non reconnu : '{groupe_age}'")

moyenne_age_valeur = 0

if ages_moyens:
    somme_age = 0
    for age in ages_moyens:
        somme_age += age
    moyenne_age_valeur = somme_age / len(ages_moyens)

# Calculer la moyenne des scores
moyenne_score_valeur = 0
if scores:
    somme_score = 0

    for score in scores:
        somme_score += score
    moyenne_score_valeur = somme_score / len(scores)

# Calcule la médiane des scores

mediane_score_valeur = 0
if scores:
    scores_tries = sorted(scores)
    nombre_scores = len(scores_tries)

    if nombre_scores % 2 == 0:
        mediane_score_valeur = (scores_tries[nombre_scores//2 - 1] + scores_tries[nombre_scores//2]) / 2
    else:
        mediane_score_valeur = scores_tries[nombre_scores//2]

# Calculer min et max des scores
score_min = 0
score_max = 0

if scores:
    score_min = scores[0]
    score_max = scores[0]
    for score in scores:
        if score < score_min:
            score_min = score
        if score > score_max:
            score_max = score

# Calculer la distribution hommes/femmes
hommes = 0
femmes = 0
for ligne_donnee in donnees:
    if len(ligne_donnee) > 2:
        genre = ligne_donnee[2]
        if genre == 'M':
            hommes += 1
        elif genre == 'F':
            femmes += 1
total_genre = hommes + femmes

pourcentage_hommes = 0
pourcentage_femmes = 0
if total_genre > 0:
    pourcentage_hommes = (hommes / total_genre) * 100
    pourcentage_femmes = (femmes / total_genre) * 100

# Affichage du menu
print("\n" + "=" * 40)
print("-- Outil d'analyse du sondage Halo --")
print("=" * 40)
print("1. Afficher le nombre total de répondants")
print("2. Calculer la moyenne d'âge")
print("3. Calculer la moyenne des scores")
print("4. Calculer la médiane des scores")
print("5. Calculer les scores maximum et minimum")
print("6. Distribution Hommes/Femmes")
print("7. Quitter")
print()

# Execution du menu
menu = True
while menu:
    choix = input("Entrez votre choix (1 à 7): ")
    
    if choix == "1":
        print(f"\nNombre total de répondants : {nombre_repondants}")
        print("-" * 40)
        
    elif choix == "2":
        print(f"\nMoyenne d'âge (approximative) : {moyenne_age_valeur:.1f} ans")
        print("-" * 40)
        
    elif choix == "3":
        print(f"\nMoyenne des scores : {moyenne_score_valeur:.2f}/20")
        print("-" * 40)
        
    elif choix == "4":
        print(f"\nMédiane des scores : {mediane_score_valeur}/20")
        print("-" * 40)
        
    elif choix == "5":
        print(f"\nScore minimum : {score_min}/20")
        print(f"Score maximum : {score_max}/20")
        print("-" * 40)
        
    elif choix == "6":
        print(f"\nHommes : {hommes} ({pourcentage_hommes:.1f}%)")
        print(f"Femmes : {femmes} ({pourcentage_femmes:.1f}%)")
        print(f"Total : {hommes + femmes}")
        print("-" * 40)
        
    elif choix == "7":
        print("\nAu revoir !")
        menu= False
        
    else:
        print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 7.")
        
