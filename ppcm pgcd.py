from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem

def pgcd_ppcm():
    if(w.L1.text().isdigit()==False) or (int(w.L1.text()==0)):
        w.res.setText("tapper un entier m")
        w.L1.setText("")
        w.l1.setFocus()
    if(w.L2.text().isdigit()==False) or (int(w.L2.text()==0)):
        w.res.setText("tapper un entier n!")
        w.L2.setText("")
        w.l1.setFocus()
    elif(w.pgcd.isChecked()==False) and(w.ppcm.isChecked()==False):
        w.res.setText("choisir pgcd ou ppcm!")
    elif(w.pgcd.isChecked()):
        calcul_pgcd()
    else:
        calcul_ppcm()

def calcul_pgcd():
    m=int(w.L1.text())
    n=int(w.L2.text())
    p=pgcd(m,n)
    w.res.setText("pgcd="+str(p))
    
def pgcd(m,n):
    if n==0 :
        return m
    else:
        return pgcd(n,m%n)
    
def calcul_ppcm():
    m=int(w.L1.text())
    n=int(w.L2.text())
    pp=ppcm(m,n,1)
    w.res.setText("le ppcm de"+str(m)+"et"+str(n)+"="+str(pp))
    
def ppcm(m,n,i):
    if(m*i % n==0):
        return m*i
    else:
        return ppcm(m,n,i+1)
    
def effacer():
    w.L1.clear()
    w.L2.clear()
    w.res.clear()

def fermer():
    w.close()
    
    
        
        
    
        
    

app = QApplication([])
w = loadUi("pgcd ppcm.ui")
w.show()
w.B1.clicked.connect(pgcd_ppcm)
w.B2.clicked.connect(effacer)
w.B3.clicked.connect(fermer)

app.exec_()