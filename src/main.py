from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
import ui.ui as mainui
import platform
import signals as signals

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mainui.Ui_main()

def pathSeperator():
    if platform.system() == 'Windows':
        return '\\'
    else: return '/'

def iterItems():
    for i in range(ui.videoList.count()):
        yield ui.videoList.item(i).text()

def prepare():
    global ui, MainWindow
    ui.setupUi(MainWindow)
    ui.addButton.clicked.connect(lambda: signals.getInput(ui.urlContainer.text(), ui))
    ui.delButton.clicked.connect(lambda: signals.deleteItem(ui, ui.videoList.selectedItems()))
    ui.destContainer.setText(os.getcwd() + pathSeperator())
    ui.browseButton.clicked.connect(lambda: ui.destContainer.setText(signals.destinationSelect().replace("/", pathSeperator()) + pathSeperator()))
    ui.downloadButton.clicked.connect(lambda: signals.downloadButton(ui, iterItems()))
    MainWindow.show()


prepare()
sys.exit(app.exec_())