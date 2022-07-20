from PyQt5 import QtCore, QtGui, QtWidgets

"""
fenêtre d'aide liée au bouton Aide
"""

class Ui_help_window(object):

    def setupUi(self, help_window):

        help_window.setObjectName("help_window")
        help_window.resize(800, 600)
        help_window.setMinimumSize(800,600)
        help_window.setMaximumSize(800,600)
        help_window.setWindowTitle("Aide")
        icon = QtGui.QIcon("icons\help_icon.png")
        help_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(help_window)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 561))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        help_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(help_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        help_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(help_window)
        self.statusbar.setObjectName("statusbar")
        help_window.setStatusBar(self.statusbar)

        self.retranslateUi(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate("help_window", "Aide"))
        self.textBrowser.setHtml(_translate("help_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Ecrit par</span> <span style=\" font-weight:600; font-style:italic;\">Jacintho MPETEYE.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Vous ne vous y retrouvez plus ? Pas de panique, lisez attentivement le mode d\'emploi suivant. Nous espérons qu\'il vous sera utile.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">1-Authentification</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Au lancement du logiciel, vous verrez apparaître une fenêtre d’authentification. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Renseignez les champs à l’aide de vos identifiants si vous êtes un utilisateur déjà enregistré dans le système et cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« accéder »</span><span style=\" font-size:8pt;\">. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Si vous n’êtes pas un utilisateur enregistré dans le système l’accès vous sera refusé. Vous pouvez toutefois, demander à un des utilisateurs enregistrés de se connecter et de vous ajouter comme utilisateur. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Le mot de passe est masqué par défaut. Pour le rendre visible, cliquez sur l’icône d’œil au bout du champ de saisie, et encore une fois pour le masquer. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2-Onglet «Gestion des équipements »</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Ajouter un équipement</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour ajouter un nouveau stock d’équipements, renseignez les informations demandées sur la fenêtre. Si vous ne connaissez pas le prix unitaire des éléments du stock, pas de panique, vous pouvez laisser la valeur à 0 et venir la modifier une fois que vous aurez connaissance du prix unitaire. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Une fois cela fait, cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Ajouter » </span><span style=\" font-size:8pt;\">pour ajouter le nouveau stock d’équipements. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour vérifier que votre stock a bien été ajouté, vérifiez l’élément à l’ID le plus grand dans la table de l’onglet, ou alors vous pouvez effectuer une recherche de sa désignation dans les onglets : « Supprimer équipement – Exporter » et « Modifier des spécifications ». </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Supprimer équipement – Exporter</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour supprimer un stock d’équipements, cliquez sur la ligne contenant les informations relatives au stock et cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Supprimer ».</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">N’hésitez pas à saisir la désignation de votre stock dans la barre de recherche pour la faire remonter en haut de la table. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Vérifiez ensuite dans la table si l’élément à bien été supprimé </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">En cliquant sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Exporter la table »</span><span style=\" font-size:8pt;\">, un répertoire s’ouvrira. Vous devrez alors choisir le dossier dans lequel vous souhaitez enregistrer la feuille de calcul Excel qui sera créée. Cela peut être pratique si vous voulez imprimer le contenu des tables pour un bilan ou quelque tâche que ce soit. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Modifier des spécifications</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour modifier les information relatives à un stock donné, cliquez dans la table sur la ligne correspondant à votre stock. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Ces informations remplirons automatiquement les champs à gauche de la table. Ensuite vous n’avez plus qu’à changer celles des informations que vous désirez modifier. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Une fois cela fait, cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« modifier »</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Vérifiez ensuite si les informations ont bien été mise à jour dans la table </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Tri et statistiques</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">La première liste déroulante vous propose les options de tri existantes. Il vous suffit d’en sélectionner une pour voir le résultat apparaître dans le champ à droite. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour obtenir des graphiques construites à partir des données des tables, sélectionnez un type de graphique dans la dernière liste déroulante, puis cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Obtenir des stats »</span><span style=\" font-size:8pt;\"> . Vous verrez apparaître une fenêtre avec un diagramme à bandes. N’hésitez pas personnaliser le graphique à votre guise à l’aide des boutons de la barre d’outils. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3- Onglet « Gestion des utilisateurs »</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Ajouter un utilisateur</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour ajouter un nouvel utilisateur, renseigner le nom d’utilisateur ainsi que son mot de passe. Ensuite cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Ajouter ». </span><span style=\" font-size:8pt;\">Vous verrez s’ouvrir une notification de confirmation. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">N.B : Le nom d’utilisateur n’a que 15 caractères admissibles et le mot de passe 10 caractères admissibles. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:8pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Supprimer un utilisateur</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour supprimer un utilisateur sélectionnez le nom de ce dernier dans la liste des utilisateurs à droite, puis cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Supprimer ».</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">4-Onglet « Historique »</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Pour supprimer un élément de l’historique, cliquez sur la ligne correspondant à ce dernier dans la table puis cliquez sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Effacer l’élément ».</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">En cliquant sur le bouton </span><span style=\" font-size:8pt; font-weight:600;\">« Effacer l’historique »,</span><span style=\" font-size:8pt;\"> vous viderez tout le registre. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Il est recommandé d’effacer tout l’historique dès que cela est possible, afin d’économiser les ressources du logiciel. </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_window = QtWidgets.QMainWindow()
    ui = Ui_help_window()
    ui.setupUi(help_window)
    help_window.show()
    sys.exit(app.exec_())
