def lire_fichier(nom_fichier):
    etudiants = []
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
        matieres = lignes[0].strip().split(',')[1:]  # sans "Nom"
        for ligne in lignes[1:]:
            valeurs = ligne.strip().split(',')
            etudiant = {
                "nom":          valeurs[0],
                matieres[0]: float(valeurs[1]),
                matieres[1]: float(valeurs[2]),
                matieres[2]: float(valeurs[3]),
                matieres[3]: float(valeurs[4])
            }
            etudiants.append(etudiant)
    return etudiants, matieres

def ecrire_resultats(etudiants, stats, groupes):
    with open("resultats.txt", 'w') as f:

        # stats par matiere
        f.write("===== STATISTIQUES =====\n")
        for matiere, s in stats.items():
            f.write(f"\n{matiere}\n")
            f.write(f"  Moyenne : {round(s['moyenne'], 2)}\n")
            f.write(f"  Minimum : {round(s['min'], 2)}\n")
            f.write(f"  Maximum : {round(s['max'], 2)}\n")

        # classement
        f.write("\n===== CLASSEMENT =====\n")
        classement = sorted(etudiants,
                            key=lambda e: e['moyenne'],
                            reverse=True)
        for i, e in enumerate(classement, 1):
            f.write(f"{i}. {e['nom']:<12} "
            f"Moyenne: {round(e['moyenne'], 2)}  "                    
            f"Mention: {e['mention']}\n")

        # groupes
        f.write("\n===== GROUPES =====\n")
        for mention, liste in groupes.items():
            noms = ", ".join(liste) if liste else "Aucun"
            f.write(f"{mention} : {noms}\n")

    print(" resultats.txt generer!")
