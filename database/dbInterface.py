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


class OutgoingInterface(object):
    """
    This interface will be used for retrieving from the database
    """
    # TODO these gets can be abstracted quite a bit
    def __init__(self, dbFilename, dbDriver=sqlite3):
        self.dbFilename = dbFilename
        self.dbDriver = dbDriver

    def openConnection(self):
        conn = self.dbDriver.connect(self.dbFilename)
        conn.row_factory = dict_factory
        return conn

    @staticmethod
    def closeConnection(self, conn):
        conn.commit()
        conn.close()


class IncomingInterface(OutgoingInterface):
    """
    This interface will be used for adding to the database
    """
    def __init__(self, dbFilename, dbDriver=sqlite3):
        super(IncomingInterface, self).__init__(dbFilename, dbDriver)
        self.dbDriver = dbDriver
        self.dbFilename = dbFilename

