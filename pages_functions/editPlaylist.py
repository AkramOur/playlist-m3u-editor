from PyQt5.QtWidgets import QWidget

from ui.pages.dashboard_ui import Ui_Form


class EditPlaylist(QWidget):
    def __init__(self):
        super(EditPlaylist, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
