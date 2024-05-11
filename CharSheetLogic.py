from PyQt6.QtWidgets import *
from PRTTRPG_CharSheet import *
from PRTTRPG_mainmenu import*
import csv

class SheetLogic(QMainWindow,Ui_MainWindow2):
    
    def __init__(self,name):
        super().__init__()
        self.setupUi(self)
        CharName = name
        
        with open('Rangers.csv') as csvfile:
            CharDataL = []
            CharDataS = []
            
            CharData = csv.reader(csvfile, delimiter = ',')
            
            for row in CharData:
                CharDataL.append(row)
            
            CharDataL = filter(None, CharDataL)

            for item in CharDataL:
                if item == None:
                    pass
                elif item[0] != CharName:
                    pass
                elif item[0] == CharName:
                    CharDataS.append(item)
                
                
            self.CharNDisplay.setText(CharDataS[0][0])
            self.CharRCDisplay.setText(CharDataS[0][1])
            self.CharRADisplay.setText(f'{CharDataS[0][2]} - {CharDataS[0][3]}')
            self.CharLDisplay.setText(f'Level: {CharDataS[0][4]}')
            self.CharODisplay.setText(f'Origin: {CharDataS[0][5]}')
            self.CharODescDisplay.setText(CharDataS[0][6])
            self.CharHDisplay.setText(CharDataS[0][7])
            self.CharMSDisplay.setText(CharDataS[0][8])
            self.CharPDisplay.setText(CharDataS[0][9])
            self.CharStrDisplay.setText(f'Strength: {CharDataS[0][10]}')
            self.CharSpdDisplay.setText(f'Speed: {CharDataS[0][11]}')
            self.CharSmrtDisplay.setText(f'Smarts: {CharDataS[0][12]}')
            self.CharSocDisplay.setText(f'Social: {CharDataS[0][13]}')
            self.CharToughDisplay.setText(f'Toughness: {CharDataS[0][14]}')
            self.CharMToughDisplay.setText(f'Morphed: {CharDataS[0][15]}')
            self.CharEvaDisplay.setText(f'Evasion: {CharDataS[0][16]}')
            self.CharMEvaDisplay.setText(f'Morphed: {CharDataS[0][17]}')
            self.CharWillDisplay.setText(f'Willpower: {CharDataS[0][18]}')
            self.CharMWillDisplay.setText(f'Morphed: {CharDataS[0][19]}')
            self.CharClevDisplay.setText(f'Cleverness: {CharDataS[0][20]}')
            self.CharMClevDisplay.setText(f'Morphed: {CharDataS[0][21]}')
            