from app.models.ProduitDAO import ProduitSqliteDAO as ProduitDAO
from app.models.ProduitDAO import ProduitDAOInterface

class ProduitService:

    def __init__(self):
        self.pdao = ProduitDAO()

    def getAll(self):
        
        res = self.pdao.findAll()

        return res 
    
    def getByName(self, nom):

        res = self.pdao.findByName(nom)

        if type(res) is not list:
            res = [res]
        return res
    
    def getByPrice(self, prix):

        res = self.pdao.findByPrice(prix)

        if len(res) > 0:
            return res
        
        return [{}]
    
    def findByStatus(self, statut):

        res = self.pdao.findByStatus(statut)

        if len(res) > 0:
            return  res
        return [{}]
    
    def getByCategory(self, categorie):

        res = self.pdao.findByCategory(categorie)

        if type(res) is not list:
            res = [res]
        return res
    
    def addProduit(self, nom, prix,description, categorie, statut,photo=None):

        res = self.pdao.addProduit(nom,prix,description,categorie,statut,photo)
        return res 
    
    def deleteProduit(self, id):
        return self.pdao.deleteProduit(id)
    
    def updateproduit(self, nom,prix,description,categorie,statut,photo=None):
        return self.pdao.updateProduit(nom, prix,description,categorie,statut,photo)

