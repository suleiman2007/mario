import pyxel


class Perso:
    
    def __init__(self):
        self.position = [0, 120]
        self.mouv = [0,0]

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.mouv[0] = 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.mouv[0] = -2

        self.position[0] += self.mouv[0]

        self.mouv = [0,0]

class Jeu:
    def __init__(self):
        pyxel.init(256, 128, 'mario')
        self.perso = Perso()
        pyxel.load("images.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.perso.deplacement()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.perso.position[0], self.perso.position[1], 0, 0, 0, 8, 8)

Jeu()