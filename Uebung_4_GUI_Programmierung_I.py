import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()




        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.adresseLineEdit = QLineEdit()
        self.postleitzahlLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.land = QComboBox ()
        self.land.addItems (["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Save")

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("PostLeitzahl:", self.postleitzahlLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button)
    


        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        #menubar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.quit)
        save.triggered.connect(self.save)


        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

        # Fenster anzeigen
        self.show()
    def createConnects(self):
        self.button.clicked.connect(self.save)
    def save(self):
        file = open("Output.txt","w", encoding="utf-8")
        file.write(f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtstag.text()},{self.adresse.text()},{self.postleitzahl.text()},{self.ort.text()},{self.land.currentText()}")
        file.close()
    def quit (self):
        print("Fenster geschlossen")
        self.close()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()