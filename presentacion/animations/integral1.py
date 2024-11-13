from manim import *

class integral1(Scene):
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
        title = Text("El Concepto de Integral", font="Arial", color=self.colors["primary"]).scale(1.2)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=self.colors["accent"]).match_width(title).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(underline))

        # Crear cuadro de diálogo fijo
        dialog = self.create_dialog("Las integrales nos ayudan a encontrar el área bajo una curva.", animate=True)
        self.wait(4)

        # Mostrar la gráfica de la función
        self.update_dialog(dialog, "Aquí está la función $f(x) = x^2$.")
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 30, 5],
            axis_config={"color": self.colors["text"]}
        ).scale(0.8).shift(UP)
        graph = axes.plot(lambda x: x**2, x_range=[0, 5], color=self.colors["primary"], stroke_width=3)
        graph_label = MathTex("f(x) = x^2", color=self.colors["text"]).scale(0.7).next_to(graph, RIGHT, buff=0.5)
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(4)

        # Explicación de los límites de integración
        self.update_dialog(dialog, "Vamos a encontrar el área bajo la curva desde $x = 0$ hasta $x = 5$.")
        point_a = Dot(axes.coords_to_point(0, 0), color=self.colors["secondary"])
        point_b = Dot(axes.coords_to_point(5, 25), color=self.colors["secondary"])
        label_a = MathTex("0", color=self.colors["text"]).next_to(point_a, DOWN)
        label_b = MathTex("5", color=self.colors["text"]).next_to(point_b, DOWN)
        self.play(FadeIn(point_a, point_b), Write(label_a), Write(label_b))
        self.wait(6)

        # Sombrear la región bajo la curva y explicar su significado
        shaded_area = axes.get_area(graph, x_range=[0, 5], color=self.colors["accent"], opacity=0.3)
        self.play(Create(shaded_area))
        self.update_dialog(dialog, "El área bajo la curva representa la integral definida de $0$ a $5$.")
        self.wait(6)

        # Explicar el significado del área
        self.update_dialog(dialog, "Esta área se mide en unidades cuadradas.")
        self.wait(6)

        # Paso 2: Explicar la suma de áreas pequeñas
        self.update_dialog(dialog, "Dividimos el área en pequeños rectángulos para aproximar el área total.")
        rects = axes.get_riemann_rectangles(
            graph,
            x_range=[0, 5],
            dx=0.5,
            color=self.colors["accent"],
            stroke_width=0.5,
            fill_opacity=0.5
        )
        self.play(Create(rects))
        self.wait(6)

        # Explicación de la suma de las áreas de los rectángulos
        self.update_dialog(dialog, "La suma de sus áreas nos da una aproximación del área.")
        self.clear_dialog(dialog)
        sum_eq = MathTex(
            "\\text{Área} \\approx \\sum_{i=1}^{n} f(x_i) \\Delta x",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.play(Transform(dialog[1], sum_eq))
        self.wait(8)

        # Explicación del límite de la suma
        self.update_dialog(dialog, "Cuando el número de rectángulos tiende a infinito, obtenemos el área exacta.")
        integral_eq = MathTex(
            "\\int_{0}^{5} x^2\\,dx",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.play(Transform(dialog[1], integral_eq))
        self.wait(8)

        # Explicar el proceso de la antiderivada
        self.update_dialog(dialog, "La antiderivada de $f(x) = x^2$ es $\\frac{x^3}{3} + C$.")
        antiderivative_eq = MathTex(
            "F(x) = \\frac{x^3}{3} + C",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.play(Transform(dialog[1], antiderivative_eq))
        self.wait(8)

        # Explicación de la constante C
        self.update_dialog(dialog, "$C$ es la constante de integración.")
        self.wait(6)

        # Evaluar la antiderivada en los límites
        self.update_dialog(dialog, "Evaluamos la integral en los límites $0$ y $5$.")
        eval_eq = MathTex(
            "\\int_{0}^{5} x^2\\,dx = \\left[\\frac{x^3}{3}\\right]_{0}^{5}",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.play(Transform(dialog[1], eval_eq))
        self.wait(8)

        # Evaluación paso a paso
        self.update_dialog(dialog, "Sustituimos $5$ y $0$ en la antiderivada.")
        eval_steps = MathTex(
            "\\left[\\frac{5^3}{3}\\right] - \\left[\\frac{0^3}{3}\\right]",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.play(Transform(dialog[1], eval_steps))
        self.wait(8)

        # Mostrar el resultado de la evaluación
        eval_result = MathTex(
            "\\frac{125}{3}",
            color=self.colors["text"]
        ).move_to(dialog[0].get_center())
        self.update_dialog(dialog, "El área bajo la curva es $\\frac{125}{3}$ unidades cuadradas.")
        self.play(Transform(dialog[1], eval_result))
        self.wait(8)

        # Explicar el resultado en decimales y unidades
        self.update_dialog(dialog, "$\\frac{125}{3} \\approx 41.67$ unidades cuadradas.")
        self.wait(8)
        self.update_dialog(dialog, "Este valor representa el área total bajo la curva entre $0$ y $5$.")
        self.wait(8)

        # Conclusión y resumen final en el cuadro de diálogo
        self.update_dialog(dialog, "Las integrales y derivadas están conectadas. El siguiente paso es entender las ecuaciones diferenciales.")
        self.wait(8)

        # Desvanecer todo y mostrar resumen de ecuaciones
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(graph_label), FadeOut(rects), FadeOut(shaded_area), FadeOut(point_a), FadeOut(point_b), FadeOut(label_a), FadeOut(label_b), run_time=3)
        self.wait(1)

        # Mostrar todas las ecuaciones en orden sin el cuadro de diálogo
        self.play(FadeOut(dialog))
        final_explanation = VGroup(
            MathTex("\\text{Área} \\approx \\sum_{i=1}^{n} f(x_i) \\Delta x", color=self.colors["text"]),
            MathTex("\\int_{0}^{5} x^2\\,dx", color=self.colors["text"]),
            MathTex("F(x) = \\frac{x^3}{3} + C", color=self.colors["text"]),
            MathTex("\\int_{0}^{5} x^2\\,dx = \\left[\\frac{x^3}{3}\\right]_{0}^{5}", color=self.colors["text"]),
            MathTex("\\left[\\frac{5^3}{3}\\right] - \\left[\\frac{0^3}{3}\\right]", color=self.colors["text"]),
            MathTex("\\frac{125}{3} \\approx 41.67", color=self.colors["text"])
        ).arrange(DOWN, buff=0.5).scale(0.8).to_edge(UP)
        self.play(Create(final_explanation))
        self.wait(12)

        # Desvanecer las ecuaciones y finalizar la animación
        self.play(FadeOut(final_explanation), run_time=3)
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

    # Método para limpiar el cuadro de diálogo
    def clear_dialog(self, dialog):
        dialog_text = dialog[1]
        self.play(FadeOut(dialog_text))