from PyQt5.QtWidgets import QMainWindow, QMessageBox

from view_orig import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

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
