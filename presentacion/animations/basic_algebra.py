from manim import *

class BasicAlgebra(Scene):
    def construct(self):
        # Configuración del fondo blanco
        self.camera.background_color = "#FFFFFF"

        # Título de la escena con tipografía más clara
        title = Text("Conceptos Básicos de Álgebra", font="Arial", color="#000000").scale(0.9)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))
        self.wait(1)

        # Cuadro de diálogo explicativo con fuente más agradable
        dialog_box = RoundedRectangle(corner_radius=0.1, height=1, width=10, color="#4682B4").to_edge(DOWN)
        dialog_text = Text("Comenzamos con la ecuación x + 3 = 7", font="Arial", color="#000000").scale(0.55)
        dialog_text.move_to(dialog_box.get_center())
        self.play(FadeIn(dialog_box), Write(dialog_text))
        self.wait(2)

        # Mostrar la ecuación principal centrada
        equation = MathTex("x + 3 = 7", color="#4682B4").scale(1.5)
        equation.move_to(UP * 1)
        self.play(Write(equation))
        self.wait(2)

        # Actualizar cuadro de diálogo para explicar el siguiente paso
        self.update_dialog(dialog_text, "Representamos visualmente 'x' y '3'.")
        self.wait(2)

        # Elementos visuales: 'x' como cuadrado y '3' como círculos
        x_square = Square(side_length=1, color="#4682B4", fill_opacity=0.3).move_to(LEFT * 2)
        x_label = MathTex("x", color="#4682B4").move_to(x_square)
        three_circles = VGroup(
            *[Circle(radius=0.2, color="#000000", fill_opacity=0.3).next_to(x_square, RIGHT, buff=0.3 * i) for i in range(1, 4)]
        )
        self.play(FadeIn(x_square), Write(x_label), FadeIn(three_circles))
        self.wait(2)

        # Mostrar el resultado a la derecha
        total_box = Rectangle(width=1.5, height=1, color="#4682B4", fill_opacity=0.3).move_to(RIGHT * 2)
        total_label = MathTex("7", color="#4682B4").move_to(total_box)
        self.play(FadeIn(total_box), Write(total_label))
        self.wait(2)

        # Actualizar cuadro de diálogo para explicar la resta
        self.update_dialog(dialog_text, "Restamos 3 de ambos lados.")
        self.wait(2)

        # Desaparecer los círculos de '3' y otros elementos visuales con animación suave
        self.play(three_circles.animate.shift(UP * 1).set_opacity(0), run_time=1.5)
        self.wait(1)

        # Quitar elementos visuales para dar espacio
        self.play(FadeOut(x_square, shift=LEFT), FadeOut(x_label, shift=LEFT), FadeOut(total_box, shift=RIGHT), FadeOut(total_label, shift=RIGHT))
        self.wait(1)

        # Mostrar el paso intermedio 'x = 7 - 3'
        step1 = MathTex("x = 7 - 3", color="#000000").scale(1.3)
        step1.move_to(UP * 1)
        self.play(Transform(equation, step1))
        self.wait(2)

        # Actualización del cuadro de diálogo para simplificar
        self.update_dialog(dialog_text, "Simplificamos la ecuación.")
        self.wait(2)

        # Transformar al resultado final 'x = 4'
        step2 = MathTex("x = 4", color="#4682B4").scale(1.3)
        step2.move_to(UP * 1)
        self.play(Transform(step1, step2))
        self.wait(2)

        # Desaparecer la ecuación anterior para limpiar la pantalla
        self.play(FadeOut(equation))
        self.wait(1)

        # Mostrar el resultado final centrado
        final_answer = Text("Solución: x = 4", font="Arial", color="#4682B4").scale(1.1)
        final_answer.move_to(DOWN * 1)
        self.play(Write(final_answer))
        self.wait(2)

        # Mensaje final en el cuadro de diálogo
        self.update_dialog(dialog_text, "¡Hemos resuelto la ecuación correctamente!")
        self.wait(2)

    def update_dialog(self, dialog_text, new_message):
        new_dialog = Text(new_message, font="Arial", color="#000000").scale(0.55)
        new_dialog.move_to(dialog_text.get_center())
        self.play(Transform(dialog_text, new_dialog))