import tkinter

def draw_wordline(canvas, x, y, size):
    canvas.create_line(x - size * 0.25, y, x, y, fill="black", width=2)
    canvas.create_line(x + size, y, x + size * 1.25, y, fill="black", width=2)

def draw_circle(canvas, x, y, size):
    canvas.create_oval(x, y, x + size, y + size, outline="black", width=2)

def draw_consonant(canvas, char, x, y, size):
    base_char = {
        'b': draw_cut_circle,
        'd': draw_cut_circle,
        'f': draw_cut_circle,
        'g': draw_cut_circle,
        'h': draw_cut_circle,
        'j': draw_floating_circle,
        'k': draw_floating_circle,
        'l': draw_floating_circle,
        'm': draw_floating_circle,
        'n': draw_floating_circle,
        'p': draw_floating_circle,
        'r': draw_floating_circle,
        's': draw_floating_circle,
        't': draw_semicircle,
        'v': draw_semicircle,
        'w': draw_semicircle,
        'y': draw_semicircle,
        'z': draw_semicircle,
        'ch': draw_combined_circle,
        'sh': draw_combined_circle,
        'th': draw_combined_circle,
        'ng': draw_combined_circle,
        'ph': draw_combined_circle,
        'wh': draw_combined_circle,
        'nt': draw_combined_circle,
        'nd': draw_combined_circle,
        'qu': draw_combined_circle
    }.get(char, draw_circle)

    base_char(canvas, x, y, size)
    draw_wordline(canvas, x, y, size)

def draw_vowel(canvas, char, x, y, size):
    if char == 'a':
        draw_triangle_up(canvas, x, y, size)
    elif char == 'e':
        draw_triangle_down(canvas, x, y, size)
    elif char == 'i':
        draw_triangle_left(canvas, x, y, size)
    elif char == 'o':
        draw_triangle_right(canvas, x, y, size)
    elif char == 'u':
        draw_triangle_pointing(canvas, x, y, size)

def draw_cut_circle(canvas, x, y, size):
    y_offset = size * 0.86
    canvas.create_arc(x, y - y_offset, x + size, y + size - y_offset, start=-45, extent=270, outline="black", width=2, style=tkinter.ARC)
    canvas.create_line(x - size * 0.25, y, x + size * 0.15, y, fill="black", width=2)
    canvas.create_line(x + size * 0.85, y, x + size * 1.25, y, fill="black", width=2)

def draw_floating_circle(canvas, x, y, size):
    y_offset = size * 1.25
    canvas.create_line(x, y, x + size, y, fill="black", width=2)
    canvas.create_oval(x, y - y_offset, x + size, y + size - y_offset, outline="black", width=2)
    draw_wordline(canvas, x, y, size)

def draw_semicircle(canvas, x, y, size):
    y_offset = size * 0.5
    canvas.create_arc(x, y - y_offset, x + size, y + size - y_offset, start=0, extent=180, outline="black", width=2, style=tkinter.ARC)
    draw_wordline(canvas, x, y, size)

def draw_combined_circle(canvas, x, y, size):
    canvas.create_oval(x, y - size // 2, x + size, y + size // 2, outline="black", width=2)

def draw_triangle_up(canvas, x, y, size):
    canvas.create_polygon(x, y, x + size / 2, y - size, x + size, y, outline="black", width=2)

def draw_triangle_down(canvas, x, y, size):
    canvas.create_polygon(x, y, x + size / 2, y + size, x + size, y, outline="black", width=2)

def draw_triangle_left(canvas, x, y, size):
    canvas.create_polygon(x, y, x - size, y + size / 2, x, y + size, outline="black", width=2)

def draw_triangle_right(canvas, x, y, size):
    canvas.create_polygon(x, y, x + size, y + size / 2, x, y + size, outline="black", width=2)

def draw_triangle_pointing(canvas, x, y, size):
    canvas.create_polygon(x, y, x + size / 2, y + size / 2, x + size, y, outline="black", width=2)
