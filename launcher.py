from PySide2 import QtWidgets
from ui import main, charCreate


class CharCreate(charCreate.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(CharCreate, self).__init__()
        self.setupUi(self)
        self.button_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.button_ok.clicked.connect(self.create_file)

    def create_file(self):
        if self.lineEdit.text() != "":
            file = open("chars/" + self.lineEdit.text() + ".txt", "w+")
            lines = [self.lineEdit.text() + '\n',
                     self.comboBox.currentText() + '\n',
                     self.comboBox_2.currentText() + '\n',
                     self.spinBox.text() + '\n',
                     self.spinBox_2.text() + '\n',
                     self.spinBox_3.text() + '\n',
                     self.spinBox_4.text() + '\n',
                     self.spinBox_5.text() + '\n',
                     self.spinBox_6.text()]
            file.writelines(lines)
            file.close()
        self.close()


class SheetsQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(SheetsQtApp, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.launch_char_creation)
        self.pushButton.clicked.connect(self.open_file)

        self.popChar_Create = CharCreate()

    def launch_char_creation(self):
        self.popChar_Create.show()

    def open_file(self):
        file_path = str(QtWidgets.QFileDialog.getOpenFileName(self, "Open Character", "", "Text Files (*.txt)")[0])

        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.split(",")
                    print(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = SheetsQtApp()
    qt_app.show()
    app.exec_()
