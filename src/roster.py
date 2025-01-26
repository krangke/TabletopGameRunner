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

class Profile:
    def __init__(self, id, name, hidden, typeId, typeName):
        self.id = id
        self.name = name
        self.hidden = hidden
        self.typeId = typeId
        self.typeName = typeName

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
