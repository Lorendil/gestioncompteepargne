# Définition d'une classe CompteBancaire(), qui permette d'instancier des objets tels que compte1, compte2, etc. Le constructeur de cette classe initialisera deux attributs d'instance nom et solde, 
# Trois méthodes sont définies :
#     depot(somme)permettra d'ajouter une certaine somme au solde ;
#     retrait(somme)permettra de retirer une certaine somme du solde ;
#     affiche()permettra d'afficher le nom du titulaire et le solde de son compte.

class CompteBancaire(object):
    """Classe permettant d'instancier des objets pour jouer sur la solde"""
    def __init__(self,nom = "Dupont",c = 1000):
        """Initialisation"""
        self.nom = nom
        self.compte = c
  
    def depot(self,vd = 0):
        """Methode permettant de déposer une somme sur un compte"""
        self.compte = self.compte + vd

    def retrait(self,vr = 0):
        """Methode permettant de retirer une somme sur un compte"""
        self.compte = self.compte - vr
        
    def affiche(self):
        """Methode permettant d'afficher la somme d'un compte"""
        return print("Le solde du compte bancaire de {} est de {} euros".format(self.nom,self.compte))

if __name__ == "__main__":
    compte1 = CompteBancaire("Duchmol", 800)
    compte2 = CompteBancaire()

    compte1.depot(350)
    compte1.retrait(200)

    compte1.affiche()

    compte2.depot(25)

    compte2.affiche()