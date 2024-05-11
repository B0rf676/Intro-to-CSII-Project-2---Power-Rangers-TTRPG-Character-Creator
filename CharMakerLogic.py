from PyQt6.QtWidgets import *
from PRTTRPG_CharMaker import *
from abilities import*
from CharSheetLogic import SheetLogic, Ui_MainWindow2
import csv

class MakerLogic(QMainWindow,Ui_MainWindow1):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.CharOrigin.currentIndexChanged.connect(self.OriginDisplay)
        self.CharDisplay.clicked.connect(self.CreateChar)
        
    def ScoreCheck(self):
        
        scores = []
        
        ## making sure int-able values were given
        try:
            Str = int(self.textEdit.toPlainText())
            scores.append(Str)
            Spd = int(self.textEdit_2.toPlainText())
            scores.append(Spd)
            Smrt = int(self.textEdit_3.toPlainText())
            scores.append(Smrt)
            Soc = int(self.textEdit_4.toPlainText())
            scores.append(Soc)
        except ValueError:
            return False
        
        TotalScores = sum(scores)
            
        if TotalScores > 12:
            print('Base essence score total cannot exceed 12!')
            return False
        elif TotalScores < 12:
            print('Base essence score total cannot be less than 12!')
            return False
        else:
            return True

    def OriginDisplay(self):
        Origin = self.CharOrigin.currentText()
        
        if Origin == 'Choose an Origin':
            Origin_desc = "Choose an origin to procede."
        elif Origin != 'Choose an Origin':
            Origin_desc = Origins[Origin]['desc']
            
        self.CharOrDesc.setText(Origin_desc)
        
    def OriginCheck(self):
        Origin = self.CharOrigin.currentText()
        
        if Origin in Origins:
            return True
        else:
            print('Please choose a valid origin')
            return False

    def CreateChar(self):
        ## get some variables ready for storage and reading
        CharDictName = self.CharName.toPlainText().strip()
        RangerColor = self.CharRColor.currentText()
        CharLevel = int(self.CharLevel.currentText())
        ChoseOrigin = self.CharOrigin.currentText()
        
        ## check if base scores are legal
        if self.ScoreCheck() == True:
            pass
        elif self.ScoreCheck() == False:
            print('Character failed to create!')
            
        ## making sure an origin was selected
        if self.OriginCheck() == True:
            pass
        elif self.OriginCheck() == False:
            print('Character failed to create!')
            
        ## making sure a name was given
        if CharDictName == '':
            print('Please name your character')
        elif CharDictName != '':
            pass
        
        Str_final = int(self.textEdit.toPlainText()) + Levels[RangerColor][CharLevel]['strength']
        Spd_final = int(self.textEdit_2.toPlainText()) + Levels[RangerColor][CharLevel]['speed']
        Smrt_final = int(self.textEdit_3.toPlainText()) + Levels[RangerColor][CharLevel]['smarts']
        Soc_final = int(self.textEdit_4.toPlainText())+ Levels[RangerColor][CharLevel]['social']
        
        
        PersPower = Levels[RangerColor][CharLevel]['power']
        
        with open('Rangers.csv', mode='w') as csvfile:
            fieldnames = ['Name', 'Color', 'ColorPower','ColorDesc', 'Level', 'Origin', 'OriginDesc','Health', 'MoveSpeed', 'Personal Power', 'Strength', 'Speed', 'Smarts', 'Social', 'Toughness', 'MToughness', 'Evasion', 'MEvasion', 'Willpower', 'MWillpower', 'Cleverness', 'MCleverness']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow({'Name': CharDictName, 'Color':RangerColor, 'ColorPower':Power[RangerColor]['Ability'], 'ColorDesc': Power[RangerColor]['Desc'], 'Level': CharLevel, 'Origin': ChoseOrigin, 'OriginDesc': Origins[ChoseOrigin]['desc'], 'Health': Origins[ChoseOrigin]['health'], 'MoveSpeed': Origins[ChoseOrigin]['movement'], 'Personal Power': Levels[RangerColor][CharLevel]['power'], 'Strength': Str_final, 'Speed': Spd_final, 'Smarts': Smrt_final, 'Social': Soc_final, 'Toughness': Str_final + 10, 'MToughness': Str_final + 10 + 1, 'Evasion': Spd_final + 10, 'MEvasion': Spd_final + 10, 'Willpower': Smrt_final + 10, 'MWillpower': Smrt_final + 10, 'Cleverness': Soc_final + 10, 'MCleverness': Soc_final + 10})
            
        name = self.CharName.toPlainText().strip()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui2 = SheetLogic(name)
        
        self.ui2.__init__(name)
        self.ui2.show()