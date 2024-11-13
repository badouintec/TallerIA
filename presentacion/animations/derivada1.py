from manim import *

class derivada1(Scene):
    def construct(self):
        # Configuración de la cámara para resolución 1080p
        self.camera.frame_width = 16  # Relación de aspecto 16:9
        self.camera.frame_height = 9

        # Configuración de colores
        self.colors = {
            "background": "#FFFFFF",   # Blanco
            "primary": "#1E88E5",      # Azul medio
            "secondary": "#1565C0",    # Azul oscuro
            "accent": "#90CAF9",       # Azul claro
            "text": "#000000",         # Negro
            "highlight": "#757575",    # Gris
        }

        # Configuración del fondo
        self.camera.background_color = self.colors["background"]

        # Título al inicio
        title = Text("El Concepto de Derivada", font="Arial", color=self.colors["primary"]).scale(1.2)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=self.colors["accent"]).match_width(title).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(underline))

        # Crear cuadro de diálogo fijo
        dialog = self.create_dialog("Una función es una relación entre \"x\" y \"f(x)\", donde cada \"x\" tiene un único \"f(x)\".", animate=True)
        self.wait(4)

        # Paso 1: Explicar qué es una función y mostrar la gráfica
        self.update_dialog(dialog, "Por ejemplo, aquí está la función $f(x) = x^2$.")
        axes = Axes(
            x_range=[-2, 6, 1],
            y_range=[-1, 10, 1],
            axis_config={"color": self.colors["text"]}
        ).scale(0.8).shift(UP * 1.5)
        graph = axes.plot(lambda x: x**2, x_range=[-2, 5], color=self.colors["primary"], stroke_width=3)
        graph_label = MathTex("f(x) = x^2", color=self.colors["text"]).scale(0.7).next_to(graph, RIGHT, buff=0.5)
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(4)

        # Paso 2: Explicar el cambio (Δ)
        self.update_dialog(dialog, "$\\Delta$ representa un cambio en una cantidad.")
        self.wait(4)
        self.update_dialog(dialog, "Por ejemplo, $\\Delta x$ es un cambio en \"x\".")
        delta_x_arrow = Arrow(
            start=axes.coords_to_point(1, 1),
            end=axes.coords_to_point(2, 4),
            color=self.colors["highlight"]
        )
        self.play(Create(delta_x_arrow))
        self.wait(4)

        # Explicación de Δy en la gráfica
        self.update_dialog(dialog, "$\\Delta y$ es el cambio en el valor de la función.")
        delta_y_line = Line(
            start=axes.coords_to_point(2, 0),
            end=axes.coords_to_point(2, 4),
            color=self.colors["secondary"]
        )
        self.play(Create(delta_y_line))
        self.wait(4)

        # Mostrar un punto en la gráfica
        self.update_dialog(dialog, "Marquemos un punto en la curva para visualizar estos cambios.")
        point = Dot(axes.coords_to_point(1, 1), color=self.colors["secondary"])
        self.play(FadeIn(point))
        self.wait(4)

        # Paso 3: Explicar qué es una pendiente
        self.update_dialog(dialog, "La pendiente se define como:")
        slope_eq = MathTex("\\text{Pendiente} = \\frac{\\Delta y}{\\Delta x}", color=self.colors["text"]).next_to(axes, DOWN)
        self.play(Write(slope_eq))
        self.wait(4)
        self.play(FadeOut(slope_eq))
        self.update_dialog(dialog, "Nos dice qué tan inclinada está una línea.")
        self.wait(4)

        # Paso 4: Explicar qué es una línea tangente
        self.update_dialog(dialog, "Una línea tangente toca la curva en un solo punto.")
        
        # Calcular la pendiente de la tangente manualmente
        x0 = 1
        slope = 2 * x0  # Derivada de f(x) = x^2 en x0=1 es 2*x0
        tangent_line = Line(
            start=axes.coords_to_point(x0 - 1, (x0 - 1)**2 + slope * (x0 - 1 - x0)),
            end=axes.coords_to_point(x0 + 1, (x0 + 1)**2 + slope * (x0 + 1 - x0)),
            color=self.colors["accent"]
        )
        self.play(Create(tangent_line))
        self.wait(4)
        self.update_dialog(dialog, "Tiene la misma pendiente que la curva en ese punto.")
        self.wait(4)

        # Explicación de la pendiente de la tangente
        self.update_dialog(dialog, "La pendiente de la tangente nos muestra la tasa de cambio instantánea en ese punto.")
        self.wait(4)

        # Paso 5: Introducir la idea de la derivada
        self.update_dialog(dialog, "La derivada es la pendiente de la tangente en un punto.")
        deriv_eq = MathTex(
            "f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}", 
            color=self.colors["text"]
        ).next_to(axes, DOWN)
        self.play(Write(deriv_eq))
        self.wait(4)
        self.play(FadeOut(deriv_eq))
        self.update_dialog(dialog, "Esta fórmula nos da la pendiente de la tangente en un punto.")
        self.wait(4)

        # Explicación de los términos en la fórmula de la derivada
        self.update_dialog(dialog, "Desglosemos la fórmula.")
        term1 = MathTex("f(x + h)", color=self.colors["text"]).next_to(axes, UP, buff=1)
        self.play(Write(term1))
        self.wait(4)
        self.update_dialog(dialog, "$f(x + h)$ es el valor de la función cuando \"x\" aumenta por un pequeño valor \"h\".")
        self.wait(4)
        self.play(FadeOut(term1))

        term2 = MathTex("f(x)", color=self.colors["text"]).next_to(axes, UP, buff=1)
        self.play(Write(term2))
        self.wait(4)
        self.update_dialog(dialog, "$f(x)$ es el valor original de la función en \"x\".")
        self.wait(4)
        self.play(FadeOut(term2))

        # Mostrar la expansión de $f(x + h)$
        self.update_dialog(dialog, "Expresamos $f(x + h)$:")
        func_expansion = MathTex("f(x + h) = (x + h)^2 = x^2 + 2xh + h^2", color=self.colors["text"]).next_to(axes, UP, buff=1)
        self.play(Write(func_expansion))
        self.wait(4)
        self.play(FadeOut(func_expansion))

        # Mostrar cómo se simplifica el numerador
        self.update_dialog(dialog, "Restamos $f(x)$ de $f(x + h)$:")
        simplification_eq = MathTex(
            "\\frac{f(x + h) - f(x)}{h} = \\frac{2xh + h^2}{h} = 2x + h", 
            color=self.colors["text"]
        ).next_to(axes, UP, buff=1)
        self.play(Write(simplification_eq))
        self.wait(4)
        self.play(FadeOut(simplification_eq))

        # Explicación de cómo se simplifica con el límite
        self.update_dialog(dialog, "Cuando $h \\to 0$, encontramos la pendiente exacta.")
        limit_eq = MathTex("f'(x) = \\lim_{h \\to 0} (2x + h) = 2x", color=self.colors["text"]).next_to(axes, UP, buff=1)
        self.play(Write(limit_eq))
        self.wait(4)
        self.play(FadeOut(limit_eq))

        # Mostrar la derivada en un punto específico
        self.update_dialog(dialog, "La derivada en $x=1$ es la pendiente de la tangente.")
        tangent_value = MathTex("f'(1) = 2", color=self.colors["highlight"], font_size=48).next_to(axes, RIGHT, buff=0.5)
        self.play(Write(tangent_value))
        self.play(Indicate(tangent_value, color=self.colors["highlight"], scale_factor=1.2))
        self.wait(4)
        self.play(FadeOut(tangent_value))

        # Conectar el concepto con integrales
        self.update_dialog(dialog, "Las derivadas nos indican cómo cambia una función en un punto.")
        self.wait(4)
        self.update_dialog(dialog, "Para encontrar áreas bajo una curva, usamos integrales.")
        self.wait(4)
        self.update_dialog(dialog, "Exploraremos esto en un siguiente video.")
        self.wait(4)

        # Finalizar la animación
        self.play(
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(graph_label),
            FadeOut(delta_x_arrow),
            FadeOut(delta_y_line),
            FadeOut(point),
            FadeOut(tangent_line),
            run_time=3
        )
        self.wait(1)

    # Método para crear el cuadro de diálogo
    def create_dialog(self, message, animate=False):
        bubble_base = RoundedRectangle(
            corner_radius=0.2,
            width=12,
            height=2,
            color=self.colors["accent"],
            fill_color=self.colors["accent"],
            fill_opacity=0.1
        )
        tail = Polygon(
            bubble_base.get_bottom() + DOWN * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + LEFT * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + RIGHT * 0.5,
            color=self.colors["accent"],
            fill_color=self.colors["accent"],
            fill_opacity=0.1
        )
        bubble = VGroup(bubble_base, tail).to_edge(DOWN, buff=0.1)
        dialog_text = Tex(
            message,
            font_size=30,
            color=self.colors["text"]
        ).move_to(bubble_base.get_center())

        if animate:
            self.play(FadeIn(bubble), Write(dialog_text))
        else:
            self.add(bubble, dialog_text)
        return VGroup(bubble, dialog_text)

    # Método para actualizar el cuadro de diálogo
    def update_dialog(self, dialog, new_message):
        dialog_text = dialog[1]
        new_dialog_text = Tex(
            new_message,
            font_size=30,
            color=self.colors["text"]
        ).move_to(dialog_text.get_center())
        self.play(Transform(dialog_text, new_dialog_text))