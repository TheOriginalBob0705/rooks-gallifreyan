import tkinter


def draw_wordline(canvas, x, y, size):
    canvas.create_line(x - size * 0.25, y, x, y, fill="black", width=2)
    canvas.create_line(x + size, y, x + size * 1.25, y, fill="black", width=2)


def draw_circle(canvas, x, y, size):
    canvas.create_oval(x, y, x + size, y + size, outline="black", width=2)


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
