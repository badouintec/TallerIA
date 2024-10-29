from manim import *
import sympy as sp
from sympy import MatrixSymbol, HadamardProduct, Function, Eq, pretty

class DetailedNeuralNetwork(Scene):
    def construct(self):
        # Configuración inicial de la escena
        self.setup_scene()

        # Paso 1: Introducción visual con un dibujo de una neurona
        self.introduce_neuron()

        # Paso 2: Mostrar título y subtítulo brevemente, y luego ocultarlos
        self.show_title_and_subtitle()

        # Paso 3: Crear las capas de la red neuronal
        layers = self.create_network_layers()

        # Paso 4: Conectar las capas de la red neuronal
        connections = self.connect_network_layers(layers)

        # Paso 5: Explicación detallada de los elementos
        self.explain_elements(layers, connections)

        # Paso 6: Explicación de la propagación hacia adelante
        self.explain_forward_propagation()

        # Paso 7: Animar la propagación hacia adelante a través de la red
        self.animate_forward_propagation(layers, connections)

        # Paso 8: Simular retropropagación
        self.simulate_backpropagation(layers, connections)

        # Paso 9: Mostrar las ecuaciones correspondientes usando SymPy
        self.show_equations()

        # Paso 10: Conclusión final
        self.conclusion()

    def setup_scene(self):
        """
        Configuración inicial de la escena, con la definición de colores y fondo.
        """
        self.colors = {
            "background": "#2E4053",
            "neuron": "#F0B27A",
            "input": "#52BE80",
            "hidden": "#AF7AC5",
            "output": "#E74C3C",
            "connection": "#85C1E9",
            "active": "#F1C40F",
            "text": "#FFFFFF",
            "highlight": "#F1948A"
        }
        self.camera.background_color = self.colors["background"]

    def introduce_neuron(self):
        """
        Introducción visual con un dibujo de una neurona sencilla.
        """
        # Cuerpo de la neurona
        neuron_body = Circle(
            radius=0.5,
            color=self.colors["neuron"],
            fill_color=self.colors["neuron"],
            fill_opacity=1
        ).shift(UP * 2)

        # Dendritas
        dendrites = VGroup(
            Line(neuron_body.get_left(), neuron_body.get_left() + LEFT * 1.0, color=self.colors["connection"], stroke_opacity=0.6),
            Line(neuron_body.get_top(), neuron_body.get_top() + UP * 1.0, color=self.colors["connection"], stroke_opacity=0.6),
            Line(neuron_body.get_bottom(), neuron_body.get_bottom() + DOWN * 1.0, color=self.colors["connection"], stroke_opacity=0.6),
            Line(neuron_body.get_right(), neuron_body.get_right() + RIGHT * 1.0, color=self.colors["connection"], stroke_opacity=0.6)
        )

        # Axón
        axon = Line(neuron_body.get_right(), neuron_body.get_right() + RIGHT * 2.0, color=self.colors["connection"], stroke_opacity=0.6)
        axon_terminal = VGroup(
            Line(axon.get_end(), axon.get_end() + UP * 0.3, color=self.colors["connection"], stroke_opacity=0.6),
            Line(axon.get_end(), axon.get_end() + DOWN * 0.3, color=self.colors["connection"], stroke_opacity=0.6)
        )

        neuron = VGroup(neuron_body, dendrites, axon, axon_terminal)

        # Añadir etiqueta a la neurona
        neuron_label = Text("Neurona", font_size=24, color=self.colors["text"], font="Arial").next_to(neuron_body, DOWN)
        neuron_group = VGroup(neuron, neuron_label)

        # Animación de introducción
        self.play(FadeIn(neuron, shift=UP), Write(neuron_label))
        self.wait(1)
        self.play(FadeOut(neuron_group))

    def show_title_and_subtitle(self):
        """
        Mostrar título y subtítulo brevemente y luego ocultarlos.
        """
        title = Text(
            "Visualización de una Red Neuronal",
            font_size=48,
            color=self.colors["text"],
            font="Arial"
        ).to_edge(UP)

        subtitle = Text(
            "Inspirada en la estructura del cerebro humano",
            font_size=32,
            color=self.colors["text"],
            font="Arial"
        ).next_to(title, DOWN)

        # Animación de entrada
        self.play(FadeIn(title, shift=DOWN), FadeIn(subtitle, shift=DOWN))
        self.wait(2)

        # Animación de salida
        self.play(FadeOut(title, shift=DOWN), FadeOut(subtitle, shift=DOWN))

    def create_network_layers(self):
        """
        Crea las capas de la red neuronal con neuronas visualizadas como círculos.
        """
        # Definir número de neuronas por capa
        self.layer_sizes = [5, 7, 7, 5, 3]  # Ejemplo: 5 entradas, tres capas ocultas de 7, 5 y 3 salidas

        # Posiciones horizontales para cada capa
        layer_positions = [LEFT * 6, LEFT * 3, ORIGIN, RIGHT * 3, RIGHT * 6]

        # Definir tipos de capas
        layer_types = ['input', 'hidden', 'hidden', 'hidden', 'output']

        layers = []

        for i, (size, position, layer_type) in enumerate(zip(self.layer_sizes, layer_positions, layer_types)):
            if layer_type == 'input':
                label_text = "Entrada"
                neuron_color = self.colors["input"]
            elif layer_type == 'output':
                label_text = "Salida"
                neuron_color = self.colors["output"]
            else:
                label_text = f"Capa Oculta {i}"  # Numeración de capas ocultas
                neuron_color = self.colors["hidden"]

            layer = self.create_layer(size, position, label_text, neuron_color)
            layers.append(layer)

        self.layers = layers  # Guardar las capas para uso posterior
        return layers

    def create_layer(self, n_neurons, position, label_text, neuron_color):
        """
        Crea una capa de neuronas en una posición específica.
        """
        neurons = VGroup()
        for _ in range(n_neurons):
            neuron = Circle(
                radius=0.3,
                color=self.colors["neuron"],
                fill_opacity=1
            )
            neuron.set_fill(neuron_color, opacity=0.9)
            neurons.add(neuron)

        neurons.arrange(DOWN, buff=0.6).move_to(position)

        # Añadir etiqueta a la capa
        label = Text(label_text, font_size=24, color=self.colors["text"], font="Arial").next_to(neurons, UP, buff=0.5)

        # Animación de creación de la capa
        self.play(
            LaggedStart(*[GrowFromCenter(neuron) for neuron in neurons], lag_ratio=0.1),
            FadeIn(label, shift=UP)
        )

        return {"neurons": neurons, "label": label, "color": neuron_color}

    def connect_network_layers(self, layers):
        """
        Conecta las capas de la red neuronal usando líneas que representan las conexiones.
        """
        connections = []

        for i in range(len(layers) - 1):
            layer1 = layers[i]
            layer2 = layers[i + 1]
            conn = self.connect_layers(layer1, layer2)
            connections.append(conn)

        self.connections = connections  # Guardar conexiones para uso posterior
        return connections

    def connect_layers(self, layer1, layer2):
        """
        Conecta dos capas de la red neuronal dibujando líneas entre las neuronas.
        """
        connections = VGroup()
        for neuron1 in layer1["neurons"]:
            for neuron2 in layer2["neurons"]:
                line = Line(
                    neuron1.get_right(),
                    neuron2.get_left(),
                    stroke_width=1.0,
                    color=self.colors["connection"],
                    stroke_opacity=0.6  # Reemplazar 'opacity' con 'stroke_opacity'
                )
                connections.add(line)

        # Animación de conexiones
        self.play(Create(connections), run_time=1.5)

        layer2["connections_in"] = connections
        return connections

    def explain_elements(self, layers, connections):
        """
        Explicación detallada de las neuronas y conexiones.
        """
        # Explicación de las neuronas
        neuron_explanation = Text(
            "Las neuronas son unidades básicas que reciben, procesan y transmiten información.",
            font_size=24,
            color=self.colors["text"],
            font="Arial",
            t2c={"neuronas": self.colors["neuron"]}
        ).to_edge(DOWN)

        # Animación de entrada
        self.play(FadeIn(neuron_explanation, shift=UP))
        self.wait(3)

        # Resaltar una neurona de entrada
        input_layer = layers[0]  # Asumiendo que la primera capa es de entrada
        sample_neuron = input_layer["neurons"][0]
        self.play(
            sample_neuron.animate.set_fill(self.colors["highlight"], opacity=1).scale(1.2)
        )
        self.wait(1)

        # Añadir una flecha apuntando a la neurona resaltada
        arrow = Arrow(
            start=LEFT * 5,
            end=sample_neuron.get_left(),
            buff=0.1,
            color=self.colors["highlight"]
        )
        self.play(GrowArrow(arrow))
        self.wait(2)

        # Explicación de las conexiones
        connection_explanation = Text(
            "Las líneas representan las conexiones sinápticas entre las neuronas,\n"
            "a través de las cuales se transmite la información.",
            font_size=24,
            color=self.colors["text"],
            font="Arial",
            t2c={"conexiones sinápticas": self.colors["connection"]}
        ).to_edge(DOWN)

        self.play(FadeOut(neuron_explanation), FadeOut(arrow))
        self.play(FadeIn(connection_explanation, shift=UP))
        self.wait(3)

        # Resaltar una conexión
        sample_connection = connections[0][0]  # Primera conexión de la primera capa
        self.play(
            sample_connection.animate.set_color(self.colors["highlight"]).set_stroke(width=2)
        )
        self.wait(1)

        # Añadir una flecha apuntando a la conexión resaltada
        arrow_conn = Arrow(
            start=LEFT * 5,
            end=sample_connection.get_center(),
            buff=0.1,
            color=self.colors["highlight"]
        )
        self.play(GrowArrow(arrow_conn))
        self.wait(2)

        # Finalizar explicaciones
        self.play(FadeOut(connection_explanation), FadeOut(arrow_conn), FadeOut(sample_connection))

    def explain_forward_propagation(self):
        """
        Explicación de la propagación hacia adelante.
        """
        explanation_text = Text(
            "La información se propaga hacia adelante\n"
            "desde la capa de entrada hasta la capa de salida.",
            font_size=28,
            color=self.colors["text"],
            font="Arial",
            t2c={"información": self.colors["active"], "propaga hacia adelante": self.colors["active"]}
        ).to_edge(DOWN)

        self.play(FadeIn(explanation_text, shift=UP))
        self.wait(3)
        self.play(FadeOut(explanation_text, shift=DOWN))

    def animate_forward_propagation(self, layers, connections):
        """
        Simula el proceso de propagación hacia adelante.
        """
        propagation_text = Text(
            "Propagación hacia adelante",
            font_size=32,
            color=self.colors["active"],
            font="Arial"
        ).to_edge(UP)

        self.play(FadeIn(propagation_text, shift=DOWN))
        self.wait(1)

        for i in range(len(layers) - 1):
            current_layer = layers[i]
            next_layer = layers[i + 1]
            current_connections = connections[i]

            # Resaltar neuronas de la capa actual
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.2)
                for neuron in current_layer["neurons"]
            ], run_time=0.5)

            # Resaltar conexiones
            self.play(*[
                conn.animate.set_color(self.colors["active"]).set_stroke(width=2)
                for conn in current_connections
            ], run_time=1)

            # Resaltar neuronas de la siguiente capa
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.2)
                for neuron in next_layer["neurons"]
            ], run_time=0.5)

            self.wait(0.5)

            # Restaurar colores y tamaños originales
            self.play(*[
                neuron.animate.set_fill(current_layer["color"], opacity=0.9).scale(1/1.2)
                for neuron in current_layer["neurons"]
            ] + [
                conn.animate.set_color(self.colors["connection"]).set_stroke(width=1)
                for conn in current_connections
            ] + [
                neuron.animate.set_fill(next_layer["color"], opacity=0.9).scale(1/1.2)
                for neuron in next_layer["neurons"]
            ], run_time=0.5)

        self.play(FadeOut(propagation_text, shift=DOWN))
        self.wait(1)

    def simulate_backpropagation(self, layers, connections):
        """
        Simula el proceso de retropropagación.
        """
        backprop_text = Text(
            "Retropropagación",
            font_size=32,
            color=self.colors["active"],
            font="Arial"
        ).to_edge(UP)

        self.play(FadeIn(backprop_text, shift=DOWN))
        self.wait(1)

        for i in reversed(range(len(layers) - 1)):
            current_layer = layers[i + 1]
            previous_layer = layers[i]
            current_connections = connections[i]

            # Resaltar neuronas de la capa actual
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.2)
                for neuron in current_layer["neurons"]
            ], run_time=0.5)

            # Resaltar conexiones (invertidas)
            self.play(*[
                conn.animate.set_color(self.colors["active"]).set_stroke(width=2)
                for conn in current_connections
            ], run_time=1)

            # Resaltar neuronas de la capa previa
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.2)
                for neuron in previous_layer["neurons"]
            ], run_time=0.5)

            self.wait(0.5)

            # Restaurar colores y tamaños originales
            self.play(*[
                neuron.animate.set_fill(current_layer["color"], opacity=0.9).scale(1/1.2)
                for neuron in current_layer["neurons"]
            ] + [
                conn.animate.set_color(self.colors["connection"]).set_stroke(width=1)
                for conn in current_connections
            ] + [
                neuron.animate.set_fill(previous_layer["color"], opacity=0.9).scale(1/1.2)
                for neuron in previous_layer["neurons"]
            ], run_time=0.5)

        self.play(FadeOut(backprop_text, shift=DOWN))
        self.wait(1)

    def show_equations(self):
        """
        Muestra las ecuaciones de propagación hacia adelante y retropropagación usando SymPy con Text y Unicode.
        """
        # Definir símbolos y ecuaciones con SymPy
        l = 0  # índice de la capa actual

        # Verificar que hay al menos dos capas para definir W(l)
        if len(self.layer_sizes) < 2:
            raise ValueError("Se requieren al menos dos capas para definir las ecuaciones.")

        # Definir W_l con dimensiones correctas
        W_l = MatrixSymbol(f'W_{l}', self.layer_sizes[l+1], self.layer_sizes[l])

        # Definir vectores de activación y bias como MatrixSymbols
        a_l = MatrixSymbol(f'a_{l}', self.layer_sizes[l], 1)
        b_l = MatrixSymbol(f'b_{l}', self.layer_sizes[l+1], 1)

        # Definir z_l y la función de activación
        z_l = W_l * a_l + b_l
        f_z_l = Function('f')(z_l)  # [7,1]

        # Ecuación de propagación hacia adelante
        a_next = MatrixSymbol(f'a_{l+1}', self.layer_sizes[l+1], 1)
        forward_eq = Eq(a_next, f_z_l, evaluate=False)  # 'a₁ = f(z₀)'

        # Definir delta para retropropagación
        delta_prev = MatrixSymbol(f'delta_{l+1}', self.layer_sizes[l+1], 1)
        delta_l = MatrixSymbol(f'delta_{l}', self.layer_sizes[l], 1)

        # Ecuación de retropropagación
        f_prime_z_l = Function('f_prime')(z_l)  # [7,1]
        Hadamard = HadamardProduct(delta_prev, f_prime_z_l)  # Multiplicación elemento a elemento [7,1]
        backward_eq = Eq(delta_l, W_l.transpose() * Hadamard, evaluate=False)  # 'delta₀ = W₀ᵀ ⋅ (HadamardProduct(delta₁, f_prime(z₀)))'

        # Convertir ecuaciones a cadenas con formato legible usando SymPy's pretty
        forward_eq_str = pretty(forward_eq, use_unicode=True)
        backward_eq_str = pretty(backward_eq, use_unicode=True)

        # **Depuración: Imprimir las ecuaciones para verificar su formato**
        print(f"forward_eq_str: '{forward_eq_str}'")
        print(f"backward_eq_str: '{backward_eq_str}'")

        # Crear objetos Text en Manim para cada ecuación
        # Usar una fuente monoespaciada para mejorar la alineación
        forward_eq_text = Text(forward_eq_str, font_size=24, font="Consolas", color=self.colors["text"], line_spacing=0.8).to_edge(UP)
        backward_eq_text = Text(backward_eq_str, font_size=24, font="Consolas", color=self.colors["text"], line_spacing=0.8).next_to(forward_eq_text, DOWN, buff=0.8)

        # Ajustar el tamaño y posición para evitar recortes
        forward_eq_text.scale(0.8).to_edge(UP + LEFT * 0.5)
        backward_eq_text.scale(0.8).next_to(forward_eq_text, DOWN, buff=0.8)

        # Mostrar ecuaciones
        self.play(FadeIn(forward_eq_text, shift=UP))
        self.wait(2)
        self.play(FadeIn(backward_eq_text, shift=UP))
        self.wait(2)

        # Resaltar 'a₁' en la ecuación de propagación hacia adelante
        highlight_forward = 'a₁'
        if highlight_forward in forward_eq_str:
            # Encontrar la posición de 'a₁' en la cadena
            index = forward_eq_str.find(highlight_forward)
            # Calcular el desplazamiento basado en el índice
            total_length = len(forward_eq_str)
            text_width = forward_eq_text.width
            char_width = text_width / total_length
            highlight_position = forward_eq_text.get_left() + RIGHT * (index * char_width + char_width / 2)

            # Crear un objeto Text para resaltar
            highlighted_forward = Text(highlight_forward, font_size=24, font="Consolas", color=self.colors["highlight"]).move_to(highlight_position)

            # Animar el resaltado
            self.play(FadeIn(highlighted_forward))
            self.wait(1)
            self.play(FadeOut(highlighted_forward))
        else:
            print(f"No se encontró '{highlight_forward}' en la ecuación de propagación hacia adelante.")

        # Resaltar 'delta₀' en la ecuación de retropropagación
        highlight_backward = 'delta₀'
        if highlight_backward in backward_eq_str:
            # Encontrar la posición de 'delta₀' en la cadena
            index = backward_eq_str.find(highlight_backward)
            # Calcular el desplazamiento basado en el índice
            total_length = len(backward_eq_str)
            text_width = backward_eq_text.width
            char_width = text_width / total_length
            highlight_position = backward_eq_text.get_left() + RIGHT * (index * char_width + char_width / 2)

            # Crear un objeto Text para resaltar
            highlighted_backward = Text(highlight_backward, font_size=24, font="Consolas", color=self.colors["highlight"]).move_to(highlight_position)

            # Animar el resaltado
            self.play(FadeIn(highlighted_backward))
            self.wait(1)
            self.play(FadeOut(highlighted_backward))
        else:
            print(f"No se encontró '{highlight_backward}' en la ecuación de retropropagación.")

        self.wait(2)

        # Finalizar mostrando las ecuaciones
        self.play(FadeOut(VGroup(forward_eq_text, backward_eq_text)))

    def conclusion(self):
        """
        Conclusión de la animación con un mensaje final.
        """
        conclusion_text = Text(
            "Las redes neuronales aprenden ajustando los pesos de las conexiones\n"
            "mediante la propagación hacia adelante y la retropropagación del error.",
            font_size=28,
            color=self.colors["text"],
            font="Arial",
            t2c={"propagación hacia adelante": self.colors["active"], "retropropagación": self.colors["active"]}
        ).to_edge(DOWN)

        # Animación de conclusión
        self.play(FadeIn(conclusion_text, shift=UP))
        self.wait(4)
        self.play(FadeOut(conclusion_text, shift=DOWN))