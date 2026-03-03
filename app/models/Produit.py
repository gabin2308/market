class Produit :

    def __init__(self, dico):
        self.id = dico["id"]
        #self.user_id = dico["user_id"]
        self.nom = dico["nom"]
        self.prix = dico["prix"]
        self.categorie = dico["categorie"]
        self.description = dico["description"]
        self.statut = dico["statut"]
        self.photo = dico.get("photo")