import sqlite3
from flask import current_app
from app.models.Produit import Produit
from app.models.ProduitDAOInterface import ProduitDAOInterface

class ProduitSqliteDAO(ProduitDAOInterface):

    def __init__(self):
        self.databasename = current_app.root_path + "/database.db"

    def _getDbConnection(self):
        connection = sqlite3.connect(self.databasename)
        connection.row_factory = sqlite3.Row
        return connection

    def addProduit(self, nom, prix, description, categorie, statut, photo=None):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO produit(nom, prix, description, categorie, statut, photo) VALUES (?,?,?,?,?,?)",
                (nom, prix, description, categorie, statut, photo)
            )
            connection.commit()
        finally:
            connection.close()

    def deleteProduit(self, id):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM produit WHERE id = :id", {"id": id})
            connection.commit()
        finally:
            connection.close()

    def updateProduit(self, id, nom, prix, description, categorie, statut, photo=None):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        try:
            if photo:
                query = "UPDATE produit SET nom=?, prix=?, description=?, categorie=?, statut=?, photo=? WHERE id=?"
                cursor.execute(query, (nom, prix, description, categorie, statut, photo, id))
            else:
                query = "UPDATE produit SET nom=?, prix=?, description=?, categorie=?, statut=? WHERE id=?"
                cursor.execute(query, (nom, prix, description, categorie, statut, id))
            connection.commit()
        finally:
            connection.close()

    def findAll(self):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM produit")
        rows = cursor.fetchall()
        connection.close()
        return [Produit(dict(row)) for row in rows]

    def findByName(self, nom):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM produit WHERE nom LIKE ?", (f"%{nom}%",)).fetchall()
        connection.close()
        return [Produit(dict(row)) for row in rows]

    def findByPrice(self, prix):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM produit WHERE prix <= ? ORDER BY prix ASC", (prix,)).fetchall()
        connection.close()
        return [Produit(dict(row)) for row in rows]

    def findByCategory(self, categorie):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM produit WHERE categorie = ? ORDER BY prix ASC", (categorie,)).fetchall()
        connection.close()
        return [Produit(dict(row)) for row in rows]

    def findByStatus(self, statut):
        connection = self._getDbConnection()
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM produit WHERE statut = ? ORDER BY prix ASC", (statut,)).fetchall()
        connection.close()
        return [Produit(dict(row)) for row in rows]