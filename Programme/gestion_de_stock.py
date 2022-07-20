import os

from PyQt5 import QtCore, QtGui, QtWidgets
from chiffrage import cesar, cesar_reverse
import matplotlib.pyplot as plt
from datetime import date
from pandas import DataFrame
from help import Ui_help_window
import add_user_mediafile #importation de l'image du login partie ajout d'utilisateur

#recuperer le dernier ID

last_id = open('databases\last_id.txt','r')
current_id = int(last_id.readlines()[0].rstrip('\n'))
last_id.close()

passwords = []

class Ui_second_window(object):
    
    def setupUi(self, second_window):

        second_window.setObjectName("second_window")
        second_window.resize(1104, 700)
        second_window.setMinimumSize(1104, 700)
        second_window.setMaximumSize(1104, 700)
        icon = QtGui.QIcon("icons\carton1.png")
        second_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")
        self.app_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.app_tabWidget.setGeometry(QtCore.QRect(0, 50, 1111, 651))
        self.app_tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        
        self.app_tabWidget.setFont(font)
        self.app_tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.app_tabWidget.setAutoFillBackground(False)
        self.app_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.app_tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.app_tabWidget.setDocumentMode(True)
        self.app_tabWidget.setObjectName("app_tabWidget")
        
        self.tab_gestion_eq = QtWidgets.QWidget()
        self.tab_gestion_eq.setObjectName("tab_gestion_eq")
        
        self.gestion_eq_tabWidget = QtWidgets.QTabWidget(self.tab_gestion_eq)
        self.gestion_eq_tabWidget.setGeometry(QtCore.QRect(0, -2, 1111, 601))
        self.gestion_eq_tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gestion_eq_tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.gestion_eq_tabWidget.setObjectName("gestion_eq_tabWidget")
        
        self.tab_add_eq = QtWidgets.QWidget()
        self.tab_add_eq.setObjectName("tab_add_eq")
        
        self.label_designation_add = QtWidgets.QLabel(self.tab_add_eq)
        self.label_designation_add.setGeometry(QtCore.QRect(40, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_designation_add.setFont(font)
        self.label_designation_add.setObjectName("label_designation_add")
        
        self.table_add_eq = QtWidgets.QTableWidget(self.tab_add_eq)
        self.table_add_eq.setGeometry(QtCore.QRect(420, 11, 671, 541))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_add_eq.setFont(font)
        self.table_add_eq.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_add_eq.setTabKeyNavigation(False)
        self.table_add_eq.setProperty("showDropIndicator", False)
        self.table_add_eq.setDragDropOverwriteMode(False)
        self.table_add_eq.setRowCount(0)
        self.table_add_eq.setObjectName("table_add_eq")
        self.table_add_eq.setColumnCount(5)
        self.table_add_eq.setColumnWidth(4,165)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_add_eq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_eq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_eq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_eq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_add_eq.setHorizontalHeaderItem(4, item)
        self.table_add_eq.verticalHeader().setVisible(False)
        self.table_add_eq.verticalHeader().setHighlightSections(False)

        
        self.label_quantite_add = QtWidgets.QLabel(self.tab_add_eq)
        self.label_quantite_add.setGeometry(QtCore.QRect(40, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_quantite_add.setFont(font)
        self.label_quantite_add.setObjectName("label_quantite_add")
        
        self.label_prix_add = QtWidgets.QLabel(self.tab_add_eq)
        self.label_prix_add.setGeometry(QtCore.QRect(40, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prix_add.setFont(font)
        self.label_prix_add.setObjectName("label_prix_add")
        
        self.label_dep_add = QtWidgets.QLabel(self.tab_add_eq)
        self.label_dep_add.setGeometry(QtCore.QRect(40, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dep_add.setFont(font)
        self.label_dep_add.setObjectName("label_dep_add")
        
        self.designation_entry_add = QtWidgets.QLineEdit(self.tab_add_eq)
        self.designation_entry_add.setGeometry(QtCore.QRect(160, 180, 221, 31))
        self.designation_entry_add.setObjectName("designation_entry_add")
        
        self.quantite_spinBox_add = QtWidgets.QSpinBox(self.tab_add_eq)
        self.quantite_spinBox_add.setGeometry(QtCore.QRect(160, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantite_spinBox_add.setFont(font)
        self.quantite_spinBox_add.setMinimum(1)
        self.quantite_spinBox_add.setObjectName("quantite_spinBox_add")
        
        self.prix_dSpinBox_add = QtWidgets.QDoubleSpinBox(self.tab_add_eq)
        self.prix_dSpinBox_add.setGeometry(QtCore.QRect(160, 300, 221, 31))
        self.prix_dSpinBox_add.setMaximum(100000.0)
        self.prix_dSpinBox_add.setSingleStep(5.0)
        self.prix_dSpinBox_add.setObjectName("prix_dSpinBox_add")
        
        self.dep_comboBox_add = QtWidgets.QComboBox(self.tab_add_eq)
        self.dep_comboBox_add.setGeometry(QtCore.QRect(160, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dep_comboBox_add.setFont(font)
        self.dep_comboBox_add.setObjectName("dep_comboBox_add")
        self.dep_comboBox_add.addItem("")
        self.dep_comboBox_add.addItem("")
        self.dep_comboBox_add.addItem("")
        self.dep_comboBox_add.addItem("")
        self.dep_comboBox_add.addItem("")
        self.dep_comboBox_add.addItem("")
        
        self.label_add_eq = QtWidgets.QLabel(self.tab_add_eq)
        self.label_add_eq.setGeometry(QtCore.QRect(30, 80, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_add_eq.setFont(font)
        self.label_add_eq.setObjectName("label_add_eq")
        
        self.eq_add_button = QtWidgets.QPushButton(self.tab_add_eq, clicked = lambda : self.add_eq())
        self.eq_add_button.setGeometry(QtCore.QRect(120, 440, 151, 41))
        self.eq_add_button.setObjectName("eq_add_button")
        
        self.gestion_eq_tabWidget.addTab(self.tab_add_eq, "")
        
        self.tab_suppress_eq = QtWidgets.QWidget()
        self.tab_suppress_eq.setObjectName("tab_suppress_eq")
        
        self.eq_suppress_button = QtWidgets.QPushButton(self.tab_suppress_eq, clicked = lambda : self.delete_eq())
        self.eq_suppress_button.setGeometry(QtCore.QRect(140, 200, 151, 41))
        self.eq_suppress_button.setObjectName("eq_suppress_button")

        self.table_export_button = QtWidgets.QPushButton(self.tab_suppress_eq, clicked=lambda: self.export_table())
        self.table_export_button.setGeometry(QtCore.QRect(140, 300, 151, 41))
        self.table_export_button.setObjectName("table_export_button")
        
        self.label_recherche_supress = QtWidgets.QLabel(self.tab_suppress_eq)
        self.label_recherche_supress.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_recherche_supress.setFont(font)
        self.label_recherche_supress.setObjectName("label_recherche_supress")
        
        self.recherche_entry_suppress = QtWidgets.QLineEdit(self.tab_suppress_eq)
        self.recherche_entry_suppress.setGeometry(QtCore.QRect(140, 20, 260, 31))
        self.recherche_entry_suppress.setObjectName("recherche_entry_suppress")
        
        self.table_suppress_eq = QtWidgets.QTableWidget(self.tab_suppress_eq)
        self.table_suppress_eq.setGeometry(QtCore.QRect(420, 11, 671, 541))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_suppress_eq.setFont(font)
        self.table_suppress_eq.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_suppress_eq.setTabKeyNavigation(False)
        self.table_suppress_eq.setProperty("showDropIndicator", False)
        self.table_suppress_eq.setDragDropOverwriteMode(False)
        self.table_suppress_eq.setRowCount(0)
        self.table_suppress_eq.setObjectName("table_suppress_eq")
        self.table_suppress_eq.setColumnCount(5)
        self.table_suppress_eq.setColumnWidth(4,165)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_suppress_eq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_suppress_eq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_suppress_eq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_suppress_eq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_suppress_eq.setHorizontalHeaderItem(4, item)
        self.table_suppress_eq.verticalHeader().setVisible(False)
        self.table_suppress_eq.verticalHeader().setHighlightSections(False)
        
        self.research_logo_3 = QtWidgets.QLabel(self.tab_suppress_eq)
        self.research_logo_3.setGeometry(QtCore.QRect(361, 14, 41, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.research_logo_3.setFont(font)
        self.research_logo_3.setToolTip("")
        self.research_logo_3.setStatusTip("")
        self.research_logo_3.setWhatsThis("")
        self.research_logo_3.setAccessibleName("")
        self.research_logo_3.setAccessibleDescription("")
        self.research_logo_3.setAutoFillBackground(False)
        self.research_logo_3.setStyleSheet("image : url(:/newPrefix/research_logo.png)")
        self.research_logo_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.research_logo_3.setText("")
        self.research_logo_3.setTextFormat(QtCore.Qt.AutoText)
        self.research_logo_3.setScaledContents(True)
        self.research_logo_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.research_logo_3.setObjectName("research_logo_3")
        
        self.gestion_eq_tabWidget.addTab(self.tab_suppress_eq, "")
        
        self.tab_modify_eq = QtWidgets.QWidget()
        self.tab_modify_eq.setObjectName("tab_modify_eq")
        self.table_modify_eq = QtWidgets.QTableWidget(self.tab_modify_eq, clicked = lambda : self.fill_area_on_selection())
        self.table_modify_eq.setGeometry(QtCore.QRect(420, 11, 671, 541))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_modify_eq.setFont(font)
        self.table_modify_eq.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_modify_eq.setTabKeyNavigation(False)
        self.table_modify_eq.setProperty("showDropIndicator", False)
        self.table_modify_eq.setDragDropOverwriteMode(False)
        self.table_modify_eq.setRowCount(0)
        self.table_modify_eq.setObjectName("table_modify_eq")
        self.table_modify_eq.setColumnCount(5)
        self.table_modify_eq.setColumnWidth(4,165)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_modify_eq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_modify_eq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_modify_eq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_modify_eq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_modify_eq.setHorizontalHeaderItem(4, item)
        self.table_modify_eq.verticalHeader().setVisible(False)
        self.table_modify_eq.verticalHeader().setHighlightSections(False)
        
        self.label_modify_eq = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_modify_eq.setGeometry(QtCore.QRect(10, 80, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_modify_eq.setFont(font)
        self.label_modify_eq.setObjectName("label_modify_eq")
        
        self.label_designation_modify = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_designation_modify.setGeometry(QtCore.QRect(40, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_designation_modify.setFont(font)
        self.label_designation_modify.setObjectName("label_designation_modify")
        
        self.prix_dSpinBox_modify = QtWidgets.QDoubleSpinBox(self.tab_modify_eq)
        self.prix_dSpinBox_modify.setGeometry(QtCore.QRect(160, 300, 221, 31))
        self.prix_dSpinBox_modify.setMaximum(100000.0)
        self.prix_dSpinBox_modify.setSingleStep(5.0)
        self.prix_dSpinBox_modify.setObjectName("prix_dSpinBox_modify")
        
        self.label_prix_modify = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_prix_modify.setGeometry(QtCore.QRect(40, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_prix_modify.setFont(font)
        self.label_prix_modify.setObjectName("label_prix_modify")
        
        self.label_quantite_modify = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_quantite_modify.setGeometry(QtCore.QRect(40, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_quantite_modify.setFont(font)
        self.label_quantite_modify.setObjectName("label_quantite_modify")
        
        self.designation_entry_modify = QtWidgets.QLineEdit(self.tab_modify_eq)
        self.designation_entry_modify.setGeometry(QtCore.QRect(160, 180, 221, 31))
        self.designation_entry_modify.setObjectName("designation_entry_modify")
        
        self.label_dep_modify = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_dep_modify.setGeometry(QtCore.QRect(40, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dep_modify.setFont(font)
        self.label_dep_modify.setObjectName("label_dep_modify")
        
        self.quantite_spinBox_modify = QtWidgets.QSpinBox(self.tab_modify_eq)
        self.quantite_spinBox_modify.setGeometry(QtCore.QRect(160, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantite_spinBox_modify.setFont(font)
        self.quantite_spinBox_modify.setMinimum(1)
        self.quantite_spinBox_modify.setObjectName("quantite_spinBox_modify")
        
        self.eq_modify_button = QtWidgets.QPushButton(self.tab_modify_eq, clicked = lambda : self.modify_eq())
        self.eq_modify_button.setGeometry(QtCore.QRect(120, 440, 151, 41))
        self.eq_modify_button.setObjectName("eq_modify_button")
        
        self.dep_comboBox_modify = QtWidgets.QComboBox(self.tab_modify_eq)
        self.dep_comboBox_modify.setGeometry(QtCore.QRect(160, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dep_comboBox_modify.setFont(font)
        self.dep_comboBox_modify.setObjectName("dep_comboBox_modify")
        self.dep_comboBox_modify.addItem("")
        self.dep_comboBox_modify.addItem("")
        self.dep_comboBox_modify.addItem("")
        self.dep_comboBox_modify.addItem("")
        self.dep_comboBox_modify.addItem("")
        self.dep_comboBox_modify.addItem("")
        
        self.label_recherche_modify = QtWidgets.QLabel(self.tab_modify_eq)
        self.label_recherche_modify.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_recherche_modify.setFont(font)
        self.label_recherche_modify.setObjectName("label_recherche_modify")
        
        self.recherche_entry_modify = QtWidgets.QLineEdit(self.tab_modify_eq)
        self.recherche_entry_modify.setGeometry(QtCore.QRect(140, 20, 260, 31))
        self.recherche_entry_modify.setObjectName("recherche_entry_modify")
        
        self.research_logo_2 = QtWidgets.QLabel(self.tab_modify_eq)
        self.research_logo_2.setGeometry(QtCore.QRect(361, 14, 41, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.research_logo_2.setFont(font)
        self.research_logo_2.setToolTip("")
        self.research_logo_2.setStatusTip("")
        self.research_logo_2.setWhatsThis("")
        self.research_logo_2.setAccessibleName("")
        self.research_logo_2.setAccessibleDescription("")
        self.research_logo_2.setAutoFillBackground(False)
        self.research_logo_2.setStyleSheet("image : url(:/newPrefix/research_logo.png)")
        self.research_logo_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.research_logo_2.setText("")
        self.research_logo_2.setTextFormat(QtCore.Qt.AutoText)
        self.research_logo_2.setScaledContents(True)
        self.research_logo_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.research_logo_2.setObjectName("research_logo_2")
        
        self.gestion_eq_tabWidget.addTab(self.tab_modify_eq, "")
        
        self.tab_stat_eq = QtWidgets.QWidget()
        self.tab_stat_eq.setObjectName("tab_stat_eq")
        # self.tab_stat_eq.setStyleSheet('background-color : rgb(230,230,230) ')
        
        self.eq_list_afficher = QtWidgets.QListWidget(self.tab_stat_eq)
        self.eq_list_afficher.setGeometry(QtCore.QRect(420, 10, 671, 541))
        self.eq_list_afficher.setObjectName("eq_list_afficher")
        font = QtGui.QFont("Computer Modern")
        font.setPointSize(12)
        self.eq_list_afficher.setFont(font)
        
        self.label_trier = QtWidgets.QLabel(self.tab_stat_eq)
        self.label_trier.setGeometry(QtCore.QRect(40, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_trier.setFont(font)
        self.label_trier.setObjectName("label_trier")
        
        self.optionsTri_comboBox = QtWidgets.QComboBox(self.tab_stat_eq)
        self.optionsTri_comboBox.setGeometry(QtCore.QRect(130, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optionsTri_comboBox.setFont(font)
        self.optionsTri_comboBox.setObjectName("optionsTri_comboBox")
        self.optionsTri_comboBox.addItem("")
        self.optionsTri_comboBox.addItem("")
        
        self.get_graph_button = QtWidgets.QPushButton(self.tab_stat_eq, clicked = lambda : self.draw_graph())
        self.get_graph_button.setGeometry(QtCore.QRect(120, 310, 181, 41))
        self.get_graph_button.setObjectName("get_graph_button")
        
        self.optionsGraph_comboBox = QtWidgets.QComboBox(self.tab_stat_eq)
        self.optionsGraph_comboBox.setGeometry(QtCore.QRect(30, 390, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optionsGraph_comboBox.setFont(font)
        self.optionsGraph_comboBox.setObjectName("optionsGraph_comboBox")
        self.optionsGraph_comboBox.addItem("")
        self.optionsGraph_comboBox.addItem("")
        
        self.gestion_eq_tabWidget.addTab(self.tab_stat_eq, "")
        self.app_tabWidget.addTab(self.tab_gestion_eq, "")
        
        self.tab_gestion_user = QtWidgets.QWidget()
        self.tab_gestion_user.setObjectName("tab_gestion_user")
        
        self.gestion_user_tabWidget = QtWidgets.QTabWidget(self.tab_gestion_user)
        self.gestion_user_tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 590))
        self.gestion_user_tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.gestion_user_tabWidget.setObjectName("gestion_user_tabWidget")
        
        self.tab_add_user = QtWidgets.QWidget()
        self.tab_add_user.setObjectName("tab_add_user")
        
        self.password_entry2 = QtWidgets.QLineEdit(self.tab_add_user)
        self.password_entry2.setGeometry(QtCore.QRect(450, 320, 271, 41))
        self.password_entry2.setObjectName("password_entry2")
        self.password_entry2.setMaxLength(10)
        font = QtGui.QFont("Cascadia Code")
        font.setPointSize(10)
        self.password_entry2.setFont(font)
        
        self.username_entry2 = QtWidgets.QLineEdit(self.tab_add_user)
        self.username_entry2.setGeometry(QtCore.QRect(450, 210, 271, 41))
        self.username_entry2.setObjectName("username_entry2")
        self.username_entry2.setMaxLength(15)
        font = QtGui.QFont("Cascadia Code")
        font.setPointSize(10)
        self.username_entry2.setFont(font)
        
        self.user_add_button = QtWidgets.QPushButton(self.tab_add_user, clicked = lambda : self.add_user())
        self.user_add_button.setGeometry(QtCore.QRect(517, 430, 141, 41))
        self.user_add_button.setObjectName("user_add_button")
        
        self.login_image2 = QtWidgets.QLabel(self.tab_add_user)
        self.login_image2.setGeometry(QtCore.QRect(508, 70, 141, 111))
        font = QtGui.QFont()
        font.setKerning(True)
        self.login_image2.setFont(font)
        self.login_image2.setToolTip("")
        self.login_image2.setStatusTip("")
        self.login_image2.setWhatsThis("")
        self.login_image2.setAccessibleName("")
        self.login_image2.setAccessibleDescription("")
        self.login_image2.setAutoFillBackground(False)
        self.login_image2.setStyleSheet("image : url(:/newPrefix/Login.png)")
        self.login_image2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_image2.setText("")
        self.login_image2.setTextFormat(QtCore.Qt.AutoText)
        self.login_image2.setScaledContents(True)
        self.login_image2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_image2.setObjectName("login_image2")
        
        self.username2 = QtWidgets.QLabel(self.tab_add_user)
        self.username2.setGeometry(QtCore.QRect(287, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username2.setFont(font)
        self.username2.setObjectName("username2")
        
        self.password2 = QtWidgets.QLabel(self.tab_add_user)
        self.password2.setGeometry(QtCore.QRect(314, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password2.setFont(font)
        self.password2.setObjectName("password2")
        
        self.gestion_user_tabWidget.addTab(self.tab_add_user, "")
        
        self.tab_suppress_user = QtWidgets.QWidget()
        self.tab_suppress_user.setObjectName("tab_suppress_user")
        
        self.user_list = QtWidgets.QListWidget(self.tab_suppress_user)
        self.user_list.setGeometry(QtCore.QRect(390, 10, 691, 541))
        self.user_list.setObjectName("user_list")
        
        self.user_suppress_button = QtWidgets.QPushButton(self.tab_suppress_user, clicked = lambda : self.delete_user())
        self.user_suppress_button.setGeometry(QtCore.QRect(110, 240, 171, 41))
        self.user_suppress_button.setObjectName("user_suppress_button")
        
        self.gestion_user_tabWidget.addTab(self.tab_suppress_user, "")
        self.app_tabWidget.addTab(self.tab_gestion_user, "")
        
        self.tab_history = QtWidgets.QWidget()
        self.tab_history.setObjectName("tab_history")
        
        self.history_table = QtWidgets.QTableWidget(self.tab_history)
        self.history_table.setGeometry(QtCore.QRect(250, 10, 851, 571))
        self.history_table.setObjectName("history_table")
        self.history_table.setColumnCount(3)
        self.history_table.setRowCount(0)
        self.history_table.setColumnWidth(0,150)
        self.history_table.setColumnWidth(1,480)
        self.history_table.setColumnWidth(2,215)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(2, item)
        self.history_table.verticalHeader().setVisible(False)
        self.history_table.verticalHeader().setHighlightSections(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.history_table.setFont(font)
        
        self.clean_button = QtWidgets.QPushButton(self.tab_history, clicked = lambda : self.delete_whole_history())
        self.clean_button.setGeometry(QtCore.QRect(40, 290, 171, 41))
        self.clean_button.setObjectName("clean_button")
        
        self.element_suppress_button = QtWidgets.QPushButton(self.tab_history, clicked = lambda : self.delete_history_element())
        self.element_suppress_button.setGeometry(QtCore.QRect(40, 200, 171, 41))
        self.element_suppress_button.setObjectName("element_suppress_button")
        self.app_tabWidget.addTab(self.tab_history, "")
        
        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(140, 0, 823, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.titre.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.titre.setObjectName("titre")
        
        self.help_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.open_help())
        self.help_button.setGeometry(QtCore.QRect(3, 5, 134, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.help_button.setFont(font)
        self.help_button.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.help_button.setObjectName("help_button")
        
        self.app_quit_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : second_window.close())
        self.app_quit_button.setGeometry(QtCore.QRect(965, 5, 134, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.app_quit_button.setFont(font)
        self.app_quit_button.setStyleSheet("background-color: rgb(220, 220, 220)")
        self.app_quit_button.setObjectName("app_quit_button")
        second_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.current_user = QtWidgets.QLabel(self.statusbar)# variable pour stocker l'utilisateur de la session
        font = QtGui.QFont()
        font.setItalic(True)
        self.current_user.setFont(font)
        self.current_user.setStyleSheet("color : rgb(0,0,175)")

        self.statusbar.addWidget(self.current_user)

        self.retranslateUi(second_window)
        self.app_tabWidget.setCurrentIndex(0)
        self.gestion_eq_tabWidget.setCurrentIndex(3)
        self.gestion_user_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(second_window)
        
        #Connection des champs de recherche à la fonction de recherche
        
        self.recherche_entry_suppress.textChanged.connect(lambda : self.search(self.recherche_entry_suppress,self.table_suppress_eq))
        self.recherche_entry_modify.textChanged.connect(lambda : self.search(self.recherche_entry_modify,self.table_modify_eq))
        
        #Connection des comboBox de l'onglet Tri et Statistiques
        
        self.optionsTri_comboBox.activated.connect(lambda : self.sort_eq())
            
        #Chargement des données enregistrées

        self.load_data()
        self.load_user_data()
        self.load_history_data()

        
    def load_data(self):
        
        #ouverture du fichier texte de stockage
        
        equipement_saved = open('databases\equipements.txt','r')
        saved_data = [] #variable de recuperation des données 
        
        #recuperation des données
        for line in equipement_saved.readlines():
            line = line.rstrip('\n')
            saved_data.append(line.split("|"))
            
        equipement_saved.close()
        
        #affichage des données dans la table
        
        for row in saved_data : 
            
            #table dans la partie ajout d'equipements
            self.table_add_eq.setRowCount(self.table_add_eq.rowCount()+1)
            self.update_table(self.table_add_eq,row[1],row[2],row[3],row[4],row[0],True,self.table_add_eq.rowCount()-1)
            #table dans la partie modification de specifications
            self.table_modify_eq.setRowCount(self.table_add_eq.rowCount())
            self.update_table(self.table_modify_eq, row[1], row[2], row[3], row[4], row[0], True,self.table_add_eq.rowCount() - 1)
            #table dans la partie suppression d'équipement
            self.table_suppress_eq.setRowCount(self.table_add_eq.rowCount())
            self.update_table(self.table_suppress_eq, row[1], row[2], row[3], row[4], row[0], True,self.table_add_eq.rowCount() - 1)
            
    def load_user_data(self):
        
        global passwords
        
        """Ouverture du fichier d'enregistrement des identifiants et remplissaqe de passwords 
        et de la liste de l'onglet suppression d'utilisateurs"""
        
        identifiants = open('databases\identifiants.txt','r')
        for line in identifiants.readlines():
            line = line.rstrip('\n')
            self.user_list.addItem(cesar_reverse(line.split('|')[0],2))
            passwords.append(cesar_reverse(line.split('|')[1],5))
        identifiants.close()
        
    def load_history_data(self):
        
        historique = open('databases\historique.txt','r')
        for line in historique.readlines():
            line = line.rstrip('\n')
            self.history_table.setRowCount(self.history_table.rowCount()+1)
            self.history_table.setItem(self.history_table.rowCount()-1,0,QtWidgets.QTableWidgetItem(line.split('|')[0]))
            self.history_table.setItem(self.history_table.rowCount()-1,1,QtWidgets.QTableWidgetItem(line.split('|')[1]))
            self.history_table.setItem(self.history_table.rowCount()-1,2,QtWidgets.QTableWidgetItem(line.split('|')[2]))
        historique.close()
    
    """Fonctions de sauvegarde des données des tables"""    
    
    #Sauvegarde des données équipements
    
    def save_data(self):
        
        equipement_saved = open('databases\equipements.txt','w')
        
        for row in range(self.table_add_eq.rowCount()):
            line = self.table_add_eq.item(row,0).text()+'|'+self.table_add_eq.item(row,1).text()+'|'+self.table_add_eq.item(row,2).text()+'|'+self.table_add_eq.item(row,3).text()+'|'+self.table_add_eq.item(row,4).text()+'\n'
            equipement_saved.write(line)
            
        equipement_saved.close()   
    
    #Sauvegarde des données utilisateur
    
    def save_user_data(self):
        
        global passwords
        
        #Stocker l'utilisateur dans le fichier
        identifiants = open('databases\identifiants.txt','w')
        for index in range(self.user_list.count()):
            identifiants.write(cesar(self.user_list.item(index).text(),2)+'|'+cesar(passwords[index],5)+'\n')
        identifiants.close()
    
    #Sauvegarde de l'historique
    
    def save_history_data(self):
        
        historique = open('databases\historique.txt','w')
        for row in range(self.history_table.rowCount()):
            line = self.history_table.item(row,0).text()+'|'+self.history_table.item(row,1).text()+'|'+self.history_table.item(row,2).text()+'\n'
            historique.write(line)
            
        historique.close()
    
    def add_user(self):
        
        global passwords
        
        #Ajouter l'utilisateur à la liste de l'onglet supprimer
        new_user = self.username_entry2.text()
        
        self.user_list.addItem(self.username_entry2.text())
        
        passwords.append(self.password_entry2.text())
        
        #Vider les zones de saisie
        self.username_entry2.setText("")
        self.password_entry2.setText("")
                
        #message de confirmation
        
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Opération réussie !")
        msg.setWindowIcon(QtGui.QIcon("icons\juste.png"))
        msg.setText("Vous avez ajouté un nouvel utilisateur !")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()
        
        #Notification dans l'historique
        
        self.set_history_element("Nouvel utilisateur '"+new_user+"' ajouté")
        
        #Enregistrement des données
        
        self.save_user_data()
        self.save_history_data()
    def delete_user(self):

        try:
            #Affichage de la boîte de dialogue

            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            box.setWindowTitle('Confirmation')
            box.setText('Voulez vous vraiment supprimer l\'utilisateur ?\nCe dernier n\'aura plus accès au logiciel.')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Quitter')
            box.exec_()

            if box.clickedButton() == buttonY: #si le bouton oui est cliqué

                user_to_delete = self.user_list.item(self.user_list.currentRow()).text()
                #supprimer le mot de passe de la liste ouverte
                passwords.remove(passwords[self.user_list.currentRow()])
                #supprimer le mot de passe de la liste de l'onglet suppression d'utilisateurs
                self.user_list.takeItem(self.user_list.currentRow())

                #Notification dans l'historique

                self.set_history_element("Utilisateur '"+user_to_delete+"' supprimé")

                #Enregistrement des données utilisateurs
                self.save_user_data()
                self.save_history_data()

            elif box.clickedButton() == buttonN:  # si le bouton quitter est cliqué

                box.close()

        except:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur !")
            msg.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            msg.setText("Aucun utilisateur sélectionné !")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()

    def update_table(self, table, designation, quantite, prix, departement, id, need_id, row):

        if need_id :
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(id))
        table.setItem(row, 1,QtWidgets.QTableWidgetItem(designation))
        table.setItem(row, 2,QtWidgets.QTableWidgetItem(quantite))
        table.setItem(row, 3,QtWidgets.QTableWidgetItem(prix))
        table.setItem(row, 4,QtWidgets.QTableWidgetItem(departement))

    def add_eq(self):
        if self.designation_entry_add.text() == "" or self.designation_entry_add.text().strip(" ") == "" :

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur !")
            msg.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            msg.setText("Designation invalide !")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()

        else:
            #Ajouter l'equipement dans la table visible
            global current_id
            current_id += 1
            last_id = open('databases\last_id.txt','w')
            last_id.writelines(str(current_id))
            last_id.close()

            #Mise à jour de la partie de la table de la partie ajout
            self.table_add_eq.setRowCount(self.table_add_eq.rowCount()+1)
            self.update_table(self.table_add_eq,self.designation_entry_add.text(),str(self.quantite_spinBox_add.value()),str(self.prix_dSpinBox_add.value())+ " Dh",self.dep_comboBox_add.currentText(),str(current_id), True, self.table_add_eq.rowCount() - 1)

            #Mise à jour de la partie de la table de la partie modification
            self.table_modify_eq.setRowCount(self.table_add_eq.rowCount())
            self.update_table(self.table_modify_eq,self.designation_entry_add.text(),str(self.quantite_spinBox_add.value()),str(self.prix_dSpinBox_add.value())+ " Dh",self.dep_comboBox_add.currentText(),str(current_id), True, self.table_add_eq.rowCount() - 1)

            #Mise à jour de la liste des équipements dans la partie suppression
            self.table_suppress_eq.setRowCount(self.table_add_eq.rowCount())
            self.update_table(self.table_suppress_eq, self.designation_entry_add.text(), str(self.quantite_spinBox_add.value()),str(self.prix_dSpinBox_add.value())+ " Dh", self.dep_comboBox_add.currentText(),str(current_id), True, self.table_add_eq.rowCount() - 1)

            #Notification dans l'historique
            self.set_history_element("Nouvel équipement '"+self.designation_entry_add.text()+"' ajouté")

            #Réinitialisation des champs

            self.designation_entry_add.setText("")
            self.quantite_spinBox_add.setValue(1)
            self.prix_dSpinBox_add.setValue(0.00)
            self.dep_comboBox_add.setCurrentIndex(0)

            #stocker l'equipement dans le fichier texte
            self.save_data()
            self.save_history_data()

    def delete_eq(self):

        try:
             #Notification dans l'historique

            self.set_history_element("Equipement '"+self.table_add_eq.item(self.table_suppress_eq.currentRow(),1).text()+"' supprimé")

            #suppression dans la table de l'onglet ajout d'équipements
            self.table_add_eq.removeRow(self.table_suppress_eq.currentRow())
            #suppression dans la table de l'onglet modification d'équipements
            self.table_modify_eq.removeRow(self.table_suppress_eq.currentRow())
            #suppression dans la table de l'onglet suppression d'équipements
            self.table_suppress_eq.removeRow(self.table_suppress_eq.currentRow())

            #Retirer l'equipement du fichier texte
            self.save_data()
            self.save_history_data()

        except:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur !")
            msg.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            msg.setText("Aucun stock d'équipement sélectionné !")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        
    
    def fill_area_on_selection(self): #remplir les champs pour la modification
        
        self.designation_entry_modify.setText(self.table_add_eq.item(self.table_modify_eq.currentRow(),1).text())
        self.quantite_spinBox_modify.setValue(int(self.table_add_eq.item(self.table_modify_eq.currentRow(),2).text()))
        self.prix_dSpinBox_modify.setValue(float(self.table_add_eq.item(self.table_modify_eq.currentRow(),3).text().rstrip(' Dh')))
        self.dep_comboBox_modify.setCurrentIndex(self.dep_comboBox_modify.findText(self.table_add_eq.item(self.table_modify_eq.currentRow(),4).text()))
        
    def modify_eq(self):

        if self.designation_entry_modify.text() == "" or self.designation_entry_modify.text().strip(" ") == "":

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur !")
            msg.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            msg.setText("Designation invalide !")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()

        else:
            #Mise à jour de la ligne correspondant à l'équipement

                        #Dans la table de modification
            self.update_table(self.table_modify_eq,self.designation_entry_modify.text(),str(self.quantite_spinBox_modify.value()),str(self.prix_dSpinBox_modify.value())+ " Dh",self.dep_comboBox_modify.currentText(),None, False, self.table_modify_eq.currentRow())
                        #Dans la table d'ajout
            self.update_table(self.table_add_eq,self.designation_entry_modify.text(),str(self.quantite_spinBox_modify.value()),str(self.prix_dSpinBox_modify.value())+ " Dh",self.dep_comboBox_modify.currentText(),None, False, self.table_modify_eq.currentRow())
                        #Dans la table de suppression
            self.update_table(self.table_suppress_eq,self.designation_entry_modify.text(),str(self.quantite_spinBox_modify.value()),str(self.prix_dSpinBox_modify.value())+ " Dh",self.dep_comboBox_modify.currentText(),None, False, self.table_modify_eq.currentRow())

            #Notification dans l'historique

            self.set_history_element("Spécifications de l'équipement '"+self.designation_entry_modify.text()+"' modifiées")

            #Réinitialisation des champs

            self.designation_entry_modify.setText("")
            self.quantite_spinBox_modify.setValue(1)
            self.prix_dSpinBox_modify.setValue(0.00)
            self.dep_comboBox_modify.setCurrentIndex(0)


            #Modifier l'élément dans le fichier texte
            self.save_data()
            self.save_history_data()

    def export_table(self):
        columnHeaders = [] # liste des noms sur la colonne

        for column in range(self.table_add_eq.model().columnCount()):
            columnHeaders.append(self.table_add_eq.horizontalHeaderItem(column).text())

        df = DataFrame(columns = columnHeaders) #création du dataframe de pandas

        #Les élément de la table sont classés dans le dataframe
        for row in range(self.table_add_eq.rowCount()):
            for col in range(self.table_add_eq.columnCount()):
                df.at[row, columnHeaders[col]] = self.table_add_eq.item(row,col).text()

        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)' #filtre des extensions admissibles
        #affichage d'une boîte de dialogue pour sauvegarde de fichier
        response = QtWidgets.QFileDialog.getSaveFileName(
            caption = 'Exporter les données dans un tableur',
            directory = 'Equipements.xlsx',
            filter = file_filter,
            initialFilter ='Excel File(*.xlsx *.xls)'
        )
        df.to_excel(response[0], index = False) #conversion des données du panda en tableur excel dans le répertoire sélectionné
        self.set_history_element("Table des équipements exportée dans un tableur")

    def set_history_element(self, action):
        
        #ajoute un nouvel élément à l'historique
        
        self.history_table.setRowCount(self.history_table.rowCount()+1)
        self.history_table.setItem(self.history_table.rowCount()-1,0,QtWidgets.QTableWidgetItem(str(date.today())))
        self.history_table.setItem(self.history_table.rowCount()-1,1,QtWidgets.QTableWidgetItem(action))
        self.history_table.setItem(self.history_table.rowCount()-1,2,QtWidgets.QTableWidgetItem(self.current_user.text()[len("Utilisateur connecté : "):].rstrip(" ")))
        
    def delete_history_element(self):

        try:
            #supprime l'élément de l'historique sélectionné

            self.history_table.removeRow(self.history_table.currentRow())

            #enregistrement de l'historique
            self.save_history_data()
        except:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Erreur !")
            msg.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
            msg.setText("Aucun élément sélectionné !")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        
    def delete_whole_history(self):
        
        #supprimer tout l'historique
        
        #Boîte de dialogue 
        
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowIcon(QtGui.QIcon("icons\panneau.png"))
        box.setWindowTitle('Confirmation')
        box.setText('Voulez vous vraiment supprimer tout l\'historique ?\nCette suppression sera définitive.')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        buttonY = box.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('Oui')
        buttonN = box.button(QtWidgets.QMessageBox.No)
        buttonN.setText('Quitter')
        box.exec_()
        
        if box.clickedButton() == buttonY :
            
            self.history_table.setRowCount(0)
            
        elif box.clickedButton() == buttonN:
            
            box.close()
            
        #enregistrement de l'historique
        self.save_history_data()
        
    def search(self, search_entry_zone, table):
        
        designation_to_search = search_entry_zone.text().lower()
        
        for row in range(table.rowCount()):
            
            item = table.item(row, 1)
            
            table.setRowHidden(row, designation_to_search not in item.text().lower()) #masquer la ligne qui ne comporte pas l'élément recherché
            
    def sort_eq(self):
        
        #fontion de tri des équipements dans l'onglet tri et statistiques
        
        self.eq_list_afficher.clear() #réinitialisation de la liste
        
        if self.optionsTri_comboBox.currentIndex() == 0: #tri par département
            
            for list_row in range(self.dep_comboBox_add.count()): #parcours des départements
                
                self.eq_list_afficher.addItem(self.dep_comboBox_add.itemText(list_row).upper())
                self.eq_list_afficher.item(self.eq_list_afficher.count()-1).setBackground(QtGui.QColor(255,255,0))
                
                for row in range(self.table_add_eq.rowCount()): #parcours des designations dans la table d'ajout 
                    
                    if self.table_add_eq.item(row, 4).text() == self.dep_comboBox_add.itemText(list_row):
                        
                        self.eq_list_afficher.addItem(self.table_add_eq.item(row, 1).text())
                        
        elif self.optionsTri_comboBox.currentIndex() == 1 : #tri par ordre alphabétique
        
            my_designation_list = []
            
            for row in range(self.table_add_eq.rowCount()): #obtenir la liste des désignations
                
                my_designation_list.append(self.table_add_eq.item(row,1).text().lower())
            
            my_designation_list.sort() #tri de la liste
            
            for equipement in my_designation_list: #ajouter les éléments de la liste triée au listWidget dans le même ordre
                
                self.eq_list_afficher.addItem(equipement)
                
    def draw_graph(self):
        
        if self.optionsGraph_comboBox.currentIndex() == 0: #graphe du nombre d'équipements en fonction du département

            total_quantities = [0 for i in range(self.dep_comboBox_add.count())]

            for list_row in range(self.dep_comboBox_add.count()):
                # parcours des éléments de la table d'ajout d'équipement
                for row in range(self.table_add_eq.rowCount()):
                    
                    if self.table_add_eq.item(row,4).text() == self.dep_comboBox_add.itemText(list_row):
                        
                        total_quantities[list_row] += 1

            fig = plt.figure(figsize = (12,6))
            man = plt.get_current_fig_manager()
            man.set_window_title('Nombre d\'équipements par département')
            plt.grid(linewidth = 0.2)
            plt.bar([self.dep_comboBox_add.itemText(i) for i in range(self.dep_comboBox_add.count())],total_quantities, width = 0.5)
            plt.xlabel("Départements")
            plt.ylabel("Nombre d'équipements")
            plt.show()

        elif self.optionsGraph_comboBox.currentIndex() == 1 : #graphe du prix total des équipements par département

            total_cost = [0 for i in range(self.dep_comboBox_add.count())]

            for list_row in range(self.dep_comboBox_add.count()):

                for row in range(self.table_add_eq.rowCount()):

                    if self.table_add_eq.item(row, 4).text() == self.dep_comboBox_add.itemText(list_row):

                        total_cost[list_row] += int(self.table_add_eq.item(row, 2).text())*float(self.table_add_eq.item(row, 3).text().rstrip(' Dh'))

            fig = plt.figure(figsize=(12, 6))
            man = plt.get_current_fig_manager()
            man.set_window_title('Prix total des équipements par département')
            plt.grid(linewidth=0.2)
            plt.bar([self.dep_comboBox_add.itemText(i) for i in range(self.dep_comboBox_add.count())], total_cost, width=0.5)
            plt.xlabel("Départements")
            plt.ylabel("Prix total des équipements")
            plt.show()

    def open_help(self):

        self.helpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_help_window()
        self.ui.setupUi(self.helpWindow)
        self.helpWindow.show()


    def retranslateUi(self, second_window):
        
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "HestimLab's Devices and Tools Management System"))
        self.label_designation_add.setText(_translate("second_window", "Désignation:"))
        item = self.table_add_eq.horizontalHeaderItem(0)
        item.setText(_translate("second_window", "ID"))
        item = self.table_add_eq.horizontalHeaderItem(1)
        item.setText(_translate("second_window", "Désignation"))
        item = self.table_add_eq.horizontalHeaderItem(2)
        item.setText(_translate("second_window", "Quantité"))
        item = self.table_add_eq.horizontalHeaderItem(3)
        item.setText(_translate("second_window", "Prix unitaire"))
        item = self.table_add_eq.horizontalHeaderItem(4)
        item.setText(_translate("second_window", "Département"))
        self.label_quantite_add.setText(_translate("second_window", "Quantité:"))
        self.label_prix_add.setText(_translate("second_window", "Prix unitaire:"))
        self.label_dep_add.setText(_translate("second_window", "Département:"))
        self.dep_comboBox_add.setItemText(0, _translate("second_window", "Chimie"))
        self.dep_comboBox_add.setItemText(1, _translate("second_window", "Electricité-Automatisme"))
        self.dep_comboBox_add.setItemText(2, _translate("second_window", "Génie Civil"))
        self.dep_comboBox_add.setItemText(3, _translate("second_window", "Hydraulique-Pneumatique"))
        self.dep_comboBox_add.setItemText(4, _translate("second_window", "Mécanique"))
        self.dep_comboBox_add.setItemText(5, _translate("second_window", "SFC"))
        self.label_add_eq.setText(_translate("second_window", "Veuillez renseigner les informations suivantes :"))
        self.eq_add_button.setText(_translate("second_window", "Ajouter"))
        self.gestion_eq_tabWidget.setTabText(self.gestion_eq_tabWidget.indexOf(self.tab_add_eq), _translate("second_window", "    Ajouter un équipement    "))
        self.eq_suppress_button.setText(_translate("second_window", "Supprimer"))
        self.table_export_button.setText(_translate("second_window", "Exporter la table"))
        self.label_recherche_supress.setText(_translate("second_window", "Rechercher:"))
        item = self.table_suppress_eq.horizontalHeaderItem(0)
        item.setText(_translate("second_window", "ID"))
        item = self.table_suppress_eq.horizontalHeaderItem(1)
        item.setText(_translate("second_window", "Désignation"))
        item = self.table_suppress_eq.horizontalHeaderItem(2)
        item.setText(_translate("second_window", "Quantité"))
        item = self.table_suppress_eq.horizontalHeaderItem(3)
        item.setText(_translate("second_window", "Prix unitaire"))
        item = self.table_suppress_eq.horizontalHeaderItem(4)
        item.setText(_translate("second_window", "Département"))
        self.gestion_eq_tabWidget.setTabText(self.gestion_eq_tabWidget.indexOf(self.tab_suppress_eq), _translate("second_window", "  Supprimer équipement - Exporter  "))
        item = self.table_modify_eq.horizontalHeaderItem(0)
        item.setText(_translate("second_window", "ID"))
        item = self.table_modify_eq.horizontalHeaderItem(1)
        item.setText(_translate("second_window", "Désignation"))
        item = self.table_modify_eq.horizontalHeaderItem(2)
        item.setText(_translate("second_window", "Quantité"))
        item = self.table_modify_eq.horizontalHeaderItem(3)
        item.setText(_translate("second_window", "Prix unitaire"))
        item = self.table_modify_eq.horizontalHeaderItem(4)
        item.setText(_translate("second_window", "Département"))
        self.label_modify_eq.setText(_translate("second_window", "Sélectionnez un équipement renseignez les champs:"))
        self.label_designation_modify.setText(_translate("second_window", "Désignation:"))
        self.label_prix_modify.setText(_translate("second_window", "Prix unitaire:"))
        self.label_quantite_modify.setText(_translate("second_window", "Quantité:"))
        self.label_dep_modify.setText(_translate("second_window", "Département:"))
        self.eq_modify_button.setText(_translate("second_window", "Modifier"))
        self.dep_comboBox_modify.setItemText(0, _translate("second_window", "Chimie"))
        self.dep_comboBox_modify.setItemText(1, _translate("second_window", "Electricité-Automatisme"))
        self.dep_comboBox_modify.setItemText(2, _translate("second_window", "Génie Civil"))
        self.dep_comboBox_modify.setItemText(3, _translate("second_window", "Hydraulique-Pneumatique"))
        self.dep_comboBox_modify.setItemText(4, _translate("second_window", "Mécanique"))
        self.dep_comboBox_modify.setItemText(5, _translate("second_window", "SFC"))
        self.label_recherche_modify.setText(_translate("second_window", "Rechercher:"))
        self.gestion_eq_tabWidget.setTabText(self.gestion_eq_tabWidget.indexOf(self.tab_modify_eq), _translate("second_window", "   Modifier des spécifications   "))
        self.label_trier.setText(_translate("second_window", "Trier par : "))
        self.optionsTri_comboBox.setItemText(0, _translate("second_window", "Départements"))
        self.optionsTri_comboBox.setItemText(1, _translate("second_window", "Désignation(ordre alphabétique)"))
        self.get_graph_button.setText(_translate("second_window", "Obtenir des Stats"))
        self.optionsGraph_comboBox.setItemText(0, _translate("second_window", "Nombre d\'équipements par départements "))
        self.optionsGraph_comboBox.setItemText(1, _translate("second_window", "Prix total d\'équipements par départements"))
        self.gestion_eq_tabWidget.setTabText(self.gestion_eq_tabWidget.indexOf(self.tab_stat_eq), _translate("second_window", "       Tri et Statistiques        "))
        self.app_tabWidget.setTabText(self.app_tabWidget.indexOf(self.tab_gestion_eq), _translate("second_window", "              Gestion des équipements             "))
        self.user_add_button.setText(_translate("second_window", "Ajouter"))
        self.username2.setText(_translate("second_window", "Nom d\'utilisateur:"))
        self.password2.setText(_translate("second_window", "Mot de passe:"))
        self.gestion_user_tabWidget.setTabText(self.gestion_user_tabWidget.indexOf(self.tab_add_user), _translate("second_window", "                            Ajouter un utilisateur                          "))
        self.user_suppress_button.setText(_translate("second_window", "Supprimer"))
        self.gestion_user_tabWidget.setTabText(self.gestion_user_tabWidget.indexOf(self.tab_suppress_user), _translate("second_window", "                             Supprimer un utilisateur                              "))
        self.app_tabWidget.setTabText(self.app_tabWidget.indexOf(self.tab_gestion_user), _translate("second_window", "               Gestion des utilisateurs               "))
        item = self.history_table.horizontalHeaderItem(0)
        item.setText(_translate("second_window", "Date"))
        item = self.history_table.horizontalHeaderItem(1)
        item.setText(_translate("second_window", "Nature de l\'action"))
        item = self.history_table.horizontalHeaderItem(2)
        item.setText(_translate("second_window", "Utilisateur"))
        self.clean_button.setText(_translate("second_window", "Effacer l\'historique"))
        self.element_suppress_button.setText(_translate("second_window", "Effacer l\'élément"))
        self.app_tabWidget.setTabText(self.app_tabWidget.indexOf(self.tab_history), _translate("second_window", "                  Historique                  "))
        self.titre.setText(_translate("second_window", "          Système de gestion des équipements du laboratoire HESTIM"))
        self.app_quit_button.setText(_translate("second_window", "Quitter"))
        self.help_button.setText(_translate("second_window", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
