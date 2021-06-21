from PyQt5 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())  # Set layout style
        self.keypad()
        self.temp_nums = []  # Stores all numbers entered
        self.fin_nums = []   # Stores the current equation

        self.show()

    def keypad(self):
        """Create buttons for calculator."""
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter', clicked=self.func_result)
        btn_clear = qtw.QPushButton('Clear', clicked=self.clear_calc)
        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_add = qtw.QPushButton('+', clicked=lambda: self.num_press('+'))
        btn_subtract = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_multiply = qtw.QPushButton('x', clicked=lambda: self.func_press('*'))
        btn_divide = qtw.QPushButton('÷', clicked=lambda: self.func_press('÷'))

        # Adding buttons to the layout
        container.layout().addWidget(self.result_field, 0, 0, 1, 5)
        container.layout().addWidget(btn_result, 1, 0, 1, 3)
        container.layout().addWidget(btn_clear, 1, 3, 1, 3)

        container.layout().addWidget(btn_9, 2, 3)
        container.layout().addWidget(btn_8, 2, 2)
        container.layout().addWidget(btn_7, 2, 1)
        container.layout().addWidget(btn_add, 2, 4)

        container.layout().addWidget(btn_6, 3, 3)
        container.layout().addWidget(btn_5, 3, 2)
        container.layout().addWidget(btn_4, 3, 1)
        container.layout().addWidget(btn_subtract, 3, 4)

        container.layout().addWidget(btn_3, 4, 3)
        container.layout().addWidget(btn_2, 4, 2)
        container.layout().addWidget(btn_1, 4, 1)
        container.layout().addWidget(btn_multiply, 4, 4)

        container.layout().addWidget(btn_0, 5, 0, 1, 4)
        container.layout().addWidget(btn_divide, 5, 4)

        # Add widgets to main window (QVBoxLayout())
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


# Create application
app = qtw.QApplication([])
mw = MainWindow()
# Run Application
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec()
