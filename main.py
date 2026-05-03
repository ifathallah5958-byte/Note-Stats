from fichier     import lire_fichier, ecrire_resultats
from validation  import valider_notes
from stats       import calculer_stats
from mentions    import grouper_mentions




etudiants, matieres = lire_fichier("notes.csv")
etudiants           = valider_notes(etudiants, matieres)
etudiants, stats    = calculer_stats(etudiants, matieres)
groupes             = grouper_mentions(etudiants)
ecrire_resultats(etudiants, stats, groupes)