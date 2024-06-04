from composant import Composant

class Transformateur(Composant):
    def __init__(self, coords):
        super().__init__(coords)
        self.spec_values = {
            "coords" : {
                "puissanceNominale" : (220, 812),
                "tensionPrimaire" : (211, 840),
                "tensionSecondaireAVide" : (212, 871),
                "Reseau" : (423, 871),
                "chuteDeTensionAdmissible" : (150, 953)
        }
        }

if __name__ == "__main__":  
    transfo = Transformateur("test")

    print(transfo.spec_values['test'])