colors = {
 'SI': "#D5C404",
 'Maths': "#0415D5",
 'Phy': "#C404D5",
 'Chi': "#C404D5",
 'Ang': "#D5047E",
 'Fr': "#7DD504",
 'Red': "#D50415",
}


def mat2color(matiere):
    if "MATH" in matiere.upper():
        return colors['Maths']
    if "PHY" in matiere.upper():
        return colors['Phy']
    if "CHI" in matiere.upper():
        return colors['Chi']
    if "SI" in matiere.upper():
        return colors['SI']
    if "FR" in matiere.upper():
        return colors['Fr']
    if "ANG" in matiere.upper():
        return colors['Ang']


def text2mat(text):
    if "MATH" in text.upper():
        return "Maths"
    if "PHY" in text.upper():
        return "Physique"
    if "CHI" in text.upper():
        return "Chimie"
    if "SI" in text.upper():
        return "Science de l'ingénieur"
    if "FR" in text.upper():
        return "Francais"
    if "ANG" in text.upper():
        return "Anglais"
    else:
        False


def CleanStr(str):
    clean_str = ""
    add = True
    for a in str:
        if a == "<":
            add = False
        if add:
            clean_str += a
        if a == ">":
            add = True
            clean_str += " "
    return clean_str


day2num = {
    "Lundi":	0,
    "Mardi":	1,
    "Mercredi":	2,
    "Jeudi":	3,
    "Vendredi":	4,
    "Samedi":	5,
    "Dimanche":	6,
}

num2day = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]