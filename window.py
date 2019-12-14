import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox, QCheckBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.uic.properties import QtGui

class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyQt Tuts')

        extractAction = QAction('&Get to the choppah', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        openEditor = QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction)

        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        
        self.home()

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        checkBox = QCheckBox('Enlarge window', self)
        checkBox.move(0,20)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.show()
    
    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
    
    def close_application(self):
        choice = QMessageBox.question(self, 'Message',
                                        "Are you sure to quit?", QMessageBox.Yes |
                                        QMessageBox.No, QMessageBox.No)
        
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()