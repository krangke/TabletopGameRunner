from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
from roster import Cost, Category, Profile, Rule, Selection
from ImportRoster import parse_roster

class MainWindow(QMainWindow):
    def __init__(self, roster):
        super().__init__()
        self.setWindowTitle("Roster Classes")
        self.setGeometry(100, 100, 600, 400)

        self.tree_view = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Classes", "Attributes"])
        self.tree_view.setModel(self.model)

        self.populate_tree()

        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_tree(self):
        classes = {
            "Cost": ["name", "typeId", "value"],
            "Category": ["id", "name", "entryId", "primary"],
            "Profile": ["id", "name", "hidden", "typeId", "typeName"],
            "Rule": ["id", "name", "publicationId", "page", "hidden"],
            "Selection": ["id", "name", "entryId", "number", "type"],
            "Force": ["id", "name", "entryId", "catalogueId", "catalogueRevision", "catalogueName"]
        }

        for force in roster.forces:
            force_item = QStandardItem(str(getattr(force, "name", '')))
            
            for selection in force.selections:
                if selection.type == "model" or selection.type == "unit":
                    selection_item = QStandardItem(str(getattr(selection, "name", '')))
                    force_item.appendRow(selection_item)
            self.model.appendRow(force_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Example usage
    roster = parse_roster('Dan\'s Space Marines(10th).ros')
    window = MainWindow(roster)
    window.show()
    sys.exit(app.exec())