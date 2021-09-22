import datetime

import xlrd as xlrd

colloscope = xlrd.open_workbook('/home/Pseud3mys/DjangoApp/polls/Scripts/colloscope.xls')
sheet = colloscope.sheet_by_index(1)

colors = {
 'SI': "#D5C404",
 'Maths': "#0415D5",
 'Phy': "#C404D5",
 'Ang': "#D5047E",
 'Fr': "#7DD504",
 'Red': "#D50415",
}
def mat2color(matiere):
    if "MATH" in matiere.upper():
        return colors['Maths']
    if "PHY" in matiere.upper():
        return colors['Phy']
    if "SI" in matiere.upper():
        return colors['SI']
    if "FR" in matiere.upper():
        return colors['Fr']
    if "ANG" in matiere.upper():
        return colors['Ang']

def get_colles(groupe):
    now = datetime.datetime.now()
    row_index = 0
    date = datetime.datetime(2000, 1, 1)
    # trouver la colonne à jour
    while date <= now:
        row_index += 1
        _date = sheet.cell_value(1, row_index)
        _type = sheet.cell_type(1, row_index)
        # on saute les cases vides
        if _type != xlrd.sheet.XL_CELL_DATE:
            continue
        # on cherche la colonne de la semaine
        date = datetime.datetime(*xlrd.xldate.xldate_as_tuple(_date, colloscope.datemode))
    row_index -= 1
    col_index = -1
    colles = []
    # cherche les colles pour le groupe donné
    for groupeCell in sheet.col(row_index):
        col_index += 1
        if col_index <= 2:
            continue
        if groupeCell.ctype != xlrd.sheet.XL_CELL_NUMBER:
            continue
        if int(groupeCell.value) == groupe:
            prof = sheet.cell_value(col_index, 1)
            jour = sheet.cell_value(col_index, 2)
            salle = sheet.cell_value(col_index, 3)
            if type(salle) == float:
                salle = str(int(salle))
            # matiere (bete et mechant)
            matiere = "matiere"
            if col_index <= 11:
                matiere = "Maths"
            elif col_index <= 20:
                matiere = "SI"
            elif col_index <= 23:
                matiere = "Francais"
            elif col_index <= 32:
                matiere = "Physique"
            elif col_index <= 42:
                matiere = "Anglais"
            color = mat2color(matiere)
            colles.append((matiere, jour, prof, salle, color))
    # trie par jour... (Jeudi avant tt en ordre alphabetique)
    colles.sort(key=lambda x: x[1])
    if "Jeudi" in colles[0][1]:
        colles += [colles.pop(0)]
        if "Vendredi" in colles[-2][1]:
            colles += [colles.pop(-2)]
    return colles
