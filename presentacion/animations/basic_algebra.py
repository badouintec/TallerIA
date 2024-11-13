# basic_algebra.py
from manim import *

class BasicAlgebraEnhanced(Scene):
    def construct(self):
        # Definir una paleta de colores en tonos de azul, negro, gris y blanco
        self.colors = {
            "background": "#FFFFFF",   # Blanco
            "primary": "#1E88E5",      # Azul medio
            "secondary": "#1565C0",    # Azul oscuro
            "accent": "#90CAF9",       # Azul claro
            "text": "#000000",         # Negro para texto
            "highlight": "#757575",    # Gris para resaltar
        }

        # Configuración del fondo
        self.camera.background_color = self.colors["background"]

        # Título centrado
        title = Text(
            "Conceptos Básicos de Álgebra",
            font="Arial",
            color=self.colors["primary"]
        ).scale(1.2)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=self.colors["accent"]).match_width(title).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        self.wait(1)

        # Cuadro de diálogo inicial con contexto sobre ecuaciones e igualdades
        dialog = self.create_dialog(r"Una ecuación es una igualdad entre dos expresiones matemáticas.", animate=True)
        self.wait(2)

        # Actualizar diálogo para introducir la ecuación
        self.update_dialog(dialog, r"Resolveremos la ecuación $x + 3 = 7$ para encontrar el valor de $x$.")
        self.wait(2)

        # Mostrar la ecuación principal centrada
        equation = MathTex("x + 3 = 7", color=self.colors["text"], font_size=72)
        equation.next_to(title, DOWN, buff=1)
        self.play(Write(equation))
        self.wait(2)

        # Enfatizar cada término con colores
        self.play(
            equation.animate.set_color_by_tex("x", self.colors["primary"])
                            .set_color_by_tex("3", self.colors["accent"])
                            .set_color_by_tex("7", self.colors["secondary"])
        )
        self.wait(2)

        # Actualizar diálogo
        self.update_dialog(dialog, "Representemos gráficamente cada término.")
        self.wait(2)

        # Crear y posicionar los elementos gráficos
        x_square = Square(
            side_length=1,
            color=self.colors["primary"],
            fill_color=self.colors["primary"],
            fill_opacity=0.8
        )
        x_label = MathTex("x", color=WHITE, font_size=36).move_to(x_square.get_center())
        x_group = VGroup(x_square, x_label)

        plus_sign = MathTex("+", color=self.colors["text"], font_size=48)

        three_circles = VGroup(*[
            Circle(
                radius=0.3,
                color=self.colors["accent"],
                fill_color=self.colors["accent"],
                fill_opacity=0.8
            ) for _ in range(3)
        ]).arrange(RIGHT, buff=0.3)

        equal_sign = MathTex("=", color=self.colors["text"], font_size=48)

        seven_squares = VGroup(*[
            Square(
                side_length=0.5,
                color=self.colors["secondary"],
                fill_color=self.colors["secondary"],
                fill_opacity=0.8
            ) for _ in range(7)
        ]).arrange(RIGHT, buff=0.2)

        # Agrupar y centrar los elementos
        left_side = VGroup(x_group, plus_sign, three_circles).arrange(RIGHT, buff=0.5)
        right_side = VGroup(equal_sign, seven_squares).arrange(RIGHT, buff=0.5)

        equation_group = VGroup(left_side, right_side).arrange(RIGHT, buff=1)
        equation_group.next_to(equation, DOWN, buff=1)

        # Mostrar representación gráfica con animaciones
        self.play(FadeIn(equation_group))
        self.wait(2)

        # Actualizar diálogo
        self.update_dialog(dialog, "Restamos 3 de ambos lados para despejar $x$.")
        self.wait(2)

        # Animación de resta y eliminación del signo '+'
        self.play(
            FadeOut(plus_sign, shift=UP),
            FadeOut(three_circles, shift=UP),
            FadeOut(seven_squares[-3:], shift=UP),
            run_time=2
        )
        self.wait(1)

        # Reorganizar los elementos restantes
        remaining_squares = VGroup(*seven_squares[:4]).arrange(RIGHT, buff=0.2)
        right_side = VGroup(equal_sign, remaining_squares).arrange(RIGHT, buff=0.5)

        # Actualizar el lado izquierdo para mostrar solo 'x'
        left_side = x_group  # sin el '+'

        equation_group = VGroup(left_side, right_side).arrange(RIGHT, buff=1)
        equation_group.next_to(equation, DOWN, buff=1)

        # Actualizar la escena
        self.play(
            left_side.animate.move_to(equation_group.get_left()),
            run_time=1
        )
        self.wait(1)

        # Mostrar nueva ecuación simplificada
        equation2 = MathTex("x = 4", color=self.colors["text"], font_size=72)
        equation2.move_to(equation.get_center())
        self.play(Transform(equation, equation2))
        self.wait(2)

        # Actualizar diálogo
        self.update_dialog(dialog, "¡Hemos encontrado que $x = 4$!")
        self.wait(2)

        # Destacar la solución
        self.play(Indicate(equation, color=self.colors["highlight"], scale_factor=1.2))
        self.wait(2)

        # Desvanecer elementos
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(underline, shift=UP),
            FadeOut(dialog),
            FadeOut(equation),
            FadeOut(equation_group),
            run_time=3
        )
        self.wait(1)

    def create_dialog(self, message, animate=False):
        # Cuadro de diálogo centrado en la parte inferior
        bubble_base = RoundedRectangle(
            corner_radius=0.2,
            width=12,  # Ancho del cuadro de diálogo
            height=2,  # Altura del cuadro de diálogo
            color=self.colors["accent"],
            fill_color=self.colors["accent"],
            fill_opacity=0.1
        )

        # Definir la cola del cuadro de diálogo
        tail = Polygon(
            bubble_base.get_bottom() + DOWN * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + LEFT * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + RIGHT * 0.5,
            color=self.colors["accent"],
            fill_color=self.colors["accent"],
            fill_opacity=0.1
        )

        bubble = VGroup(bubble_base, tail)
        bubble.to_edge(DOWN, buff=0.1)  # Posicionar en la parte inferior

        # Texto centrado en el cuadro de diálogo
        dialog_text = Tex(
            message,
            font_size=30,
            color=self.colors["text"],
            # font="Arial",  # Eliminamos este argumento
        ).move_to(bubble_base.get_center())

        if animate:
            self.play(FadeIn(bubble), Write(dialog_text))
        else:
            self.add(bubble, dialog_text)
        return VGroup(bubble, dialog_text)

    def update_dialog(self, dialog, new_message):
        dialog_text = dialog[1]
        new_dialog_text = Tex(
            new_message,
            font_size=30,
            color=self.colors["text"],
            # font="Arial",  # Eliminamos este argumento
        ).move_to(dialog_text.get_center())
        self.play(Transform(dialog_text, new_dialog_text))