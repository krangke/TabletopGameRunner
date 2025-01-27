from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
from roster import Cost, Category, Profile, Rule, Selection, Force, RosterItemModel
from ImportRoster import parse_roster

class MainWindow(QMainWindow):
    def __init__(self, roster):
        super().__init__()
        self.setWindowTitle("Army List")
        self.setGeometry(100, 100, 600, 400)

        self.tree_view = QTreeView()
        self.model = RosterItemModel(roster)
        self.tree_view.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Example usage
    roster = parse_roster('Dan\'s Space Marines(10th).ros')
    window = MainWindow(roster)
    window.show()
    sys.exit(app.exec())