import sys

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUV"


# Функция для перевода целой части числа в другую систему счисления
def to_int(num, to_base):
    n = abs(num)
    s = []

    while not (n < to_base):
        s.append(alphabet[n % to_base])
        n //= to_base
    else:
        s.append(alphabet[n])
        s.reverse()

    return ('' if num >= 0 else '-') + ''.join(s)


# Функция для перевода дробной части числа в другую систему счисления
def to_float(frac, base, n=16):
    s = []

    while n:
        frac *= base
        frac = round(frac, n)
        s.append(str(alphabet[int(frac)]))
        frac -= int(frac)
        n -= 1

    return ''.join(s)


# Функция для перевода всего числа в другую систему счисления
def convert_base(number, to_base=10, from_base=10):
    if '.' in number:
        num, frac = map(str, number.split('.'))
        num = int(num, from_base)
        a = to_int(num, to_base)
        b = 0
        k = from_base
        for i in frac:
            b += alphabet.index(i) / k
            k *= from_base
        b = str(to_float(b, to_base)).rstrip('0')
        return a + '.' + b
    else:
        return to_int(int(number, from_base), to_base)


class Calculator_NS(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.number = ''  # нынешнее число
        self.f = True  # флажок начала
        self.bases = [str(el) for el in range(2, 33)] # Список доступных СС
        self.base = '10' # Начальная СС
        self.last_base = self.base

        # Список кнопок с цифрами
        self.buttons = [self.btn_0,
                   self.btn_1,
                   self.btn_2,
                   self.btn_3,
                   self.btn_4,
                   self.btn_5,
                   self.btn_6,
                   self.btn_7,
                   self.btn_8,
                   self.btn_9,
                   self.btn_A,
                   self.btn_B,
                   self.btn_C,
                   self.btn_D,
                   self.btn_E,
                   self.btn_F,
                   self.btn_G,
                   self.btn_H,
                   self.btn_I,
                   self.btn_J,
                   self.btn_K,
                   self.btn_L,
                   self.btn_M,
                   self.btn_N,
                   self.btn_O,
                   self.btn_P,
                   self.btn_Q,
                   self.btn_R,
                   self.btn_S,
                   self.btn_T,
                   self.btn_U,
                   self.btn_V]

        # Список кнопок с операциями
        self.operations = [self.add,
                        self.mult,
                        self.ded,
                        self.deg,
                        self.deg_2,
                        self.mult_2,
                        self.perc]

        # Подключение
        for el in self.buttons:
            el.clicked.connect(self.click_numeral)

        for el in self.operations:
            el.clicked.connect(self.click_operation)

        self.change_notation.clicked.connect(self.convertation)

        self.btn_c.clicked.connect(self.clear)
        self.point.clicked.connect(self.add_point)
        self.ce.clicked.connect(self.click)

        self.eq.clicked.connect(self.click_output)
        self.change.clicked.connect(self.sign_change)
        self.label_base.setText(self.base)

        self.left_bkt.clicked.connect(self.click_numeral)
        self.right_bkt.clicked.connect(self.click_numeral)

        # Изменение шрифта лэйблов
        self.big_label.setAlignment(Qt.AlignRight)
        self.big_label.setFont(QFont('MS Shell Dlg 2', 25))
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('MS Shell Dlg 2', 15))
        self.label_base.setAlignment(Qt.AlignRight)
        self.label_base.setFont(QFont('MS Shell Dlg 2', 10))
        self.comboBox.addItems(self.bases)

        # Вызов функции, делающую кнопки с цифрами, большими или равными СС в данный момент, ненажимаемыми
        self.enabled()

    # Фунцкия вывода
    def click_output(self):
        if self.big_label.text() != '':
            try:
                if int(self.base) == 10:
                    self.number = str(eval(self.label.text() + self.big_label.text()))
                else:
                    p = (self.label.text() + ' ' + self.big_label.text()).split(' ')
                    for i in range(len(p)):
                        if p[i] not in '+-//**%':
                            p[i] = convert_base(p[i], 10, int(self.base))
                    self.number = str(eval(' '.join(p)))

                if '.' in self.number:
                    if self.number.split('.')[-1] != '0':
                        if len(str(self.number).split('.')[-1]) >= 6:
                            self.number = '{:.6f}'.format(float(self.number))
                        else:
                            st = '{:.' + str(len(self.number.split('.')[-1])) + 'f}'
                            self.number = st.format(float(self.number))
                    else:
                        self.number = self.number.split('.')[0]

                self.number = str(self.number)
                self.label.setText('')
                self.big_label.setText(self.number if int(self.base) == 10
                                       else convert_base(self.number, int(self.base)))

            except ZeroDivisionError:
                self.label.setText(self.label.text() + str(self.number))
                self.big_label.setText('ERROR')

            except SyntaxError:
                self.label.setText(self.label.text() + ' ' + str(self.number))
                self.big_label.setText('SYNTAX ERROR')

    # Функция, для кнопок с цифрами
    def click_numeral(self):
        if self.f or (self.label.text() != '' and not self.f):
            self.number += self.sender().text()
            self.big_label.setText(self.number)

    # Функция, для кнопок с операциями
    def click_operation(self):
        if self.f:
            self.f = False
        if self.big_label.text() != '':
            if self.label.text() == '':
                self.big_label.setText('')
                self.label.setText(self.number + ' ' + self.sender().text())
                self.number = ''
            else:
                self.big_label.setText('')
                self.label.setText(self.label.text() + ' ' + self.number + ' ' + self.sender().text())
                self.number = ''

    # Функция, для кнопки, очищающей всё
    def clear(self):
        self.big_label.setText('0')
        self.label.setText('')
        self.number = ''
        self.f = True

    # Функция для создания дробных чисел
    def add_point(self):
        if self.f or (self.label.text() != '' and not self.f):
            if '.' not in self.number:
                if self.number == '':
                    self.number = '0.'
                else:
                    self.number += '.'
                self.big_label.setText(self.number)

    # Функция для смены знака числа
    def sign_change(self):
        if self.label.text() == '' and (self.big_label.text() != '' and int(self.big_label.text()) != 0):
            if self.big_label.text()[0] == '-':
                self.big_label.setText(self.big_label.text()[1:])
            else:
                self.big_label.setText('-' + self.big_label.text())

    # Функция возвращения на шаг назад
    def click(self):
        if self.big_label.text() == '':
            stroka = self.label.text().split(' ')
            self.label.setText(' '.join(stroka[:-2]))
            self.big_label.setText(stroka[-2])
        else:
            self.big_label.setText('')

    # Функция смены СС
    def convertation(self):
        if self.number == '':
            self.big_label.setText('0')
        else:
            self.big_label.setText(convert_base(self.number, int(self.base), int(self.last_base)))
        self.last_base = self.base
        self.base = self.comboBox.currentText()
        self.label_base.setText(self.base)
        self.enabled()

    # Функция, которая делает кнопки с цифрами, большими или равными СС в данный момент, ненажимаемыми
    def enabled(self):
        for i in range(len(self.buttons) - 1, -1, -1):
            if i >= int(self.base):
                self.buttons[i].setEnabled(False)
            else:
                self.buttons[i].setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator_NS()
    ex.show()
    sys.exit(app.exec_())