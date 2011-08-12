# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtbe/resources/mainwindow.ui'
#
# Created: Fri Aug 12 13:57:28 2011
#      by: pyside-uic 0.2.9 running on PySide 1.0.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 644)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mainBox = QtGui.QGroupBox(self.centralwidget)
        self.mainBox.setFlat(False)
        self.mainBox.setObjectName("mainBox")
        self.gridLayout = QtGui.QGridLayout(self.mainBox)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.projectTitle = QtGui.QLabel(self.mainBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectTitle.sizePolicy().hasHeightForWidth())
        self.projectTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.projectTitle.setFont(font)
        self.projectTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.projectTitle.setObjectName("projectTitle")
        self.gridLayout.addWidget(self.projectTitle, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.mainBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 2)
        self.issueTable = QtGui.QTableView(self.layoutWidget)
        self.issueTable.setAlternatingRowColors(True)
        self.issueTable.setObjectName("issueTable")
        self.gridLayout_3.addWidget(self.issueTable, 1, 0, 1, 3)
        self.newIssueBox = QtGui.QGroupBox(self.layoutWidget)
        self.newIssueBox.setObjectName("newIssueBox")
        self.newCommentGrid_2 = QtGui.QGridLayout(self.newIssueBox)
        self.newCommentGrid_2.setObjectName("newCommentGrid_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.newCommentGrid_2.addItem(spacerItem, 1, 0, 1, 1)
        self.saveIssueButton = QtGui.QPushButton(self.newIssueBox)
        self.saveIssueButton.setObjectName("saveIssueButton")
        self.newCommentGrid_2.addWidget(self.saveIssueButton, 1, 1, 1, 1)
        self.newIssueEdit = QtGui.QLineEdit(self.newIssueBox)
        self.newIssueEdit.setObjectName("newIssueEdit")
        self.newCommentGrid_2.addWidget(self.newIssueEdit, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.newIssueBox, 2, 0, 1, 3)
        self.newIssueButton = QtGui.QPushButton(self.layoutWidget)
        self.newIssueButton.setCheckable(True)
        self.newIssueButton.setObjectName("newIssueButton")
        self.gridLayout_3.addWidget(self.newIssueButton, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.addCommentButton = QtGui.QPushButton(self.layoutWidget)
        self.addCommentButton.setCheckable(True)
        self.addCommentButton.setChecked(False)
        self.addCommentButton.setDefault(False)
        self.addCommentButton.setFlat(False)
        self.addCommentButton.setObjectName("addCommentButton")
        self.gridLayout_3.addWidget(self.addCommentButton, 3, 2, 1, 1)
        self.issueSortCombo = QtGui.QComboBox(self.layoutWidget)
        self.issueSortCombo.setObjectName("issueSortCombo")
        self.gridLayout_3.addWidget(self.issueSortCombo, 0, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)
        self.vcsLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.vcsLabel.setFont(font)
        self.vcsLabel.setText("")
        self.vcsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vcsLabel.setObjectName("vcsLabel")
        self.gridLayout_3.addWidget(self.vcsLabel, 4, 1, 1, 2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.issueTitle = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.issueTitle.setFont(font)
        self.issueTitle.setObjectName("issueTitle")
        self.verticalLayout.addWidget(self.issueTitle)
        self.issueCommentList = QtGui.QListWidget(self.layoutWidget1)
        self.issueCommentList.setObjectName("issueCommentList")
        self.verticalLayout.addWidget(self.issueCommentList)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.issueDetailsBox = QtGui.QGroupBox(self.layoutWidget1)
        self.issueDetailsBox.setFlat(False)
        self.issueDetailsBox.setCheckable(False)
        self.issueDetailsBox.setObjectName("issueDetailsBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.issueDetailsBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.shortLabel = QtGui.QLabel(self.issueDetailsBox)
        self.shortLabel.setText("")
        self.shortLabel.setObjectName("shortLabel")
        self.gridLayout_2.addWidget(self.shortLabel, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 2, 1, 1)
        self.idLabel = QtGui.QLabel(self.issueDetailsBox)
        self.idLabel.setText("")
        self.idLabel.setObjectName("idLabel")
        self.gridLayout_2.addWidget(self.idLabel, 0, 3, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.statusCombo = QtGui.QComboBox(self.issueDetailsBox)
        self.statusCombo.setObjectName("statusCombo")
        self.horizontalLayout_4.addWidget(self.statusCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.severityCombo = QtGui.QComboBox(self.issueDetailsBox)
        self.severityCombo.setObjectName("severityCombo")
        self.horizontalLayout_5.addWidget(self.severityCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.milestoneCombo = QtGui.QComboBox(self.issueDetailsBox)
        self.milestoneCombo.setObjectName("milestoneCombo")
        self.horizontalLayout_6.addWidget(self.milestoneCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.assignedCombo = QtGui.QComboBox(self.issueDetailsBox)
        self.assignedCombo.setObjectName("assignedCombo")
        self.horizontalLayout_7.addWidget(self.assignedCombo)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 3, 1, 2)
        self.saveDetailsButton = QtGui.QPushButton(self.issueDetailsBox)
        self.saveDetailsButton.setObjectName("saveDetailsButton")
        self.gridLayout_2.addWidget(self.saveDetailsButton, 4, 0, 1, 1)
        self.discardDetailsButton = QtGui.QPushButton(self.issueDetailsBox)
        self.discardDetailsButton.setObjectName("discardDetailsButton")
        self.gridLayout_2.addWidget(self.discardDetailsButton, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)
        self.reporterLabel = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.reporterLabel.setFont(font)
        self.reporterLabel.setText("")
        self.reporterLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reporterLabel.setObjectName("reporterLabel")
        self.gridLayout_2.addWidget(self.reporterLabel, 2, 3, 1, 2)
        self.creatorLabel = QtGui.QLabel(self.issueDetailsBox)
        self.creatorLabel.setText("")
        self.creatorLabel.setObjectName("creatorLabel")
        self.gridLayout_2.addWidget(self.creatorLabel, 1, 3, 1, 2)
        self.label_2 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.issueDetailsBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.createdLabel = QtGui.QLabel(self.issueDetailsBox)
        self.createdLabel.setText("")
        self.createdLabel.setObjectName("createdLabel")
        self.gridLayout_2.addWidget(self.createdLabel, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.issueDetailsBox)
        self.newCommentBox = QtGui.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.newCommentBox.setFont(font)
        self.newCommentBox.setObjectName("newCommentBox")
        self.newCommentGrid = QtGui.QGridLayout(self.newCommentBox)
        self.newCommentGrid.setObjectName("newCommentGrid")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.newCommentGrid.addItem(spacerItem2, 1, 0, 1, 1)
        self.saveCommentButton = QtGui.QPushButton(self.newCommentBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.saveCommentButton.setFont(font)
        self.saveCommentButton.setObjectName("saveCommentButton")
        self.newCommentGrid.addWidget(self.saveCommentButton, 1, 1, 1, 1)
        self.newCommentEdit = QtGui.QTextEdit(self.newCommentBox)
        self.newCommentEdit.setObjectName("newCommentEdit")
        self.newCommentGrid.addWidget(self.newCommentEdit, 0, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.newCommentBox)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.mainBox, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionA_bout = QtGui.QAction(MainWindow)
        self.actionA_bout.setObjectName("actionA_bout")
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.actionA_bout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.newIssueButton, QtCore.SIGNAL("toggled(bool)"), self.newIssueBox.setVisible)
        QtCore.QObject.connect(self.addCommentButton, QtCore.SIGNAL("toggled(bool)"), self.newCommentBox.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Qt Bugs Everywhere", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTitle.setText(QtGui.QApplication.translate("MainWindow", "Project Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Issues", None, QtGui.QApplication.UnicodeUTF8))
        self.newIssueBox.setTitle(QtGui.QApplication.translate("MainWindow", "Create Issue", None, QtGui.QApplication.UnicodeUTF8))
        self.saveIssueButton.setText(QtGui.QApplication.translate("MainWindow", "Save Issue", None, QtGui.QApplication.UnicodeUTF8))
        self.newIssueButton.setText(QtGui.QApplication.translate("MainWindow", "New Issue", None, QtGui.QApplication.UnicodeUTF8))
        self.addCommentButton.setText(QtGui.QApplication.translate("MainWindow", "Add Comment >>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Version Control:", None, QtGui.QApplication.UnicodeUTF8))
        self.issueTitle.setText(QtGui.QApplication.translate("MainWindow", "Issue Title", None, QtGui.QApplication.UnicodeUTF8))
        self.issueDetailsBox.setTitle(QtGui.QApplication.translate("MainWindow", "Issue Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Short Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Severity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Milestone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Assigned", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDetailsButton.setText(QtGui.QApplication.translate("MainWindow", "Save Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.discardDetailsButton.setText(QtGui.QApplication.translate("MainWindow", "Discard Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Reporter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Creator:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Created at:", None, QtGui.QApplication.UnicodeUTF8))
        self.newCommentBox.setTitle(QtGui.QApplication.translate("MainWindow", "Add New Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCommentButton.setText(QtGui.QApplication.translate("MainWindow", "Save Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">No project is open.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Please create a new project</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">or open an exisiting project</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">to view/edit/track your issues.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_bout.setText(QtGui.QApplication.translate("MainWindow", "A&bout", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))

