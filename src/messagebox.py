import PyQt5.QtWidgets

def info(title : str, text : str):
    a = PyQt5.QtWidgets.QMessageBox()
    a.setText(text)
    a.setWindowTitle(title)
    a.setIcon(PyQt5.QtWidgets.QMessageBox.Icon.Information)
    return a