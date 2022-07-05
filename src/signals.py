#from GetYT.src.ui.ui import Ui_Form
import lxml, PyQt5.QtGui, PyQt5.QtWidgets
from downloader import Downloader, getInfo

def getInput(url : str, ui):
    
    ui.videoList.addItem(url)
    ui.urlContainer.setText("")

def deleteItem(ui, selected):
    for item in selected:
        ui.videoList.takeItem(ui.videoList.row(item))

def destinationSelect():
    return PyQt5.QtWidgets.QFileDialog.getExistingDirectory(caption='Videos Destination: ')

def downloadButton(ui, items):
    dest = ui.destContainer.text()
    urls = tuple(items)
    a = Downloader(urls, dest, ui)
    a.download_all()
