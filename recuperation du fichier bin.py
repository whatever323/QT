from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
from pickle import*


def affiche():
    form.tabw.setRowCount(0)
    f=open("eleve.dat","rb")
    k=0
    test=True
    while(test):
      try:
          e=load(f)
          form.tabw.insertRow(k)
          form.tabw.setItem(k,0,QTableWidgetItem(e["matricule"]))
          form.tabw.setItem(k,1,QTableWidgetItem(str(e["nom"])))
          form.tabw.setItem(k,2,QTableWidgetItem(str(e["prenom"])))
          form.tabw.setItem(k,3,QTableWidgetItem(str(e["date"])))
          form.tabw.setItem(k,4,QTableWidgetItem(str(e["sexe"])))
          form.tabw.setItem(k,5,QTableWidgetItem(str(e["moy"])))
          k=k+1
      except:
          test=False
    f.close()
    
def fermer():
    form.close()

app = QApplication([])
form = loadUi("/home/mohamed/Bac2026/qt/rec_fich_bin.ui")
form.show()
form.bt1.clicked.connect (affiche)
form.bt2.clicked.connect (fermer)
app.exec_()