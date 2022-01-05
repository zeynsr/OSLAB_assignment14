from math import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader



class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.initButtons()


    def initButtons(self):
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_rem.clicked.connect(self.rem)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn1.clicked.connect(self.btn1)
        self.ui.btn2.clicked.connect(self.btn2)
        self.ui.btn3.clicked.connect(self.btn3)
        self.ui.btn4.clicked.connect(self.btn4)
        self.ui.btn5.clicked.connect(self.btn5)
        self.ui.btn6.clicked.connect(self.btn6)
        self.ui.btn7.clicked.connect(self.btn7)
        self.ui.btn8.clicked.connect(self.btn8)
        self.ui.btn9.clicked.connect(self.btn9)
        self.ui.btn0.clicked.connect(self.btn0)
        


    def add(self):
        self.state = 'add'
        self.n1 = float(self.ui.tb.text())
        self.ui.tb.setText("")

    def sub(self):
        self.state = 'sub'
        self.n1 = float(self.ui.tb.text())
        self.ui.tb.setText("")

    def mul(self):
        self.state = 'mul'
        self.n1 = float(self.ui.tb.text())
        self.ui.tb.setText("")

    def div(self):
        self.state = 'div'
        self.n1 = float(self.ui.tb.text())
        self.ui.tb.setText("")

    def rem(self):
        self.state = 'rem'
        self.n1 = float(self.ui.tb.text())
        self.ui.tb.setText("")    

    def sin(self):
        self.ui.tb.setText(str(round(sin(radians(float(self.ui.tb.text()))))))

    def cos(self):
        self.ui.tb.setText(str(round(cos(radians(float(self.ui.tb.text()))))))   

    def tan(self):
        self.ui.tb.setText(str(round(tan(radians(float(self.ui.tb.text()))))))   

    def cot(self):
        self.ui.tb.setText(str(round(1/(tan(radians(float(self.ui.tb.text())))))))     

    def log(self):
        self.ui.tb.setText(str(log10(float(self.ui.tb.text()))))

    def sqrt(self):
        self.ui.tb.setText(str(sqrt(float(self.ui.tb.text()))))      

    def equal(self):
        self.n2 = float(self.ui.tb.text())

        if self.state == "add":
            self.res = self.n1 + self.n2
            self.ui.tb.setText(str(self.res))
        elif self.state == "sub":
            self.res = self.n1 - self.n2
            self.ui.tb.setText(str(self.res))
        elif self.state == "mul":
            self.res = self.n1 * self.n2
            self.ui.tb.setText(str(self.res))
        elif self.state == "div":
            try:
                self.res = self.n1 / self.n2
                self.ui.tb.setText(str(self.res))
            except ZeroDivisionError:
                self.res = 0     
                self.ui.tb.setText('DIVISION BY ZERO ERROR')
        elif self.state == "rem":
            try:
                self.res = self.n1 % self.n2
                self.ui.tb.setText(str(self.res))
            except ZeroDivisionError:
                self.res = 0     
                self.ui.tb.setText('DIVISION BY ZERO ERROR')       

    def dot(self):
        if '.' not in self.ui.tb.text():
            self.ui.tb.setText(self.ui.tb.text() + '.')    

    def ac(self):
       self.ui.tb.setText("")
       self.res=0
       self.state = ""

    def sign(self):
        self.n2=float(self.ui.tb.text())
        self.n2 *=-1
        self.ui.tb.setText(str(self.n2))
    
    def btn1(self):
        self.ui.tb.setText(self.ui.tb.text() + "1")
    def btn2(self):
        self.ui.tb.setText(self.ui.tb.text() + "2")
    def btn3(self):
        self.ui.tb.setText(self.ui.tb.text() + "3")
    def btn4(self):
        self.ui.tb.setText(self.ui.tb.text() + "4")
    def btn5(self):
        self.ui.tb.setText(self.ui.tb.text() + "5")
    def btn6(self):
        self.ui.tb.setText(self.ui.tb.text() + "6")
    def btn7(self):
        self.ui.tb.setText(self.ui.tb.text() + "7")
    def btn8(self):
        self.ui.tb.setText(self.ui.tb.text() + "8")
    def btn9(self):
        self.ui.tb.setText(self.ui.tb.text() + "9")
    def btn0(self):
        self.ui.tb.setText(self.ui.tb.text() + "0")    



if __name__ == "__main__":
    myApp = QApplication()
    main_Window = Calculator()

    myApp.exec()