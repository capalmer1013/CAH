"""
These are the interfaces that will be used
in order to interact with the database
"""
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class dbQuery(object):
    def __init__(self, tableName='', dictOfIds={}):
        self.tableName=tableName
        self.dictOfIds=dictOfIds

    def generateQuery(self):
        baseQuery = "SELECT * from "+self.tableName+"WHERE "

        for each in self.dictOfIds:
            baseQuery += each+" = "+str(self.dictOfIds[each])+" AND "

        return baseQuery[:-4] + ";"


class OutgoingInterface(object):
    """
    This interface will be used for retrieving from the database
    """
    def __init__(self, dbFilename, dbDriver=sqlite3):
        self.dbFilename = dbFilename
        self.dbDriver = dbDriver

    def openConnection(self):
        conn = self.dbDriver.connect(self.dbFilename)
        conn.row_factory = dict_factory
        return conn

    @staticmethod
    def closeConnection(conn):
        conn.commit()
        conn.close()

    def getEntryById(self, query):
        c = self.openConnection()
        result = c.cursor().execute(dbQuery(query).generateQuery())
        self.closeConnection(c)
        return result

    def getAllEntries(self, tableName):
        c = self.openConnection()
        result = c.cursor().execute("SELECT * FROM "+tableName)
        self.closeConnection(c)
        return result

    def getAllBlackCards(self):
        pass

    def getBlackCardById(self, cardID):
        pass

    def getAllWhiteCards(self):
        pass

    def getWhiteCardByID(self, cardID):
        pass

    def getAllUsers(self):
        pass

    def getUserById(self, userID):
        pass

    def getUserByName(self, userName):
        pass

    def getHandByPlayerID(self, playerID):
        pass

    def getWhiteDeckByRoomID(self, roomID):
        pass

    def getBlackDeckByRoomID(self, roomID):
        pass

    def getAllRooms(self):
        pass

    def getPlayersByRoom(self, roomID):
        pass

class IncomingInterface(OutgoingInterface):
    """
    This interface will be used for adding to the database
    """
    def __init__(self, dbFilename, dbDriver=sqlite3):
        super(IncomingInterface, self).__init__(dbFilename, dbDriver)
        self.dbDriver = dbDriver
        self.dbFilename = dbFilename

    def addSingleEntry(self, entry):
        pass

    def addManyEntries(self, listOfEntries):
        pass

    def addWhiteCard(self, card):
        pass

    def addWhiteCards(self, listOfCards):
        pass

    def addBlackCard(self, card):
        pass

    def addBlackCards(self, listOfCards):
        pass