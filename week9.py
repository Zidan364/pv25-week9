import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QComboBox, QLineEdit,
    QPushButton, QLabel, QSpinBox
)
from PyQt6.uic import loadUi


class InputDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("week9.ui", self)

        self.btn_list.clicked.connect(self.showListDialog)
        self.btn_name.clicked.connect(self.showNameDialog)
        self.btn_integer.clicked.connect(self.showIntegerDialog)

    def showListDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select from List")
        layout = QVBoxLayout()

        label = QLabel("List of Languages")
        combo = QComboBox()
        combo.addItems(["C", "C++", "Java", "Python"])

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: (
            self.line_list.setText(combo.currentText()),
            dialog.accept()
        ))

        layout.addWidget(label)
        layout.addWidget(combo)
        layout.addWidget(btn_ok)
        dialog.setLayout(layout)
        dialog.exec()

    def showNameDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Enter Name")
        layout = QVBoxLayout()

        label = QLabel("Enter your name:")
        line_edit = QLineEdit()

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: (
            self.line_name.setText(line_edit.text()),
            dialog.accept()
        ))

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(btn_ok)
        dialog.setLayout(layout)
        dialog.exec()

    def showIntegerDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Enter Integer")
        layout = QVBoxLayout()

        label = QLabel("Enter a number:")
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: (
            self.line_integer.setText(str(spin_box.value())),
            dialog.accept()
        ))

        layout.addWidget(label)
        layout.addWidget(spin_box)
        layout.addWidget(btn_ok)
        dialog.setLayout(layout)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.show()
    sys.exit(app.exec())
