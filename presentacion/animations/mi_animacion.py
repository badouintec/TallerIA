from manim import *

class MiPrimeraEscena(Scene):
    def construct(self):
        texto = Text("Les damos la bienvenida al taller de inteligencia artificial")
        self.play(Write(texto))
        self.wait(2)
        self.play(FadeOut(texto))