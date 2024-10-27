from manim import *
import numpy as np

class DetailedNeuralNetwork(Scene):
    def construct(self):
        # Configuración inicial de la escena
        self.setup_scene()

        # Introducción visual con elementos gráficos
        self.introduce_neural_network()

        # Creación de las capas de la red neuronal
        layers = self.create_network_layers()

        # Conexión de las capas con animaciones detalladas
        connections = self.connect_network_layers(layers)

        # Explicación de los componentes de la red neuronal
        self.explain_components(layers)

        # Animación de la propagación hacia adelante
        self.animate_forward_propagation(layers, connections)

        # Mostrar ecuaciones y explicar el funcionamiento matemático
        self.show_equations()

        # Simular el entrenamiento con retropropagación
        self.simulate_backpropagation(layers, connections)

        # Conclusión y mensaje final
        self.conclusion()

    def setup_scene(self):
        # Paleta de colores agradable
        self.colors = {
            "background": "#D6EAF8",  # Azul claro para el fondo
            "neuron": "#154360",      # Azul oscuro para las neuronas
            "input": "#76D7C4",       # Verde agua para la capa de entrada
            "hidden": "#F5B041",      # Naranja para capas ocultas
            "output": "#E74C3C",      # Rojo para la capa de salida
            "connection": "#1F618D",  # Azul para las conexiones
            "active": "#F4D03F",      # Amarillo para activación
            "text": "#1B2631"         # Gris oscuro para el texto
        }

        # Configurar el fondo
        self.camera.background_color = self.colors["background"]

    def introduce_neural_network(self):
        # Título principal con animación
        title = Text(
            "Visualización Detallada de una Red Neuronal",
            font_size=48,
            color=self.colors["text"]
        ).to_edge(UP)

        # Imagen representativa de una neurona (opcional)
        # Asegúrate de tener 'neuron.svg' en tu directorio
        neuron_image = SVGMobject("neuron.svg").scale(1.5)
        neuron_image.set_fill(self.colors["input"], opacity=1)
        neuron_image.set_stroke(color=self.colors["neuron"], width=2)
        neuron_image.next_to(title, DOWN, buff=0.5)

        # Animación de introducción
        self.play(
            Write(title),
            FadeIn(neuron_image, shift=DOWN)
        )
        self.wait(2)
        self.play(FadeOut(neuron_image))

        # Breve explicación
        intro_text = Text(
            "Las redes neuronales son modelos computacionales inspirados\n"
            "en el cerebro humano. Aprenden ajustando pesos sinápticos\n"
            "para realizar tareas complejas.",
            font_size=28,
            color=self.colors["text"]
        )
        intro_text.next_to(title, DOWN, buff=1.0)
        self.play(Write(intro_text))
        self.wait(4)
        self.play(FadeOut(intro_text))

    def create_network_layers(self):
        # Crear las capas de la red neuronal con animaciones atractivas
        input_layer = self.create_layer(4, LEFT * 5, "Capa de Entrada", self.colors["input"])
        hidden_layer1 = self.create_layer(5, LEFT * 2, "Capa Oculta 1", self.colors["hidden"])
        hidden_layer2 = self.create_layer(5, RIGHT * 1, "Capa Oculta 2", self.colors["hidden"])
        output_layer = self.create_layer(3, RIGHT * 5, "Capa de Salida", self.colors["output"])

        layers = [input_layer, hidden_layer1, hidden_layer2, output_layer]
        return layers

    def create_layer(self, n_neurons, position, label_text, neuron_color):
        # Crear neuronas con diseño mejorado
        neurons = VGroup()
        for i in range(n_neurons):
            neuron = Circle(radius=0.3, color=self.colors["neuron"], fill_opacity=1)
            neuron.set_fill(neuron_color, opacity=0.9)
            neurons.add(neuron)

        neurons.arrange(DOWN, buff=0.5).move_to(position)

        # Etiqueta de la capa con fondo y borde
        label_bg = Rectangle(
            width=3.5,
            height=0.6,
            fill_color=self.colors["background"],
            fill_opacity=1,
            stroke_color=self.colors["neuron"],
            stroke_width=1
        ).next_to(neurons, UP, buff=0.2)
        label = Text(label_text, font_size=24, color=self.colors["text"]).move_to(label_bg.get_center())

        # Mostrar neuronas y etiqueta con animación
        self.play(
            LaggedStart(*[DrawBorderThenFill(neuron) for neuron in neurons], lag_ratio=0.1),
            FadeIn(label_bg),
            Write(label)
        )

        # Devolver un diccionario con neuronas y etiqueta para futuras referencias
        return {"neurons": neurons, "label": label, "color": neuron_color}

    def connect_network_layers(self, layers):
        connections = []
        for i in range(len(layers) - 1):
            conn = self.connect_layers(layers[i], layers[i + 1])
            connections.append(conn)
        return connections

    def connect_layers(self, layer1, layer2):
        # Conectar neuronas entre dos capas con líneas curvas
        connections = VGroup()
        for neuron1 in layer1["neurons"]:
            for neuron2 in layer2["neurons"]:
                line = CubicBezier(
                    neuron1.get_right(),
                    neuron1.get_right() + RIGHT * 0.5,
                    neuron2.get_left() + LEFT * 0.5,
                    neuron2.get_left(),
                    stroke_width=1.5,
                    color=self.colors["connection"]
                )
                connections.add(line)
        self.play(Create(connections, run_time=2))
        # Guardar las conexiones para animaciones futuras
        layer2["connections_in"] = connections
        return connections

    def explain_components(self, layers):
        # Resaltar una neurona y explicar su función
        sample_neuron = layers[1]["neurons"][2].copy()
        sample_neuron.set_fill(self.colors["active"], opacity=1)
        self.play(Indicate(sample_neuron, scale_factor=1.2))
        neuron_explanation = Text(
            "Las neuronas procesan la información recibida y generan una salida.",
            font_size=24,
            color=self.colors["text"]
        ).to_edge(DOWN)
        self.play(Write(neuron_explanation))
        self.wait(3)
        self.play(FadeOut(neuron_explanation), sample_neuron.animate.set_fill(layers[1]["color"], opacity=0.9))

        # Resaltar una conexión y explicar su función
        sample_connection = layers[1]["connections_in"][5].copy()
        sample_connection.set_stroke(self.colors["active"], width=3)
        self.play(Indicate(sample_connection, scale_factor=1.05))
        connection_explanation = Text(
            "Las conexiones representan los pesos que determinan la influencia entre neuronas.",
            font_size=24,
            color=self.colors["text"]
        ).to_edge(DOWN)
        self.play(Write(connection_explanation))
        self.wait(3)
        self.play(FadeOut(connection_explanation), sample_connection.animate.set_stroke(self.colors["connection"], width=1.5))

    def animate_forward_propagation(self, layers, connections):
        # Animar la propagación de información con mejores animaciones
        propagation_text = Text(
            "Propagación hacia adelante (Forward Propagation)",
            font_size=28,
            color=self.colors["text"]
        ).to_edge(DOWN)
        self.play(Write(propagation_text))

        # Resaltar neuronas y conexiones en secuencia con animaciones suaves
        for i in range(len(layers) - 1):
            current_layer = layers[i]
            next_layer = layers[i + 1]
            current_connections = connections[i]

            # Resaltar neuronas actuales
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.1)
                for neuron in current_layer["neurons"]
            ], run_time=0.5)

            # Resaltar conexiones
            self.play(*[
                ShowPassingFlash(
                    conn.copy().set_stroke(self.colors["active"], width=2),
                    time_width=0.5,
                    run_time=1
                )
                for conn in current_connections
            ])

            # Resaltar neuronas siguientes
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.1)
                for neuron in next_layer["neurons"]
            ], run_time=0.5)

            self.wait(1)

            # Restaurar colores y tamaños originales
            self.play(*[
                neuron.animate.set_fill(current_layer["color"], opacity=0.9).scale(1/1.1)
                for neuron in current_layer["neurons"]
            ] + [
                neuron.animate.set_fill(next_layer["color"], opacity=0.9).scale(1/1.1)
                for neuron in next_layer["neurons"]
            ], run_time=0.5)

        self.play(FadeOut(propagation_text))

    def show_equations(self):
        # Mostrar ecuaciones y explicar el funcionamiento matemático
        equations = VGroup(
            Tex(r"$z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$", font_size=36, color=self.colors["text"]),
            Tex(r"$a^{(l)} = f(z^{(l)})$", font_size=36, color=self.colors["text"]),
            Tex(r"$f$: \text{Función de activación (ej. ReLU, Sigmoide)}$", font_size=28, color=self.colors["text"])
        ).arrange(DOWN, buff=0.5)
        equations.to_edge(UP)

        self.play(Write(equations))
        self.wait(4)
        self.play(FadeOut(equations))

    def simulate_backpropagation(self, layers, connections):
        # Simular el proceso de entrenamiento con retropropagación
        backprop_text = Text(
            "Retropropagación (Backpropagation)",
            font_size=28,
            color=self.colors["text"]
        ).to_edge(DOWN)
        self.play(Write(backprop_text))

        # Resaltar neuronas y conexiones en secuencia inversa
        for i in reversed(range(len(layers) - 1)):
            current_layer = layers[i + 1]
            previous_layer = layers[i]
            current_connections = connections[i]

            # Resaltar neuronas actuales (salida)
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.1)
                for neuron in current_layer["neurons"]
            ], run_time=0.5)

            # Resaltar conexiones inversas
            self.play(*[
                ShowPassingFlash(
                    conn.copy().set_stroke(self.colors["active"], width=2),
                    time_width=0.5,
                    run_time=1
                )
                for conn in current_connections
            ])

            # Resaltar neuronas anteriores
            self.play(*[
                neuron.animate.set_fill(self.colors["active"], opacity=1).scale(1.1)
                for neuron in previous_layer["neurons"]
            ], run_time=0.5)

            self.wait(1)

            # Restaurar colores y tamaños originales
            self.play(*[
                neuron.animate.set_fill(current_layer["color"], opacity=0.9).scale(1/1.1)
                for neuron in current_layer["neurons"]
            ] + [
                neuron.animate.set_fill(previous_layer["color"], opacity=0.9).scale(1/1.1)
                for neuron in previous_layer["neurons"]
            ], run_time=0.5)

        # Mostrar texto explicativo
        update_text = Text(
            "Ajuste de pesos para minimizar el error",
            font_size=24,
            color=self.colors["text"]
        ).next_to(backprop_text, UP, buff=0.5)
        self.play(Write(update_text))
        self.wait(3)
        self.play(FadeOut(backprop_text), FadeOut(update_text))

    def conclusion(self):
        # Conclusión y mensaje final
        conclusion_text = Text(
            "Las redes neuronales aprenden ajustando los pesos de las conexiones\n"
            "mediante la propagación hacia adelante y la retropropagación del error.",
            font_size=28,
            color=self.colors["text"]
        ).to_edge(DOWN)

        # Añadir una imagen o gráfico representativo (opcional)
        # Asegúrate de tener 'brain.svg' en tu directorio
        brain_image = SVGMobject("brain.svg").scale(1.5)
        brain_image.set_fill(self.colors["output"], opacity=1)
        brain_image.set_stroke(color=self.colors["neuron"], width=2)
        brain_image.next_to(conclusion_text, UP, buff=0.5)

        self.play(FadeIn(brain_image, shift=UP), Write(conclusion_text))
        self.wait(4)
        self.play(FadeOut(conclusion_text), FadeOut(brain_image))