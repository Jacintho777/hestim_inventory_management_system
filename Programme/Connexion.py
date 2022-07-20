from PyQt5 import QtCore, QtGui, QtWidgets
from gestion_de_stock import Ui_second_window
from chiffrage import cesar_reverse
from time import sleep
import connexion1 #importation de l'image du login et du logo de Hestim

class Ui_Connexion(object):
    
    def setupUi(self, Connexion):

        Connexion.setObjectName("Connexion")
        Connexion.resize(1035, 698)
        Connexion.setMinimumSize(1035, 698)
        Connexion.setMaximumSize(1035, 698)
        icon = QtGui.QIcon("icons\carton1.png")
        Connexion.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(Connexion)
        self.centralwidget.setObjectName("centralwidget")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 626, 171, 51))
        font = QtGui.QFont()
        font.setKerning(True)
        self.logo.setFont(font)
        self.logo.setToolTip("")
        self.logo.setStatusTip("")
        self.logo.setWhatsThis("")
        self.logo.setAccessibleName("")
        self.logo.setAccessibleDescription("")
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("image: url(:/newPrefix/Hestim-Logo.png);")
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setScaledContents(False)
        self.logo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logo.setObjectName("logo")

        self.login_image = QtWidgets.QLabel(self.centralwidget)
        self.login_image.setGeometry(QtCore.QRect(450, 100, 141, 111))
        font = QtGui.QFont()
        font.setKerning(True)
        self.login_image.setFont(font)
        self.login_image.setToolTip("")
        self.login_image.setStatusTip("")
        self.login_image.setWhatsThis("")
        self.login_image.setAccessibleName("")
        self.login_image.setAccessibleDescription("")
        self.login_image.setAutoFillBackground(False)
        self.login_image.setStyleSheet("image : url(:/newPrefix/Login1.png)")
        self.login_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_image.setText("")
        self.login_image.setTextFormat(QtCore.Qt.AutoText)
        self.login_image.setScaledContents(True)
        self.login_image.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_image.setObjectName("login_image")

        self.asking_ids = QtWidgets.QLabel(self.centralwidget)
        self.asking_ids.setGeometry(QtCore.QRect(410, 220, 251, 51))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setPointSize(10)
        self.asking_ids.setFont(font)
        self.asking_ids.setObjectName("asking_ids")

        self.username_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.username_entry.setGeometry(QtCore.QRect(385, 340, 271, 41))
        self.username_entry.setObjectName("username_entry")
        font = QtGui.QFont("Cascadia Code")
        font.setPointSize(10)
        self.username_entry.setFont(font)

        self.password_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entry.setGeometry(QtCore.QRect(385, 450, 271, 41))
        self.password_entry.setObjectName("password_entry")
        font = QtGui.QFont("Cascadia Code")
        font.setPointSize(10)
        self.password_entry.setFont(font)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(472, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setObjectName("password")

        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(460, 290, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setObjectName("username")

        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(-20, 0, 1061, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.titre.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.titre.setObjectName("titre")

        self.statue = QtWidgets.QLabel(self.centralwidget)
        self.statue.setGeometry(QtCore.QRect(460, 510, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.statue.setFont(font)
        self.statue.setStyleSheet("color: rgb(200, 0, 0);")
        self.statue.setText("Accès refusé !")
        self.statue.setObjectName("statue")
        self.statue.hide()

        self.eye_icon = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.hide_show_password())
        self.eye_icon.setGeometry(QtCore.QRect(621, 455, 31, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.eye_icon.setStyleSheet("image : url(:/newPrefix/eye.png)")
        self.eye_icon.setText("")
        self.eye_icon.setObjectName("eye_icon")

        self.connexion_quit_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : Connexion.close())
        self.connexion_quit_button.setGeometry(QtCore.QRect(890, 630, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connexion_quit_button.setFont(font)
        self.connexion_quit_button.setObjectName("connexion_quit_button")

        self.access_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.check())
        self.access_button.setGeometry(QtCore.QRect(450, 570, 136, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.access_button.setFont(font)
        self.access_button.setObjectName("access_button")

        Connexion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Connexion)
        self.statusbar.setObjectName("statusbar")
        Connexion.setStatusBar(self.statusbar)

        #variable pour la fonction de clignotement
        self.flag = False
        #Variable pour l'état de visisbilité du mot de passe
        self.password_view = False

        #timer pour générer l'action à intervalles de temps
        self.timer = QtCore.QTimer(interval = 1000)
        self.timer.timeout.connect(self.blink)
        self.timer.start()

        self.retranslateUi(Connexion)
        QtCore.QMetaObject.connectSlotsByName(Connexion)

    def blink(self): #fonction pour faire clignoter le boutton accéder
        if self.flag:
            self.access_button.setStyleSheet('background-color : rgb(220,220,220);')
        else:
            self.access_button.setStyleSheet("background-color : rgb(255,255,255);")
        self.flag = not self.flag

    def hide_show_password(self): #masquer et afficher le mot de passe à volonté
        if self.password_view :
            self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.password_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_view = not self.password_view

    def check(self):
        """comparer les données saisies dans les champs avec celles stockées dans identifiants.txt"""
        identifiants = open("databases\identifiants.txt",'r')
        for line in identifiants.readlines():
            line = line.rstrip('\n').split('|')
            if self.username_entry.text() ==  cesar_reverse(line[0],2) and self.password_entry.text() == cesar_reverse(line[1],5):
                self.appWindow = QtWidgets.QMainWindow()
                self.ui = Ui_second_window()
                self.ui.setupUi(self.appWindow)
                self.appWindow.show()
                self.ui.current_user.setText("Utilisateur connecté : "+self.username_entry.text()+"  ")
                Connexion.close()
                break
        else:
            #réinitialiser les champs de saisie
            self.username_entry.setText("")
            self.password_entry.setText("")
            #Affichage du message d'erreur
            self.statue.show()
        identifiants.close()

    def retranslateUi(self, Connexion):
        _translate = QtCore.QCoreApplication.translate
        Connexion.setWindowTitle(_translate("Connexion", "Authentification - HestimLab's Devices and Tools Management System"))
        self.asking_ids.setText(_translate("Connexion", "Veuillez saisir vos identifiants..."))
        self.password.setText(_translate("Connexion", "Mot de passe"))
        self.username.setText(_translate("Connexion", "Nom d\'utilisateur"))
        self.titre.setText(_translate("Connexion", "                          Système de gestion des équipements du laboratoire HESTIM"))
        self.connexion_quit_button.setText(_translate("Connexion", "Quitter"))
        self.access_button.setText(_translate("Connexion", "Accéder"))
        self.eye_icon.setText(_translate("Connexion", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connexion = QtWidgets.QMainWindow()
    ui = Ui_Connexion()
    ui.setupUi(Connexion)
    Connexion.show()
    sys.exit(app.exec_())
