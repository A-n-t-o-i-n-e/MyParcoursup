class Voeux:
    def __init__(self, formation : dict):
        self.formation = formation

class SousVoeux:
    def __init__(self, voeux : Voeux, formation : dict):
        self.voeux = voeux
        self.formation = formation
