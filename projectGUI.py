# Проект - Мениджър на Задачи с графичен интерфейс. Използва библиотеки PyQt5, sys. Запазва въведената информация до изход от програмата.

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QListWidget, QPushButton, QDialog
from PyQt5.QtWidgets import QListWidgetItem, QLineEdit, QMessageBox
from PyQt5 import QtWidgets, QtCore
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(370, 500)
        self.setWindowTitle("Мениджър на Задачи")
        self.label = QtWidgets.QLabel(self)
        self.button1 = QtWidgets.QPushButton(self)
        self.button2 = QtWidgets.QPushButton(self) 
        self.button3 = QtWidgets.QPushButton(self) 
        self.button4 = QtWidgets.QPushButton(self) 
        self.button5 = QtWidgets.QPushButton(self) 
        self.setMaximumSize(QtCore.QSize(370, 500))
        self.setMinimumSize(QtCore.QSize(370, 500))

        self.input = QLineEdit()
        self.text_line = QLineEdit()
        layout = QVBoxLayout()
        self.text_list = QListWidget()
        
        layout.addWidget(self.input)
        self.button1.setText("Добави")
        self.button1.setFixedSize(70, 30)
        self.button1.move(10, 10)
        self.button1.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.button1.clicked.connect(self.add_item)
        layout.addWidget(self.button1)


        self.button2.setText("Изход")
        self.button2.setFixedSize(70, 30)
        self.button2.move(290, 10)
        self.button2.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.button2.clicked.connect(exit)

        self.button3.setText("Изтрий")
        self.button3.setFixedSize(70, 30)
        self.button3.move(150, 10)
        self.button3.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.button3.clicked.connect(self.delete_item)
        
        self.button4.setText("Промени")
        self.button4.setFixedSize(70, 30)
        self.button4.move(80, 10)
        self.button4.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.button4.clicked.connect(self.change)

        self.button5.setText("Размени")
        self.button5.setFixedSize(70, 30)
        self.button5.move(220, 10)
        self.button5.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.button5.clicked.connect(self.exchange)

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.ExtendedSelection)
        self.list_widget.setGeometry(10, 50, 350, 440)
        
        layout.addWidget(self.text_line)
        layout.addWidget(self.text_list)
    
    def exchange(self):
        if self.list_widget.count() != 0:
            selected = self.list_widget.selectedItems()
            if (len(selected) == 2):
                val1 = selected[0].text().split(". ", 1)[1]
                val1num = selected[0].text().split(". ", 1)[0]
                val2 = selected[1].text().split(". ", 1)[1]
                val2num = selected[1].text().split(". ", 1)[0]
                selected[0].setText(f"{val1num}. {val2}")
                selected[1].setText(f"{val2num}. {val1}")
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Внимание")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Трябва да маркирате ДВА реда за размяна!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        else:
            emptymsg()

    def change(self):
        if self.list_widget.count() != 0:
            selected = self.list_widget.selectedItems()
            if (len(selected) == 1):
                selected = selected[0]
                dialog = Change(self, selected.text().split(". ", 1)[1])
                if dialog.exec_():
                    num = selected.text().split(". ", 1)[0]
                    item_text = dialog.get_item_text()
                    selected.setText(f"{num}. {item_text}")
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Внимание")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Трябва да маркирате ЕДИН ред за редактиране!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        else:
            emptymsg()  

    def delete_item(self, item):
        if self.list_widget.count() != 0:
            selected_items = self.list_widget.selectedItems()
            if (len(selected_items) > 0):
                for item in selected_items:
                    row = self.list_widget.row(item)
                    self.list_widget.removeItemWidget(item)
                    self.list_widget.takeItem(row)
            
                n = 1
                for x in range(self.list_widget.count()):
                    item = self.list_widget.item(x)
                    item.setText(f"{n}. {item.text().split(". ", 1)[1]}")
                    n += 1
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Внимание")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Не сте маркирали ред!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
        else:
            emptymsg()

    def add_item(self):
        dialog = AddItemDialog(self)
        if dialog.exec_():
            item_text = dialog.get_item_text()
            self.list_widget.addItem(QListWidgetItem(f"{self.list_widget.count() + 1}. {item_text}"))

class Change(QDialog):
    def __init__(self, parent, label):
        super().__init__(parent)
        self.item_text = None
        self.setWindowFlag(QtCore.Qt.WindowType.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Промяна на задачи")
        self.setFixedSize(300, 100)
        
        layout = QVBoxLayout()
        self.text_input = QLineEdit(self)
        self.text_input.setText(label)
        self.text_input.selectAll()
        layout.addWidget(self.text_input)

        change_button = QPushButton("Промени", self)
        change_button.clicked.connect(self.accept)
        layout.addWidget(change_button)

        cancel_button = QPushButton("Затвори", self)
        cancel_button.clicked.connect(self.close_window)
        layout.addWidget(cancel_button)
        self.setLayout(layout)

    def close_window(self):
        self.close()

    def get_item_text(self):
        return self.item_text

    def accept(self):
        self.item_text = self.text_input.text().strip(" ")
        if self.item_text == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Внимание")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Трябва да въведете текст!")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            self.item_text = f"{self.item_text}"
            super().accept()

class AddItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.item_text = None
        self.setWindowFlag(QtCore.Qt.WindowType.WindowContextHelpButtonHint, False)
        self.setWindowTitle("Добавяне на задачи")
        self.setFixedSize(300, 100)
        layout = QVBoxLayout()
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        add_button = QPushButton("Добави", self)
        add_button.clicked.connect(self.accept)
        layout.addWidget(add_button)

        cancel_button = QPushButton("Затвори", self)
        cancel_button.clicked.connect(self.close_window)
        layout.addWidget(cancel_button)
        self.setLayout(layout)

    def close_window(self):
        self.close()

    def get_item_text(self):
        return self.item_text

    def accept(self):
        self.item_text = self.text_input.text().strip(" ")
        if self.item_text == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Внимание")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Моля въведете текст!")
            msg_box.setStandardButtons(QMessageBox.OK)
            msg_box.exec_()
        else:
            super().accept()

def emptymsg():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Внимание")
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText("Листът е празен!")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

def window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

window()