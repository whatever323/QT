from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from numpy import*


def remplir():
    if z.L1.text().isdecimal()==False:
        z.res.setText("tapez entier")
        z.L1.setText("")
    else:
        z.list.addItem(z.L1.text())
        z.L1.setText("")
        
def rech_dich():
    n=z.list.count()
    t=array([int()]*n)
    for i in range(n):
        t[i]=int(z.list.item(i).text())
    if not(verif_tricroiss(n,t)):
        z.res.setText("saisir des entien croiss")
        z.list.clear()
        z.L2.setText("")
        z.L1.setText("")
    elif((z.L2.text()=="")or(z.L2.text().isdecimal()==False)):
        z.res.setText("tappez entier valide")
        
    else:
        x=int(z.L2.text())
        exist=False
        binf=0
        bsupp=n-1
        while(exist==False)and(binf<=bsupp):
            mil=(binf+bsupp)//2
            if x==t[mil]:
                exist=True
            elif x<t[mil]:
                bsupp=mil-1
            else:
                binf=mil+1
                
        if exist:
            z.res.setText(str(x)+"existe")
        else:
            z.res.setText(str(x)+"n existe pas")
            


def verif_tricroiss(n,t):
    for i in range(1, n):
        if t[i] < t[i - 1]:
            return False
    return True

    
def effacer():
    z.res.clear()
    z.list.clear()
    z.L2.clear()
    
def fermer():
    z.close()

        

app = QApplication([])
z = loadUi("recherche dich.ui")
z.show()
z.BB.clicked.connect(remplir)
z.B1.clicked.connect(rech_dich)
z.B2.clicked.connect(effacer)
z.B3.clicked.connect(fermer)
app.exec_()