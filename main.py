from src.core.scene import Scene

from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from src.enums import DisplayMode

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.window = QtWidgets.QWidget()
        
        self.scene = Scene(self.window)
        self.view = QtWidgets.QGraphicsView(self.scene, self.window)
  

        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.view)

        # add button to change mode
        self.button = QtWidgets.QPushButton("Change Mode")
        self.button.clicked.connect(self.change_mode)

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([mode.name for mode in DisplayMode])
        self.combo.currentIndexChanged.connect(self.change_mode)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.combo)




        self.window.setLayout(self.layout)

        self.setCentralWidget(self.window)

        self.show()

    def change_mode(self):
        mode = self.combo.currentText()
        self.scene.set_mode(DisplayMode[mode])

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec()