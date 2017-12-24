## Ali Ayrancı - SALİHLİ CBÜ - BİLGİSAYAR PROGRAMCILIĞI.

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys

ilknum = 0.0
yeninum = 0.0
sonuc = 0.0
islem=""

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ali Ayrancı Basic Calculator")
        self.disDikey = QVBoxLayout(self)
        self.satir = QHBoxLayout(self)
        self.birincirakamlar = QHBoxLayout(self)
        self.ikincirakamlar = QHBoxLayout(self)
        self.ucuncurakamlar = QHBoxLayout(self)
        self.dorduncucirakamlar = QHBoxLayout(self)
        self.besincirakamlar = QHBoxLayout(self)
        self.sifirkati = QHBoxLayout(self)
        self.hata = QHBoxLayout(self)


        self.disDikey.addLayout(self.satir)
        self.disDikey.addLayout(self.birincirakamlar)
        self.disDikey.addLayout(self.ikincirakamlar)
        self.disDikey.addLayout(self.ucuncurakamlar)
        self.disDikey.addLayout(self.sifirkati)
        self.disDikey.addLayout(self.dorduncucirakamlar)
        self.disDikey.addLayout(self.besincirakamlar)
        self.disDikey.addLayout(self.hata)

        self.hesapsatir = QLineEdit(self)
        self.hatamesaji = QLabel(self)
        self.bir = QPushButton(self)
        self.iki = QPushButton(self)
        self.uc = QPushButton(self)
        self.dort = QPushButton(self)
        self.bes = QPushButton(self)
        self.alti = QPushButton(self)
        self.yedi = QPushButton(self)
        self.sekiz = QPushButton(self)
        self.dokuz = QPushButton(self)
        self.sifir = QPushButton(self)
        self.c = QPushButton(self)
        self.arti = QPushButton(self)
        self.eksi = QPushButton(self)
        self.carp = QPushButton(self)
        self.bol = QPushButton(self)
        self.esittir = QPushButton(self)

        self.satir.addWidget(self.hesapsatir)
        self.birincirakamlar.addWidget(self.bir)
        self.bir.setText("1")
        self.birincirakamlar.addWidget(self.iki)
        self.iki.setText("2")
        self.birincirakamlar.addWidget(self.uc)
        self.uc.setText("3")
        self.ikincirakamlar.addWidget(self.dort)
        self.dort.setText("4")
        self.ikincirakamlar.addWidget(self.bes)
        self.bes.setText("5")
        self.ikincirakamlar.addWidget(self.alti)
        self.alti.setText("6")
        self.ucuncurakamlar.addWidget(self.yedi)
        self.yedi.setText("7")
        self.ucuncurakamlar.addWidget(self.sekiz)
        self.sekiz.setText("8")
        self.ucuncurakamlar.addWidget(self.dokuz)
        self.dokuz.setText("9")
        self.dorduncucirakamlar.addWidget(self.arti)
        self.arti.setText("+")
        self.dorduncucirakamlar.addWidget(self.eksi)
        self.eksi.setText("-")
        self.dorduncucirakamlar.addWidget(self.carp)
        self.carp.setText("*")
        self.dorduncucirakamlar.addWidget(self.bol)
        self.bol.setText("/")
        self.sifirkati.addWidget(self.sifir)
        self.sifir.setText("0")
        self.besincirakamlar.addWidget(self.c)
        self.c.setText("C")
        self.besincirakamlar.addWidget(self.esittir)
        self.esittir.setText("=")
        self.hata.addWidget(self.hatamesaji)

        self.bir.clicked.connect(self.birbasildi)
        self.iki.clicked.connect(self.ikibasildi)
        self.uc.clicked.connect(self.ucbasildi)
        self.dort.clicked.connect(self.dortbasildi)
        self.bes.clicked.connect(self.besbasildi)
        self.alti.clicked.connect(self.altibasildi)
        self.yedi.clicked.connect(self.yedibasildi)
        self.sekiz.clicked.connect(self.sekizbasildi)
        self.dokuz.clicked.connect(self.dokuzbasildi)
        self.sifir.clicked.connect(self.sifirbasildi)
        self.c.clicked.connect(self.cbasildi)
        self.arti.clicked.connect(self.artibasildi)
        self.eksi.clicked.connect(self.eksibasildi)
        self.carp.clicked.connect(self.carpbasildi)
        self.bol.clicked.connect(self.bolbasildi)
        self.esittir.clicked.connect(self.esittirbasildi)



    def birbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "1")


    def ikibasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "2")

    def ucbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "3")

    def dortbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "4")

    def besbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "5")

    def altibasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "6")

    def yedibasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "7")

    def sekizbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "8")

    def dokuzbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "9")

    def sifirbasildi(self):
        self.hesapsatir.setText(self.hesapsatir.text() + "0")

    def cbasildi(self):
        global islem
        global ilknum
        global yeninum
        global sonuc
        islem=""
        ilknum=0.0
        yeninum=0.0
        sonuc=0.0
        self.hesapsatir.setText("")
        self.hatamesaji.setText("")

    def artibasildi(self):
        global islem
        global  ilknum
        global islem
        if self.hesapsatir.text()=="":
            self.hatamesaji.setText("Önce Bir Sayı Belirlemeden İşlem Yapılmaz")
        elif islem=="":
            ilknum = float(self.hesapsatir.text())
            islem = "arti"
            self.hesapsatir.setText("")
        else:
            self.hatamesaji.setText("Zaten İşlem Seçilmiş")

    def eksibasildi(self):
        global islem
        global ilknum
        if self.hesapsatir.text()=="":
            self.hatamesaji.setText("Önce Bir Sayı Belirlemeden İşlem Yapılmaz")
        elif islem=="":
            ilknum = float(self.hesapsatir.text())
            islem = "eksi"
            self.hesapsatir.setText("")
        else:
            self.hatamesaji.setText("Zaten İşlem Seçilmiş")

    def carpbasildi(self):
        global islem
        global ilknum
        if self.hesapsatir.text()=="":
            self.hatamesaji.setText("Önce Bir Sayı Belirlemeden İşlem Yapılmaz")
        elif islem=="":
            ilknum = float(self.hesapsatir.text())
            islem = "carp"
            self.hesapsatir.setText("")
        else:
            self.hatamesaji.setText("Zaten İşlem Seçilmiş")

    def bolbasildi(self):
        global islem
        global ilknum
        if self.hesapsatir.text()=="":
            self.hatamesaji.setText("Önce Bir Sayı Belirlemeden İşlem Yapılmaz")
        elif islem=="":
            ilknum = float(self.hesapsatir.text())
            islem = "bol"
            self.hesapsatir.setText("")
        else:
            self.hatamesaji.setText("Zaten İşlem Seçilmiş")

    def esittirbasildi(self):
        global ilknum
        global yeninum
        global sonuc
        global islem

        if islem=="":
            self.hatamesaji.setText("Sayı ve İşlemler belirlenmeden 'EŞİTTİR' butonu kullanılamaz. ")
        elif self.hesapsatir.text()=="" :
            self.hatamesaji.setText("Sayı ve İşlemler belirlenmeden 'EŞİTTİR' butonu kullanılamaz. ")
        else:
            if islem=="bol":
                yeninum = float(self.hesapsatir.text())
                sonuc=ilknum/yeninum
                self.hatamesaji.setText("")
                self.hesapsatir.setText(str(sonuc))
                islem = ""
                ilknum = 0.0
                yeninum = 0.0
            elif islem=="carp":
                yeninum = float(self.hesapsatir.text())
                sonuc = ilknum * yeninum
                self.hatamesaji.setText("")
                self.hesapsatir.setText(str(sonuc))
                islem = ""
                ilknum = 0.0
                yeninum = 0.0
            elif islem=="eksi":
                yeninum = float(self.hesapsatir.text())
                sonuc = ilknum - yeninum
                self.hatamesaji.setText("")
                self.hesapsatir.setText(str(sonuc))
                islem = ""
                ilknum = 0.0
                yeninum = 0.0
            elif islem=="arti":
                yeninum = float(self.hesapsatir.text())
                sonuc = ilknum + yeninum
                self.hatamesaji.setText("")
                self.hesapsatir.setText(str(sonuc))
                islem = ""
                ilknum = 0.0
                yeninum = 0.0






uygulama = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()

## Ali Ayrancı - SALİHLİ CBÜ - BİLGİSAYAR PROGRAMCILIĞI.