# 📊 Système de Gestion des Notes

Un programme Python permettant de gérer, valider et analyser les notes des étudiants, avec génération automatique des mentions et des statistiques.

---

## 📁 Structure du Projet

```
├── main.py          # Point d'entrée principal du programme
├── fichier.py       # Lecture et écriture des fichiers (CSV/TXT)
├── mentions.py      # Calcul et attribution des mentions
├── stats.py         # Calcul des statistiques (moyenne, min, max...)
├── validation.py    # Validation et vérification des données
├── notes.csv        # Fichier de données des notes (entrée)
└── resultats.txt    # Fichier de résultats générés (sortie)
```

---

## ⚙️ Fonctionnalités

- 📥 **Lecture des notes** depuis un fichier CSV
- ✅ **Validation des données** (format, plage de valeurs, cohérence)
- 🏅 **Calcul des mentions** automatique selon les moyennes
- 📈 **Statistiques** : moyenne générale, note minimale, note maximale, taux de réussite
- 📄 **Export des résultats** dans un fichier texte

---

## 🏅 Système de Mentions

| Moyenne          | Mention        |
|-----------------|----------------|
| 16.00 – 20.00   | Très Bien      |
| 14.00 – 15.99   | Bien           |
| 12.00 – 13.99   | Assez Bien     |
| 10.00 – 11.99   | Passable       |
| < 10.00         | Insuffisant    |

---

## 🚀 Utilisation

### Prérequis

- Python 3.x installé

### Lancer le programme

```bash
python main.py
```

### Format du fichier `notes.csv`

```csv
Nom,Prenom,Note1,Note2,Note3
Fathallah,Ismail,15,18,14
Dupont,Marie,12,10,16
```

### Résultats

Les résultats sont générés automatiquement dans `resultats.txt` avec les moyennes et les mentions de chaque étudiant.

---

## 📦 Technologies utilisées

- **Python 3** — langage principal
- **CSV** — format de données d'entrée
- **Fichiers texte (.txt)** — format de sortie des résultats

---

## 👨‍💻 Auteur

**Ismail Fathallah**  
Étudiant en Réseaux, Cybersécurité et Intelligence Artificielle  
École Supérieure de Technologie (EST) – Kelaa des Sraghna