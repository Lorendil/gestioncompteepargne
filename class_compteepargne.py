from class_comptebancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    """Permet de calculer l'épargne d'un compte"""

    def __init__(self, nom = "Nom", compte = 0):
        """Initialisation de la classe"""
        CompteBancaire.__init__(self,nom, compte)
        self.taux = 0.3
    
    def changeTaux(self,modiftaux):
        """Methode permettant de modifier le taux d'intérêt, le taux s'écrit '5.5' pour un taux de 5,5% par exemple"""
        self.taux = modiftaux
    
    def capitalisation(self, mois = 1):
        """Methode permettant d'afficher le nombre de mois et le taux d'intérêt prix en compte """
        self.compte = self.compte + (self.compte *self.taux/100)*mois
        print("Capitalisation du compte bancaire de {} sur {} mois au taux mensuel de {} %".format(self.nom,mois,self.taux))


if __name__ == "__main__":
    c1 = CompteEpargne("Duvivier", 600)
    c1.depot(350)
    c1.affiche()
    c1.capitalisation(12)
    c1.affiche()
    c1.changeTaux(0.5)
    c1.capitalisation(12)
    c1.affiche()