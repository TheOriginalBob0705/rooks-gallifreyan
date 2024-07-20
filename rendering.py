import tkinter


def draw_wordline(canvas, x, y, size):
    canvas.create_line(x - size * 0.25, y, x, y, fill="black", width=2)
    canvas.create_line(x + size, y, x + size * 1.25, y, fill="black", width=2)


def draw_circle(canvas, x, y, size):
    canvas.create_oval(x, y, x + size, y + size, outline="black", width=2)


def draw_consonant(canvas, char, x, y, size):
    base_char = {
        'b': draw_cut_circle,
        'c': draw_c,
        'd': draw_d,
        'f': draw_f,
        'g': draw_g,
        'h': draw_h,
        'j': draw_floating_circle,
        'k': draw_k,
        'l': draw_l,
        'm': draw_m,
        'n': draw_n,
        'p': draw_p,
        'q': draw_q,
        'r': draw_r,
        's': draw_s,
        't': draw_semicircle,
        'v': draw_v,
        'w': draw_w,
        'x': draw_x,
        'y': draw_y,
        'z': draw_z,
        'ch': draw_ch,
        'sh': draw_sh,
        'th': draw_combined_circle,
        'ng': draw_ng,
        'ph': draw_ph,
        'wh': draw_wh,
        'nt': draw_nt,
        'nd': draw_nd,
        'qu': draw_qu,
        'gh': draw_gh
    }.get(char, draw_circle)

    base_char(canvas, x, y, size)
    draw_wordline(canvas, x, y, size)


def draw_vowel(canvas, char, x, y, size):
    if char == 'a':
        draw_triangle_a(canvas, x, y, size)
    elif char == 'e':
        draw_triangle_e(canvas, x, y, size)
    elif char == 'i':
        draw_triangle_i(canvas, x, y, size)
    elif char == 'o':
        draw_triangle_o(canvas, x, y, size, -10)
    elif char == 'u':
        draw_triangle_u(canvas, x, y, size)


