def valider_notes(etudiants, matieres):
    for matiere in matieres:
        notes_valides = []
        for e in etudiants:
            if 0 <= e[matiere] <= 20:
                notes_valides.append(e[matiere])

        if len(notes_valides) == 0:
            moyenne = 10
        else:
            moyenne = sum(notes_valides) / len(notes_valides)

        for e in etudiants:
            if not (0 <= e[matiere] <= 20):
                print(f"{e['nom']} a une note invalide " f"en {matiere} ({e[matiere]}) "  f"→ remplacée par {round(moyenne, 2)}")
                e[matiere] = moyenne
    return etudiants
