from PyQt6.QtWidgets import *
from PRTTRPG_mainmenu import *
from PRTTRPG_CharMaker import Ui_MainWindow1
from PRTTRPG_CharSheet import Ui_MainWindow2
from CharSheetLogic import *
from CharMakerLogic import *


class MenuLogic(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.NewChar.clicked.connect(self.NewCharacter)
        
        self.LoadChar.clicked.connect(self.LoadCharacter)
        
    def NewCharacter(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui2 = MakerLogic()
        
        self.ui2.__init__()
        self.ui2.show()
        
    
    def LoadCharacter(self):
        name = self.CharSearch.toPlainText().strip()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui2 = SheetLogic(name)
        
        self.ui2.__init__(name)
        self.ui2.show()