def get_mention(moyenne):
    if moyenne >= 16:
        return "Excellent"
    elif moyenne >= 14:
        return "Tres bien"
    elif moyenne >= 12:
        return "Bien"
    elif moyenne >= 10:
        return "Assez bien"
    else:
        return "Faible"
    
def grouper_mentions(etudiants):
    groupes = {
        "Excellent":  [],
        "Tres bien":  [],
        "Bien":       [],
        "Assez bien": [],
        "Faible":     []
    }

    for e in etudiants:
        mention = get_mention(e['moyenne'])
        e['mention'] = mention
        groupes[mention].append(e['nom'])

    return groupes
