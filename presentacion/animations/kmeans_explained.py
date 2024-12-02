from manim import *
import numpy as np

class KMeansExplained(Scene):
    def construct(self):
        # Configuración de la cámara y resolución
        self.camera.frame_width = 16  # Relación de aspecto 16:9
        self.camera.frame_height = 9

        # Configuración de colores
        colors = {
            "background": "#FFFFFF",   # Blanco
            "primary": "#1E88E5",      # Azul medio para puntos y centroides
            "secondary": "#43A047",    # Verde para otros elementos
            "accent": "#757575",       # Gris para líneas y detalles
            "text": "#000000",         # Negro para textos
            "highlight": "#FF5722",    # Naranja para resaltar
        }

        # Configuración del fondo
        self.camera.background_color = colors["background"]

        # Título al inicio
        title = Text("Método de K-Means", font="Arial", color=colors["primary"]).scale(1.2)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=colors["accent"]).match_width(title).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(underline))

        # Crear cuadro de diálogo fijo
        dialog = self.create_dialog("El algoritmo K-Means agrupa puntos en clusters basados en su proximidad a los centroides.", animate=True)
        self.wait(3)

        # Generación de datos de ejemplo
        self.update_dialog(dialog, "Primero, generamos datos de ejemplo que representan puntos en un espacio 2D.")
        np.random.seed(0)
        points = np.random.rand(50, 2)
        # Convertir puntos 2D a 3D agregando z=0
        points_3d = np.hstack((points, np.zeros((points.shape[0], 1))))
        dots = VGroup(*[Dot(point=point, radius=0.02, color=colors["primary"]) for point in points_3d])
        self.play(LaggedStart(*[Create(dot) for dot in dots], lag_ratio=0.05))
        self.wait(2)

        # Paso 1: Inicializar centroides
        self.update_dialog(dialog, "1. Inicializamos aleatoriamente los centroides de los clusters.")
        k = 3
        centroids = np.random.rand(k, 2)
        centroids_3d = np.hstack((centroids, np.zeros((centroids.shape[0], 1))))
        centroid_dots = VGroup(*[
            Dot(point=centroid, color=colors["highlight"], radius=0.05)
            for centroid in centroids_3d
        ])
        centroid_labels = VGroup(*[
            Text(f"C{i+1}", font_size=20, color=colors["text"]).next_to(dot, UP)
            for i, dot in enumerate(centroid_dots)
        ])
        self.play(LaggedStart(*[Create(dot) for dot in centroid_dots], lag_ratio=0.1))
        self.play(Write(centroid_labels))
        self.wait(2)

        # Paso 2: Asignar puntos al centroide más cercano
        self.update_dialog(dialog, "2. Asignamos cada punto al centroide más cercano.")
        
        def assign_to_clusters(points, centroids):
            clusters = [[] for _ in range(len(centroids))]
            lines = VGroup()
            for point in points:
                distances = [np.linalg.norm(point - centroid) for centroid in centroids]
                cluster_index = np.argmin(distances)
                clusters[cluster_index].append(point)
                line = Line(
                    start=point,
                    end=centroids[cluster_index],
                    stroke_width=1,
                    color=colors["accent"],
                    stroke_opacity=0.5  # Usar stroke_opacity en lugar de opacity
                )
                lines.add(line)
            return clusters, lines

        def update_centroids(clusters):
            new_centroids = []
            for cluster in clusters:
                if len(cluster) == 0:
                    # Manejar clusters vacíos re-inicializando aleatoriamente
                    new_centroid = np.random.rand(3)
                    new_centroid[2] = 0  # Asegurar z=0
                else:
                    new_centroid = np.mean(cluster, axis=0)
                new_centroids.append(new_centroid)
            return np.array(new_centroids)

        clusters, lines = assign_to_clusters(points_3d, centroids_3d)
        # Crear nuevos puntos coloreados por cluster
        cluster_dots = VGroup(*[
            VGroup(*[Dot(point=point, color=colors["primary"], radius=0.02) for point in cluster]) 
            for cluster in clusters
        ])
        self.play(Transform(dots, cluster_dots), Create(lines))
        self.wait(2)

        # Paso 3: Actualizar centroides
        self.update_dialog(dialog, "3. Actualizamos la posición de los centroides calculando la media de los puntos asignados.")
        new_centroids = update_centroids(clusters)
        centroid_dots_new = VGroup(*[
            Dot(point=centroid, color=colors["highlight"], radius=0.05)
            for centroid in new_centroids
        ])
        centroid_labels_new = VGroup(*[
            Text(f"C{i+1}", font_size=20, color=colors["text"]).next_to(dot, UP)
            for i, dot in enumerate(centroid_dots_new)
        ])
        self.play(Transform(centroid_dots, centroid_dots_new), Transform(centroid_labels, centroid_labels_new))
        self.wait(2)

        # Repetir pasos 2 y 3 hasta la convergencia
        max_iterations = 5
        for i in range(1, max_iterations + 1):
            self.update_dialog(dialog, f"Iteración {i}: Repetimos la asignación y actualización de centroides.")
            # Remover líneas anteriores
            self.play(FadeOut(lines))
            # Asignar clusters con nuevos centroides
            clusters, lines = assign_to_clusters(points_3d, new_centroids)
            # Crear nuevos cluster_dots
            cluster_dots = VGroup(*[
                VGroup(*[Dot(point=point, color=colors["primary"], radius=0.02) for point in cluster]) 
                for cluster in clusters
            ])
            # Animar transformación de puntos
            self.play(Transform(dots, cluster_dots))
            # Animar creación de nuevas líneas
            self.play(Create(lines))
            # Actualizar centroides
            old_centroids = new_centroids.copy()
            new_centroids = update_centroids(clusters)
            # Animar movimiento de centroides
            centroid_dots_new = VGroup(*[
                Dot(point=centroid, color=colors["highlight"], radius=0.05)
                for centroid in new_centroids
            ])
            self.play(Transform(centroid_dots, centroid_dots_new))
            # Actualizar etiquetas de centroides
            centroid_labels_new = VGroup(*[
                Text(f"C{i+1}", font_size=20, color=colors["text"]).next_to(dot, UP)
                for i, dot in enumerate(centroid_dots_new)
            ])
            self.play(Transform(centroid_labels, centroid_labels_new))
            self.wait(1)

        # Mostrar ecuaciones del K-Means
        self.update_dialog(dialog, "Las ecuaciones clave del algoritmo K-Means son las siguientes:")
        equations = VGroup(
            MathTex(r"d(\mathbf{x}_i, \mathbf{c}_j) = \sqrt{\sum_{k=1}^{n} (x_{ik} - c_{jk})^2}", color=colors["text"]),
            MathTex(r"\mathbf{c}_j = \frac{1}{|S_j|} \sum_{\mathbf{x}_i \in S_j} \mathbf{x}_i", color=colors["text"])
        ).arrange(DOWN, buff=0.5).scale(0.8).next_to(dialog, LEFT, buff=1)
        self.play(Create(equations))
        self.wait(4)

        # Explicación adicional de las ecuaciones
        self.update_dialog(dialog, "1. La primera ecuación calcula la distancia entre un punto y un centroide.\n2. La segunda ecuación actualiza la posición del centroide.")
        self.wait(4)

        # Finalizar
        self.update_dialog(dialog, "¡El algoritmo K-Means ha agrupado los puntos en clusters de manera efectiva!")
        self.wait(3)
        self.play(FadeOut(dots), FadeOut(centroid_dots), FadeOut(lines), FadeOut(centroid_labels),
                  FadeOut(dialog), FadeOut(equations))
        self.wait(1)

    # Método para crear el cuadro de diálogo
    def create_dialog(self, message, animate=False):
        bubble_base = RoundedRectangle(
            corner_radius=0.2,
            width=12,
            height=3,
            color="#757575",  # Gris para el borde
            fill_color="#757575",
            fill_opacity=0.1
        )
        tail = Polygon(
            bubble_base.get_bottom() + DOWN * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + LEFT * 0.5,
            bubble_base.get_bottom() + DOWN * 0.7 + RIGHT * 0.5,
            color="#757575",
            fill_color="#757575",
            fill_opacity=0.1
        )
        bubble = VGroup(bubble_base, tail).to_edge(DOWN, buff=0.5)
        dialog_text = Tex(
            message,
            font_size=24,  # Aumentar el tamaño de la fuente para mayor legibilidad
            color="#000000"  # Negro
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
            font_size=24,  # Aumentar el tamaño de la fuente para mayor legibilidad
            color="#000000"  # Negro
        ).move_to(dialog_text.get_center())
        self.play(Transform(dialog_text, new_dialog_text))

    # Método para limpiar el cuadro de diálogo
    def clear_dialog(self, dialog):
        dialog_text = dialog[1]
        self.play(FadeOut(dialog_text))