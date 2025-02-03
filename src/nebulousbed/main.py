import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QVBoxLayout, QPushButton, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Nebulous Bed - The PalmSens Measurement Name Generator')
        #self.setWindowIcon()
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: white;")
        
        self.layout = QGridLayout()

        self.electrodeWidgetLayout = QGridLayout()
        self.electrodeWidget = QtWidgets.QWidget()

            
        self.electrodeMaterial = QtWidgets.QWidget()
        self.electrodeMaterialLayout = QVBoxLayout()
        
        self.PtButton = QPushButton(text = 'Pt')
        self.PtButton.clicked.connect(lambda: self.electrodeUpdate('Pt'))

        self.AuButton = QPushButton(text = 'Au')
        self.AuButton.clicked.connect(lambda: self.electrodeUpdate('Au'))
       
        '''Electrodes'''
        self.electrodeMaterial.addWidget(self.PtButton)
        
        '''Procedures'''
        self.electrodeMaterialLayout.addWidget(self.AuButton)

        self.electrodeMaterialLayout.setLayout(self.electrodeMaterialLayout)

        self.electrodeWidget.addWidget(self.electrodeMaterial)

        

        '''procedureLayout = QGridLayout()
        procedureType = QVBoxLayout()
        procedureSettings = QVBoxLayout()

        solutionLayout = QGridLayout()
        solutionType = QVBoxLayout()'''


        #self.textEntry = QLineEdit()
        
        #self.copyButton = QPushButton(text = 'Copy')
        #self.copyButton.clicked.connect(lambda: clipbooard.setText(self.textEntry.text()))
        


        
        '''Solution'''

        '''Text Box'''
        #self.layout.addWidget(self.textEntry, 3, 1, 1, 1)

        '''Copy and Clear Buttons'''
        #self.layout.addWidget(self.copyButton, 4, 1, 1, 1)
        
        widget = QtWidgets.QWidget()
        self.layout.addWidget(self.electrodeWidget, 0, 0, 1, 1)
        
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)
        
        self.show()
    def electrodeUpdate(self, material):
        if material == 'Pt':
            self.textEntry.setText('Pt')
        elif material == 'Au':
            self.textEntry.setText('Au')

app = QApplication(sys.argv)
clipbooard = app.clipboard()
MainWindow()
sys.exit(app.exec_())