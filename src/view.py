from PyQt5.QtWidgets import QMainWindow, QMessageBox

from view_orig import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.radioButton_sha256.setChecked(True)

    def about(self) -> None:
        """
        Show a pop-up message with the about text.
        """
        QMessageBox.about(
            self,
            "About HashChecker",
            "<font style='font-family: Terminal'>"
            "<p>An simple app to compare two hash codes/codefiles:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python3</p>",
        )

    def print_text(self, text: str) -> None:
        self.textEdit_output.setPlainText(text)

    def clear_text(self) -> None:
        self.textEdit_output.clear()

    def get_text(self) -> list:
        return [self.lineEdit_h1.text(), self.lineEdit_h2.text()]
