
import sys
import datetime
import pynotify
import bbox_db
import bbox_ui
import locale
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QVariant, QAbstractListModel, Qt
from PyQt4.QtGui import QDialog, QMainWindow
from PyQt4.QtCore import QThread


DB_FILE_NAME = 'bbox_db.ini'

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


class MainWindow(QMainWindow):
    def __init__(self, database, parent=None):
        super(MainWindow, self).__init__(parent)
        self.database = database
        self.birthday_manager = bbox_db.BirthdayManager(self.database)
        self.setting_manager = bbox_db.SettingsManager(self.database)
        self.setObjectName(_fromUtf8("MainWindow"))
        self.window_icon = QtGui.QIcon('launcher.png')
        self.setWindowIcon(self.window_icon)
        self.setFixedHeight(470)
        self.setFixedWidth(505)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setWindowTitle(_fromUtf8("Birthday box"))
        self.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 505, 406))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(0, 35, 501, 150))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 200, 500, 120))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setMargin(3)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 117, 17))
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listView_2 = QtGui.QListView(self.tab_2)
        self.listView_2.setGeometry(QtCore.QRect(0, 35, 500, 292))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 340, 98, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 340, 98, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(393, 340, 98, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 12, 84, 17))
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton = QtGui.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(325, 12, 62, 22))
        self.radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(392, 12, 72, 22))
        self.radioButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(261, 13, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(383, 340, 107, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 340, 98, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.spinBox = QtGui.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(30, 90, 60, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 140, 60, 27))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.checkBox = QtGui.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 200, 103, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 250, 134, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(100, 145, 134, 17))
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(100, 95, 172, 17))
        self.label_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox_3 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_3.setGeometry(QtCore.QRect(30, 40, 60, 27))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(100, 45, 208, 17))
        self.label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(419, 10, 71, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(393, 10, 100, 27))
        self.radioButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.pushButton.setText(_translate("MainWindow", "Edit gift", None))
        self.label.setText(_translate("MainWindow", "Select event to see datails", None))
        self.label_2.setText(_translate("MainWindow", "Upcoming events", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add date", None))
        self.pushButton_5.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_6.setText(_translate("MainWindow", "Remove", None))
        self.label_3.setText(_translate("MainWindow", "Birthday list", None))
        self.radioButton.setText(_translate("MainWindow", "date", None))
        self.radioButton_2.setText(_translate("MainWindow", "name", None))
        self.label_4.setText(_translate("MainWindow", "Sort by:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Birhtday list", None))
        self.pushButton_3.setText(_translate("MainWindow", "Apply settings", None))
        self.pushButton_7.setText(_translate("MainWindow", "Reset", None))
        self.checkBox.setText(_translate("MainWindow", "Auto start", None))
        self.checkBox_2.setText(_translate("MainWindow", "Start minimized", None))
        self.label_5.setText(_translate("MainWindow", "Remind every, min.", None))
        self.label_6.setText(_translate("MainWindow", "Remind times a day limit", None))
        self.label_7.setText(_translate("MainWindow", "Start reminding when days left", None))
        self.pushButton_8.setText(_translate("MainWindow", "About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Settings", None))
        self.pushButton_2.setText(_translate("MainWindow", "Minimize", None))
        self.tray_icon = QtGui.QSystemTrayIcon(self)
        self.tray_ico = QtGui.QIcon('tray.png')
        self.tray_icon.setIcon(self.tray_ico)
        self.tray_menu = QtGui.QMenu(self)
        self.tray_action_restore = QtGui.QAction('Restore', self)
        self.tray_action_show = QtGui.QAction('Show upcoming events', self)
        self.tray_menu.addAction(self.tray_action_restore)
        self.tray_menu.addAction(self.tray_action_show)
        self.tray_icon.setContextMenu(self.tray_menu)

        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        self.update_person_list()
        self.update_events_list()

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.minimize_button)
        QtCore.QObject.connect(self.tray_action_restore, QtCore.SIGNAL('triggered()'), self.tray_restore)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), self.about_button)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.add_person_button)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.edit_person_button)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.delete_person_button)

    def minimize_button(self):
        self.hide()
        self.tray_icon.show()

    def tray_restore(self):
        self.show()
        self.tray_icon.hide()

    def closeEvent(self, event):  # Program close event catch and override
        exit_dialog = bbox_ui.ExitDialog()
        if not exit_dialog.exec_():
            event.ignore()

    def about_button(self):
        message = 'CREDITS \n Idea - EvaLeo \n Code - Lax-T'
        inform_dialog = bbox_ui.InformDialog(message)
        inform_dialog.exec_()

    def add_person_button(self):
        add_person_dialog = bbox_ui.EditPersonDialog(name='', date=datetime.datetime.now())
        if add_person_dialog.exec_():
            self.birthday_manager.add_person(add_person_dialog.name, add_person_dialog.date)
        self.update_person_list()
        self.update_events_list()

    def edit_person_button(self):
        row_selected = self.listView_2.currentIndex().row()
        person_list = self.birthday_manager.get_person_list()
        add_person_dialog = bbox_ui.EditPersonDialog(name=person_list[row_selected][0],
                                                     date=person_list[row_selected][1])
        if add_person_dialog.exec_():
            confirm_dialog = bbox_ui.ConfirmDialog('Save changes?')
            if confirm_dialog.exec_():
                self.birthday_manager.edit_person(oldname=person_list[row_selected][0],
                                                  newname=add_person_dialog.name,
                                                  date=add_person_dialog.date)
        self.update_person_list()
        self.update_events_list()

    def delete_person_button(self):
        row_selected = self.listView_2.currentIndex().row()
        person_list = self.birthday_manager.get_person_list()
        confirm_dialog = bbox_ui.ConfirmDialog('Remove %s \n from list?' % person_list[row_selected][0])
        if confirm_dialog.exec_():
            self.birthday_manager.remove_person(person_list[row_selected][0])
        self.update_person_list()
        self.update_events_list()

    def update_person_list(self):
        person_list = self.birthday_manager.get_person_list()
        list_data = []
        for person_data in person_list:
            list_data.append('%s - %s' % (person_data[1].strftime('%d %b %Y'), person_data[0]))
        person_list_model = ListModel(list_data, '')
        self.listView_2.setModel(person_list_model)

    def update_events_list(self):
        event_list = self.birthday_manager.get_next_birthdays()
        list_data = []
        for name in event_list:
            date, gift = self.birthday_manager.get_person_details(name)
            list_data.append('%s - %s' % (date.strftime('%d %b %Y'), name))
        event_list_model = ListModel(list_data, '')
        self.listView.setModel(event_list_model)


class ListModel(QAbstractListModel):  # Modified but 80% class code from internet
    def __init__(self, datain, headerdata, parent=None, *args):

        QAbstractListModel.__init__(self, parent)
        self.array_data = datain
        self.header_data = headerdata

    def rowCount(self, parent=None, *args):
        return len(self.array_data)

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(u"%s" % self.array_data[index.row()])

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()


if __name__ == '__main__':
    main_database = bbox_db.MainBD(DB_FILE_NAME)
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow(main_database)
    main_window.show()
    sys.exit(app.exec_())