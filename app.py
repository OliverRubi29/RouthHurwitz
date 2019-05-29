import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from design import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.show()
        self.coeff = []

        self.readInput()
        self.ui.clearBtn.clicked.connect(self.ui.inputFld.clear)

    def readInput(self):
        self.ui.inputFld.returnPressed.connect(self.validateInput)
        self.ui.solveBtn.clicked.connect(self.validateInput)

    def validateInput(self):
        pre_input = self.ui.inputFld.text()
        self.coeff.clear()

        try:
            for entry in pre_input.split(","):
                if "." in entry:
                    self.coeff.append(float(entry.strip()))
                else:
                    self.coeff.append(int(entry.strip()))
            self.solve()

        except ValueError:
            print("wait a minute")
            self.showInputError()

        # print(pre_input.split(","))

    def showInputError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Oops")
        msg.setText("Your input is invalid!\nPlease input coefficients in descending order separated by comma.")
        msg.exec()

    def solve(self):
        row = len(self.coeff)
        coeff = self.coeff
        col = 0

        if row%2 == 0:
            col = row/2 + 1
        else:
            col = row/2

        table = [[0 for x in range(int(col))] for y in range(int(row))]
        print(table)
        for num in coeff:
            x=0
            y=0
            if y in range(2):
                table[x][y] = num
                y = y + 1
            else:
                x = x+1

        print(table)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
