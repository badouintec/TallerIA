import cairo
from PIL import Image

# Crear un contexto de imagen
WIDTH, HEIGHT = 1000, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Fondo blanco
context.set_source_rgb(1, 1, 1)
context.rectangle(0, 0, WIDTH, HEIGHT)
context.fill()

# Configuración de color y grosor de línea
context.set_source_rgb(0, 0, 0)  # Color negro
context.set_line_width(2)

# Función para dibujar un rectángulo con esquinas redondeadas
def draw_rounded_rectangle(ctx, x, y, width, height, radius):
    ctx.move_to(x + radius, y)
    ctx.line_to(x + width - radius, y)
    ctx.arc(x + width - radius, y + radius, radius, -0.5 * 3.14159, 0)
    ctx.line_to(x + width, y + height - radius)
    ctx.arc(x + width - radius, y + height - radius, radius, 0, 0.5 * 3.14159)
    ctx.line_to(x + radius, y + height)
    ctx.arc(x + radius, y + height - radius, radius, 0.5 * 3.14159, 3.14159)
    ctx.line_to(x, y + radius)
    ctx.arc(x + radius, y + radius, radius, 3.14159, 1.5 * 3.14159)
    ctx.close_path()
    ctx.stroke()

# Dibujar las secciones principales
sections = [
    {"x": 100, "y": 50, "width": 300, "height": 150, "title": "Data point", "subtitle": "A single value in a data set"},
    {"x": 100, "y": 250, "width": 300, "height": 300, "title": "Data set", "subtitle": "A single source of data"},
    {"x": 450, "y": 250, "width": 300, "height": 300, "title": "Data server", "subtitle": "A collection of databases"},
    {"x": 100, "y": 600, "width": 300, "height": 300, "title": "Database", "subtitle": "A collection of data sets"},
    {"x": 450, "y": 600, "width": 400, "height": 300, "title": "Data lake", "subtitle": "Less structured repository\nfor data to be converted\ninto curated data sets at a later point"}
]

for section in sections:
    # Dibujar rectángulo con esquinas redondeadas
    draw_rounded_rectangle(context, section["x"], section["y"], section["width"], section["height"], 20)

    # Dibujar texto de título
    context.move_to(section["x"] + 15, section["y"] + 40)
    context.show_text(section["title"])

    # Dibujar texto de subtítulo
    context.set_font_size(18)
    context.move_to(section["x"] + 15, section["y"] + 80)
    for line in section["subtitle"].split("\n"):
        context.show_text(line)
        context.move_to(section["x"] + 15, context.get_current_point()[1] + 25)
    context.set_font_size(24)

# Guardar la imagen
output_filename = "diagram_drawn_exact.png"
surface.write_to_png(output_filename)

# Mostrar la imagen usando Pillow
img = Image.open(output_filename)
img.show()