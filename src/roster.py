from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt

class Cost:
    def __init__(self, name, typeId, value):
        self.name = name
        self.typeId = typeId
        self.value = value

class Category:
    def __init__(self, id, name, entryId, primary):
        self.id = id
        self.name = name
        self.entryId = entryId
        self.primary = primary

class Characteristic:
    def __init__(self, name, typeId, value):
        self.name = name
        self.typeId = typeId
        self.value = value

class Profile:
    def __init__(self, id, name, hidden, typeId, typeName):
        self.id = id
        self.name = name
        self.hidden = hidden
        self.typeId = typeId
        self.typeName = typeName
        self.characteristics = []

class Rule:
    def __init__(self, id, name, publicationId, page, hidden):
        self.id = id
        self.name = name
        self.publicationId = publicationId
        self.page = page
        self.hidden = hidden

class Selection:
    def __init__(self, id, name, entryId, number, type):
        self.id = id
        self.name = name
        self.entryId = entryId
        self.number = number
        self.type = type
        self.rules = []
        self.profiles = []
        self.costs = []
        self.categories = []
        self.selections = []

class Force:
    def __init__(self, id, name, entryId, catalogueId, catalogueRevision, catalogueName):
        self.id = id
        self.name = name
        self.entryId = entryId
        self.catalogueId = catalogueId
        self.catalogueRevision = catalogueRevision
        self.catalogueName = catalogueName
        self.rules = []
        self.selections = []
        self.costs = []
        self.categories = []

class Roster:
    def __init__(self, id, name, battleScribeVersion, gameSystemId, gameSystemName, gameSystemRevision):
        self.id = id
        self.name = name
        self.battleScribeVersion = battleScribeVersion
        self.gameSystemId = gameSystemId
        self.gameSystemName = gameSystemName
        self.gameSystemRevision = gameSystemRevision
        self.costs = []
        self.forces = []

class RosterItemModel(QAbstractItemModel):
    def __init__(self, roster, parent=None):
        super().__init__(parent)
        self.roster = roster

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self.roster.forces)
        if isinstance(parent.internalPointer(), Force):
            return len(parent.internalPointer().selections)
        return 0

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None

        if not index.parent().isValid():
            if(index.column() == 0):
                force = self.roster.forces[index.row()]
                return force.name
            else:
                return " "
        else:
            force = index.parent().internalPointer()
            selection = force.selections[index.row()]
            if(index.column() == 0):
                return selection.name
            elif(index.column() == 1):
                display = ""
                if selection.profiles is not None:
                    for profile in selection.profiles:
                        if profile.typeName == "Unit":
                            for characteristic in profile.characteristics:
                                display += f"{characteristic.name}: {characteristic.value}\n"
                return display

    def index(self, row, column, parent=QModelIndex()):
        if not parent.isValid():
            return self.createIndex(row, column, self.roster.forces[row])
        if isinstance(parent.internalPointer(), Force):
            force = parent.internalPointer()
            if(force.selections[row].type == "unit" or force.selections[row].type == "model"):
                return self.createIndex(row, column, force.selections[row])
            return QModelIndex()
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        if isinstance(index.internalPointer(), Force):
            return QModelIndex()
        if isinstance(index.internalPointer(), Selection) and (index.internalPointer().type == "unit" or index.internalPointer().type == "model"):
            for i, force in enumerate(self.roster.forces):
                if index.internalPointer() in force.selections:
                    return self.createIndex(i, 0, force)
        return QModelIndex()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        headers = ["Name", "Profile"]
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return headers[section]
        return None