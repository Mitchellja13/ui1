# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from UI.ui_setup import setup_video_section, setup_info_section, setup_menu_bar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("C2 Display")

        self.Width = 1500
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        video_section = setup_video_section()
        main_layout.addWidget(video_section, 3)

        info_section = setup_info_section()
        main_layout.addWidget(info_section, 1)

        setup_menu_bar(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
