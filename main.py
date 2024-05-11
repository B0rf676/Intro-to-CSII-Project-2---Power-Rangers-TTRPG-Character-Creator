from MainMenuLogic import *
from CharMakerLogic import *
from CharSheetLogic import *
from PyQt6.QtWidgets import *

def main():
    application = QApplication([])
    window = MenuLogic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()