from manim import *

class BasicAlgebra(Scene):
    def construct(self):
        # Título de la escena
        title = Text("Conceptos Básicos de Álgebra").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # Mostrar una ecuación simple
        equation = MathTex("x + 3 = 7")
        equation.set_color(BLUE)
        self.play(Write(equation))
        self.wait(2)

        # Resolver la ecuación paso a paso
        step1 = MathTex("x = 7 - 3")
        step1.next_to(equation, DOWN, buff=0.5)
        self.play(Transform(equation, step1))
        self.wait(2)

        step2 = MathTex("x = 4")
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Transform(step1, step2))
        self.wait(2)

        # Mostrar la respuesta final
        final_answer = Text("Solución: x = 4", color=GREEN).scale(0.8)
        final_answer.next_to(step2, DOWN, buff=0.5)
        self.play(Write(final_answer))
        self.wait(2)

        # Despedida
        thank_you = Text("¡Gracias por aprender álgebra!", color=YELLOW).scale(0.7)
        thank_you.to_edge(DOWN)
        self.play(FadeIn(thank_you))
        self.wait(2)