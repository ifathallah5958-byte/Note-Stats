def calculer_stats(etudiants, matieres):

    # moyenne de chaque etudiant
    for e in etudiants:
        total = 0
        for m in matieres:
            total += e[m]
        e['moyenne'] = total / len(matieres)
        
    stats = {}
    for matiere in matieres:
        notes = []
        for e in etudiants:
            notes.append(e[matiere])

        stats[matiere] = {
            'moyenne': sum(notes) / len(notes),
            'min':     min(notes),
            'max':     max(notes)
        }

    return etudiants, stats
