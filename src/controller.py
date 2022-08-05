# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" HashChecker - Controller. """

import sys
import os
from PyQt5.QtWidgets import QApplication
from view import Window
from model import Model

__version__ = "0.1"
__author__ = "klaus-moser"


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals_slots()

    def connect_signals_slots(self) -> None:
        pass
        self.view.push_button_go.clicked.connect(self.view.about)
        self.view.push_button_h1.clicked.connect(self.view.about)
        self.view.push_button_h2.clicked.connect(self.view.about)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)  # Create an instance of 'QApplication'
    win = Window()
    win.show()  # Show the calculator's GUI
    c = Controller(Model(win), win)  # Create the controller incl. Model & GUI
    sys.exit(app.exec())  # Execute main loop