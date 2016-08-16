
# coding: utf8

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class InformDialog(QDialog):
    def __init__(self, message, parent=None):
        super(InformDialog, self).__init__(parent)
        self.message = message
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedHeight(150)
        self.setFixedWidth(300)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 260, 75))
        self.label.setText(_fromUtf8("%s" % self.message))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.setWindowTitle(_translate("Dialog", "Inform", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.accept)


class ConfirmDialog(QDialog):
    def __init__(self, message, parent=None):
        super(ConfirmDialog, self).__init__(parent)
        self.message = message
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedHeight(150)
        self.setFixedWidth(300)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 110, 100, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 260, 75))
        self.label.setText(_fromUtf8("%s" % self.message))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.setWindowTitle(_translate("Dialog", "Confirm action", None))
        self.pushButton.setText(_translate("Dialog", "Yes", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.reject)


class ExitDialog(QDialog):
    def __init__(self, parent=None):
        super(ExitDialog, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedHeight(150)
        self.setFixedWidth(300)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 110, 100, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 260, 75))
        self.label.setText(_fromUtf8("If you close the program you won't receive notifications!"
                                     " You can minimize instead."))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.setWindowTitle(_translate("Dialog", "Confirm exit", None))
        self.pushButton.setText(_translate("Dialog", "Exit", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.reject)


class EditPersonDialog(QDialog):
    def __init__(self, name=None, date=None, parent=None):
        super(EditPersonDialog, self).__init__(parent)
        self.name = name
        self.date = date
        self.setObjectName(_fromUtf8("Dialog"))
        self.setFixedHeight(200)
        self.setFixedWidth(360)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 340, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.dateEdit = QtGui.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(10, 105, 110, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy", None))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 17, 66, 17))
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 82, 71, 17))
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 100, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.setWindowTitle(_translate("Dialog", "Edit person", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_2.setText(_translate("Dialog", "Birth date", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))

        self.lineEdit.setText('%s' % self.name)
        self.qdate_obj = QtCore.QDate()
        self.qdate_obj.setDate(date.year, date.month, date.day)
        self.dateEdit.setDate(self.qdate_obj)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.save_button)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.reject)

    def save_button(self):
        self.name = str(self.lineEdit.text())
        self.date = self.dateEdit.date().toPyDate()
        self.accept()


class EditGiftDialog(QDialog):
    def __init__(self, gift, parent=None):
        super(EditGiftDialog, self).__init__(parent)
        self.gift = gift
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(360, 185)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 17, 66, 17))
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 145, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 145, 100, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 340, 78))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setText('%s' % self.gift)
        self.setWindowTitle(_translate("Dialog", "Edit gift", None))
        self.label.setText(_translate("Dialog", "Gift", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.save_button)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.reject)

    def save_button(self):
        self.gift = str(self.textEdit.toPlainText())
        self.accept()
