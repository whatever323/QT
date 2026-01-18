#made by nedry yousri



from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
from pickle import dump, load

index = 0
t = array([""] * 50)   
path = "eleve.dat"

# reset file
with open(path, "wb"):
    pass


def ajout():
    global index, t, path

    mat = form.mat.text().strip()
    prenom = form.prenom.text().strip()
    nom = form.nom.text().strip()
    moy = form.moy.text().strip()

    # Sexe
    if form.mm.isChecked():
        sexe = "M"
    elif form.ff.isChecked():
        sexe = "F"
    else:
        sexe = ""

    # Validations
    if (
        mat == "" or prenom == "" or nom == "" or moy == "" or
        not moy.isdigit() or sexe == ""
    ):
        form.res.setText("Erreur ! Vérifiez vos données")
        return

    # Check if matricule exists
    if existe(mat, t):
        form.res.setText("Erreur ! La matricule existe déjà")
        return

    # Save matricule into array
    t[index] = mat
    index += 1

    # Create dictionary
    e = {
        "matricule": mat,
        "prenom": prenom,
        "nom": nom,
        "sexe": sexe,
        "moyenne": int(moy)
    }

    # Save to file
    with open(path, "ab") as f:
        dump(e, f)

    form.res.setText("Ajout réussi")
    afficher()


def existe(mat, t):
    global index
    for i in range(index):
        if mat == t[i]:
            return True
    return False


def afficher():
    form.res.setText("Affichage dans la console")
    print("\n--- LISTE ÉTUDIANTS ---")
    
    with open(path, "rb") as f:
        while True:
            try:
                e = load(f)
                print(e)
            except EOFError:
                break


def effacer():
    form.mat.clear()
    form.prenom.clear()
    form.nom.clear()
    form.mm.setChecked(False)
    form.ff.setChecked(False)
    form.moy.clear()
    form.res.setText("")


def fermer():
    form.close()


app = QApplication([])
form = loadUi("ajout eleve.ui")
form.show()

form.ajout.clicked.connect(ajout)
form.eff.clicked.connect(effacer)
form.fer.clicked.connect(fermer)

app.exec_()
