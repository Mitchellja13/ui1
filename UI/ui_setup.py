# ui_setup.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QTreeWidget, QTreeWidgetItem, \
      QLineEdit, QTabWidget, QMenuBar, QAction, QStyledItemDelegate, QLabel, \
      QPushButton
from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtGui import QColor, QIcon

from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import QFileSystemWatcher

import json

# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

def setup_video_section():
    left_section = QWidget()
    left_section.setStyleSheet("background-color: white;")
    left_layout = QVBoxLayout(left_section)
    left_layout.setSpacing(0)
    left_layout.setContentsMargins(0, 0, 0, 0)

    # Create a QTabWidget
    tabs = QTabWidget()

    # Create Video View tab
    video_view_tab = QWidget()
    video_view_layout = QVBoxLayout()
    video_view_layout.addWidget(QLabel("Video View Content"))
    video_view_tab.setLayout(video_view_layout)

    # Create Map View tab
    map_view_tab = QWidget()
    map_view_layout = QVBoxLayout()
    map_view_layout.addWidget(QLabel("Map View Content"))
    map_view_tab.setLayout(map_view_layout)

    # Add tabs to QTabWidget
    tabs.addTab(video_view_tab, "Video View")
    # tabs.addTab(map_view_tab, "Map View")

    # Add the QTabWidget to the left layout
    left_layout.addWidget(tabs)

    return left_section

def setup_info_section():
    right_splitter = QSplitter()
    right_splitter.setOrientation(Qt.Vertical)

    top_container = QWidget()
    top_layout = QVBoxLayout(top_container)
    
    top_layout.setSpacing(0)
    top_layout.setContentsMargins(0, 0, 0, 0)
    right_splitter.addWidget(top_container)

    search_bar = QLineEdit()
    search_bar.setPlaceholderText("Search...")

    # Reminder: Margin order is top, right, bottom, left
    search_bar.setStyleSheet("""
        QLineEdit {
            border-radius: 4px;
            padding: 5px;
            margin: 5px 10px 5px 10px;
            background-color: #333333;
            color: white;
        }
    """)
    
    top_layout.addWidget(search_bar)

    top_element = QTreeWidget()
    top_element.setHeaderHidden(True)


    top_layout.addWidget(top_element)

    root = QTreeWidgetItem(top_element, ["Blue"])
    child1 = QTreeWidgetItem(root, ["ScanEagle"])
    child2 = QTreeWidgetItem(root, ["ScanEagle(2)"])
    subchild1 = QTreeWidgetItem(child1, ["Subchild 1"])
    subchild2 = QTreeWidgetItem(child1, ["Subchild 2"])

    bottom_element = QTabWidget()
    bottom_element.setContentsMargins(0, 0, 0, 0)
    # bottom_element.setStyleSheet("background-color: lightcoral;")
    bottom_element.setTabPosition(QTabWidget.West)
    right_splitter.addWidget(bottom_element)

    right_splitter.setSizes([150, 450])

    tab1 = QWidget()
    tab2 = QWidget()
    bottom_element.addTab(tab1, "") # Unit Info
    bottom_element.addTab(tab2, "") # Weapon Info

    # Set Icons for Tabs
    bottom_element.setTabIcon(0, QIcon("UI/icons/info.png"))
    bottom_element.setTabIcon(1, QIcon("UI/icons/ammunition.png"))

    bottom_element.setIconSize(QSize(20, 20))


    # Create the first tab content
    tab1_layout = QVBoxLayout()
    tab1_label = QLabel("Unit Information")
    tab1_layout.addWidget(tab1_label)
    tab1_layout.addStretch()  # Add stretch to push other widgets down
    tab1_button = QPushButton("Update Unit Info")
    tab1_layout.addWidget(tab1_button)
    tab1.setLayout(tab1_layout)

    # Create the second tab content
    tab2_layout = QVBoxLayout()
    tab2_label = QLabel("Weapon Information")
    tab2_layout.addWidget(tab2_label)
    tab2_layout.addStretch()  # Add stretch to push other widgets down
    tab2_button = QPushButton("Update Weapon Info")
    tab2_layout.addWidget(tab2_button)
    tab2.setLayout(tab2_layout)


    return right_splitter

# def setup_ammo_tab(bottom_element):
    

def setup_menu_bar(main_window):
    menu_bar = QMenuBar(main_window)
    main_window.setMenuBar(menu_bar)

    file_menu = menu_bar.addMenu("File")
    file_action = QAction("File Action", main_window)
    file_menu.addAction(file_action)

    about_menu = menu_bar.addMenu("About")
    about_action = QAction("About Action", main_window)
    about_menu.addAction(about_action)


def load_json_data(tree_widget, file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    tree_widget.clear()
    add_items(tree_widget, data)

def add_items(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            item = QTreeWidgetItem([key])
            parent.addTopLevelItem(item)
            add_items(item, value)
    elif isinstance(data, list):
        for value in data:
            item = QTreeWidgetItem([str(value)])
            parent.addTopLevelItem(item)
    else:
        item = QTreeWidgetItem([str(data)])
        parent.addTopLevelItem(item)


