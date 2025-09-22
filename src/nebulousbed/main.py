'''
===================================================================================================
Copyright (C) 2024 Steven Linfield

This file is part of the nebulous-bed package. This package is free software: you can 
redistribute it and/or modify it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or (at your option) any later 
version. This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details. You should have received a copy of the GNU General 
Public License along with nebulous-bed. If not, see https://www.gnu.org/licenses/
===================================================================================================

Package title:      nebulous-bed
Repository:         https://github.com/MoonshinetheP/nebulous-bed
Date of creation:   11/10/2024
Main author:        Steven Linfield (MoonshinetheP)
Collaborators:      None
Acknowledgements:   None

Filename:           main.py

===================================================================================================

Description:

.

===================================================================================================

How to use this file:
    


===================================================================================================
'''

import sys
import os
from datetime import datetime

# Import the static LoadSaveHelperFunctions
from System import Convert
from PalmSens.Windows import LoadSaveHelperFunctions
from PalmSens.Data import IDataValue
from PalmSens.Data import VoltageReading
from PalmSens.Data import CurrentReading

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QComboBox, QFileDialog, QLineEdit, QPushButton, QTabWidget, QWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Nebulous Bed - File Management Software for PalmSens Instruments')
        #self.setWindowIcon()
        self.setGeometry(150, 150, 1800, 1200)
        self.setStyleSheet("background-color: white;")

        self.layout = QVBoxLayout()

        self.tabs = QTabWidget()        
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setStyleSheet("""
            QTabBar::tab {
                min-width: 200px;
                min-height: 20px;
                max-width: 250px;
                max-height: 20px;
            }
        """)


        """ Name Generator Tab """
        self.nameTab = QWidget()

        self.nameLayout = QVBoxLayout()

        self.upArrowButton = QPushButton("↑")
        self.downArrowButton = QPushButton("↓")

        '''Electrode selection'''
        self.ChooseElectrodeFrame = QWidget()

        self.AddNewElectrodeButton = QPushButton("Add New Electrode")

        self.ElectrodeSize = QLineEdit()
        self.ElectrodeDimensionLabel = QComboBox()
        self.ElectrodeDimensionLabel.addItems(["mm", "um", "nm"])

        self.ElectrodeModification = QLineEdit()


        '''Procedure selection'''
        self.ChooseProcedureFrame = QWidget()

        self.CyclicVoltammetryButton = QPushButton("Cyclic Voltammetry")
        self.ElectrochemicalImpedanceSpectroscopyButton = QPushButton("Electrochemical Impedance Spectroscopy")
        self.PotentiometryButton = QPushButton("Potentiometry")
        self.PulseVoltammetryButton = QPushButton("Differential Pulsed Voltammetry")
        '''Solution'''

        '''Copy and Clear Buttons'''


        self.tabs.addTab(self.nameTab, 'Measurement Name Generator')


        """ Report Generator Tab """
        self.reportTab = QWidget()
        self.reportLayout = QVBoxLayout()
        


               
        self.loadbutton = QPushButton("Open File")
        self.loadbutton.clicked.connect(self.loadsession)
        self.reportLayout.addWidget(self.loadbutton)

        self.tabs.addTab(self.reportTab, 'Report Generator')


 

        











        self.dataTab = QWidget()
        self.dataLayout = QVBoxLayout()

        self.tabs.addTab(self.dataTab, 'Data Processing')


        # Add the tabs widget to the layout
        self.layout.addWidget(self.tabs)

 
        #self.setCentralWidget(self.tabs)
        # Set the layout of the FileManagement widget
        self.setCentralWidget(self.tabs)
        self.show()

    def GenerateReport(self, input):
        '''Takes one or more .pssession files selected in a file dialogue as the input and loops through each file and adds the measurement names to a txt file'''
        
        self.input = input

        for ix in self.input:

            session = LoadSaveHelperFunctions.LoadSessionFile(ix)
            file = os.path.split(ix)[1][:-10] 

            with open(f'{file} - Report.txt', 'w') as f:
        
                    for iy in session:
                        f.write(f'\t () = \'{iy.Title}\'\n')

                    f.write(f'\'{os.path.split(ix)[1]}\'')


    def ProcessData(self, input):                
        '''Takes one or more .pssession files selected in a file dialogue as the input, then returns an Origin Project with the data from each file separated into different folders and the measurements from each file loaded into individual worksheets.'''
       
        self.input = input

        for ix in self.input:
                        
            session = LoadSaveHelperFunctions.LoadSessionFile(ix)
  
            file = os.path.split(ix)[1][:-10] 


            # Loops through each measurement object in the .pssession file
            for iy in session:
                
                arrays = iy.DataSet.GetDataArrays()

                marker = datetime(iy.TimeStamp.Year, iy.TimeStamp.Month, iy.TimeStamp.Day, iy.TimeStamp.Hour, iy.TimeStamp.Minute, iy.TimeStamp.Second)

  
                values = {}
                for n in range(0, len(arrays)):
                    values.update({arrays[n].Description : []})

                # Loops through each array in the measurement object
                for iz in arrays:
                    
                    for n in range(0, iz.Count):

                        values[iz.Description].append(float(iz.get_Item(n).Value)) # need to know desription of current array

                        try:
                            extra = Convert.ChangeType(iz.get_Item(n), VoltageReading)
                            values[iz.Description].append(str(extra.Range.ToString())) # this won't work
                            values[iz.Description].append(str(extra.ReadingStatus.ToString()))                        
                        except: pass
                        
                        try:
                            extra = Convert.ChangeType(iz.get_Item(n), CurrentReading)
                            values[iz.Description].append(str(extra.CurrentRange.ToString()))
                            values[iz.Description].append(str(extra.ReadingStatus.ToString()))
                        except: pass



                    values.insert(0, f'{iz.Description}/{iz.Unit.ToString()}')
                    wks.from_list(column, values)

                    if iy.Method.ToString() == 'Electrochemical Impedance Spectroscopy':
                        pass
                    
                    if iy.Method.ToString() == 'Electrochemical Impedance Spectroscopy':    
                        pass  

                    if (psdata.ArrayType(iz.ArrayType) == psdata.ArrayType.Potential) or (psdata.ArrayType(iz.ArrayType) == psdata.ArrayType.Current):
                        try:
                            ranges.insert(0, f'{iz.Description}/{iz.Unit.ToString()}')
                            column += 1
                            wks.from_list(column, ranges)
                            status.insert(0, f'{iz.Description}/{iz.Unit.ToString()}')                        
                            column += 1
                            wks.from_list(column, status)
                        except: pass


app = QApplication(sys.argv)
clipboard = app.clipboard()
window = MainWindow()
sys.exit(app.exec_())