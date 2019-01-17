from PySide2 import QtWidgets
from ui import main, charCreate, test


class Test(test.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)

    def open_file(self):
        file_path = str(QtWidgets.QFileDialog.getOpenFileName
                        (self,
                         "Open Character",
                         "",
                         "Text Files (*.txt)")[0]
                        )

        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.label_1.setText(lines[0])
                    self.label_2.setText(lines[1])
                    self.label_3.setText(lines[2])
                    self.label_4.setText(lines[3])
                    self.label_5.setText(lines[4])
                    self.label_6.setText(lines[5])
                    self.label_7.setText(lines[6])
                    self.label_8.setText(lines[7])
                    self.label_9.setText(lines[8])
                    inv = open(lines[9], "r")
                inv_dat = inv.readlines()
                for line in inv_dat:
                    self.label_11.setText(inv_dat[0])
                    self.label_12.setText(inv_dat[1])
                    self.label_14.setText(inv_dat[2])
                    self.label_16.setText(inv_dat[3])
            file.close()
        self.show()


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
                     self.spinBox_6.text() + '\n',
                     "chars/" + self.lineEdit.text() + "_inv.txt"]
            file.writelines(lines)
            file.close()

        auto_open = open("chars/" + self.lineEdit.text() + ".txt", "r")
        auto_read = auto_open.readlines()
        for line in auto_read:
            auto_edit = open(auto_read[9], "w+")
            lines = ["30" + '\n',
                     "75" + '\n',
                     "83" + '\n',
                     "98"]
        auto_edit.writelines(lines)
        auto_edit.close()
        auto_open.close()
        self.lineEdit.setText("")
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(0)
        self.spinBox_6.setValue(0)
        self.close()


class SheetsQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(SheetsQtApp, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.launch_char_creation)
        self.pushButton.clicked.connect(self.open_file)

        self.popChar_Create = CharCreate()
        self.popSheet = Test()

    def launch_char_creation(self):
        self.popChar_Create.show()

    def open_file(self):
        self.popSheet.open_file()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = SheetsQtApp()
    qt_app.show()
    app.exec_()