def draw_c(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_four_dots(canvas, x, y, size, size * 0.95)


def draw_d(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_three_dots(canvas, x, y, size, size * 0.55)


def draw_f(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_triple_line(canvas, x, y, size, size * 0.55)


def draw_g(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_single_line(canvas, x, y, size, size * 0.55)


def draw_h(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_double_line(canvas, x, y, size, size * 0.55)


def draw_k(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_two_dots(canvas, x, y, size, size * 0.95)


def draw_l(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_three_dots(canvas, x, y, size, size * 0.95)


def draw_m(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_triple_line(canvas, x, y, size, size * 0.95)


def draw_n(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_single_line(canvas, x, y, size, size * 0.95)


def draw_p(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_double_line(canvas, x, y, size, size * 0.95)


def draw_q(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_four_dots(canvas, x, y, size, size * 0.2)


def draw_r(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_three_dots(canvas, x, y, size, size * 0.2)


def draw_s(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_triple_line(canvas, x, y, size, size * 0.2)


def draw_v(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_single_line(canvas, x, y, size, size * 0.2)


def draw_w(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_double_line(canvas, x, y, size, size * 0.2)


def draw_x(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_double_line(canvas, x, y, size, size * 0.2)


def draw_y(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_three_dots(canvas, x, y, size, size * 0.2)


def draw_z(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_four_dots(canvas, x, y, size, size * 0.2)


def draw_ch(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_two_dots(canvas, x, y, size, size * 0.55)


def draw_sh(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_two_dots(canvas, x, y, size, size * 0.2)


def draw_ng(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_triple_line(canvas, x, y, size, size * 0.2)


def draw_ph(canvas, x, y, size):
    draw_floating_circle(canvas, x, y, size)
    draw_one_dot(canvas, x, y, size, size * 0.95)


def draw_wh(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_one_dot(canvas, x, y, size, size * 0.2)


def draw_nt(canvas, x, y, size):
    draw_semicircle(canvas, x, y, size)
    draw_four_dots(canvas, x, y, size, size * 0.2)


def draw_nd(canvas, x, y, size):
    draw_cut_circle(canvas, x, y, size)
    draw_four_dots(canvas, x, y, size, size * 0.55)


def draw_qu(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_single_line(canvas, x, y, size, size * 0.2)


def draw_gh(canvas, x, y, size):
    draw_combined_circle(canvas, x, y, size)
    draw_one_dot(canvas, x, y, size, size * 0.2)


def draw_one_dot(canvas, x, y, size, base_height):
    # The base height is used to move the modifier symbols up or down relative to which consonant they are attached to
    canvas.create_oval(x + size * 0.45, y - size * 0.4 - base_height, x + size * 0.55, y - size * 0.5 - base_height, fill="black")


def draw_two_dots(canvas, x, y, size, base_height):
    canvas.create_oval(x + size * 0.2, y - size * 0.35 - base_height, x + size * 0.3, y - size * 0.45 - base_height, fill="black")
    canvas.create_oval(x + size * 0.7, y - size * 0.35 - base_height, x + size * 0.8, y - size * 0.45 - base_height, fill="black")


def draw_three_dots(canvas, x, y, size, base_height):
    canvas.create_oval(x + size * 0, y - size * 0.2 - base_height, x + size * 0.1, y - size * 0.3 - base_height, fill="black")
    canvas.create_oval(x + size * 0.45, y - size * 0.4 - base_height, x + size * 0.55, y - size * 0.5 - base_height, fill="black")
    canvas.create_oval(x + size * 0.9, y - size * 0.2 - base_height, x + size, y - size * 0.3 - base_height, fill="black")


def draw_four_dots(canvas, x, y, size, base_height):
    canvas.create_oval(x + size * 0, y - size * 0.2 - base_height, x + size * 0.1, y - size * 0.3 - base_height, fill="black")
    canvas.create_oval(x + size * 0.2, y - size * 0.35 - base_height, x + size * 0.3, y - size * 0.45 - base_height, fill="black")
    canvas.create_oval(x + size * 0.7, y - size * 0.35 - base_height, x + size * 0.8, y - size * 0.45 - base_height, fill="black")
    canvas.create_oval(x + size * 0.9, y - size * 0.2 - base_height, x + size, y - size * 0.3 - base_height, fill="black")


def draw_single_line(canvas, x, y, size, base_height):
    canvas.create_line(x + size * 0.8, y - size * 0.2 - base_height, x + size * 1.2, y - size * 0.6 - base_height, fill="black", width=2)


def draw_double_line(canvas, x, y, size, base_height):
    # Second line starts at x 0.9 and y 0.1, but at the same angle (and shorter than the first line)
    canvas.create_line(x + size * 0.8, y - size * 0.2 - base_height, x + size * 1.2, y - size * 0.6 - base_height, fill="black", width=2)
    canvas.create_line(x + size * 0.9, y - size * 0.1 - base_height, x + size * 1.2, y - size * 0.4 - base_height, fill="black", width=2)


def draw_triple_line(canvas, x, y, size, base_height):
    canvas.create_line(x + size * 0.8, y - size * 0.2 - base_height, x + size * 1.2, y - size * 0.6 - base_height, fill="black", width=2)
    canvas.create_line(x + size * 0.9, y - size * 0.1 - base_height, x + size * 1.2, y - size * 0.4 - base_height, fill="black", width=2)
    canvas.create_line(x + size * 0.7, y - size * 0.28 - base_height, x + size * 0.97, y - size * 0.55 - base_height, fill="black", width=2)


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


def draw_triangle_a(canvas, x, y, size):
    # A hollow triangle pointing up
    size = size * 0.3
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")


def draw_triangle_e(canvas, x, y, size):
    # A hollow triangle pointing down
    size = size * 0.3
    canvas.create_polygon(x, y - size, x + size, y - size, x + size / 2, y, outline="black", width=2, fill="")


def draw_triangle_i(canvas, x, y, size):
    # A hollow triangle with a line coming straight up out of the top vertex
    size = size * 0.3
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")
    canvas.create_line(x + size / 2, y - size * 2, x + size / 2, y - size, fill="black", width=2)


def draw_triangle_o(canvas, x, y, size, height):
    # The base height value will ensure the triangle can be moved up or down in order to intersect with its attached consonant
    size = size * 0.3
    canvas.create_polygon(x, y - height, x + size, y - height, x + size / 2, y - size - height, outline="black", width=2, fill="")


def draw_triangle_u(canvas, x, y, size):
    # A hollow triangle with a line coming straight down out of the bottom face
    size = size * 0.3
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")
    canvas.create_line(x + size / 2, y, x + size / 2, y - size * -1.25, fill="black", width=2)
