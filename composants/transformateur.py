from composant import Composant

class Transformateur(Composant):
    def __init__(self, coords):
        super().__init__(coords)
        self.spec_values = { 
            "puissanceNominale" : (220, 812),
            "tensionPrimaire" : (211, 840),
            "tensionSecondaireAVide" : (212, 871),
            "raccordementPrimaire": (303, 908),
            "raccordementPrimaire_choix": {
                "monophase": (240, 928),
                "biphase": (240, 947),
                "triphase": (240, 967)
            },
            "reseau" : (423, 871),
            "chuteDeTensionAdmissible" : (150, 953),
            "SaisieAvancee" : (486, 1038),  
        }

if __name__ == "__main__":  
    transfo = Transformateur("test")

    print(transfo.spec_values['test'])