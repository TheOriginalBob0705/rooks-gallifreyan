import tkinter

CONSONANT_TYPES = {
    'cut_circle': 'cut_circle',
    'semicircle': 'semicircle',
    'combined_circle': 'combined_circle',
    'floating_circle': 'floating_circle',
    'default': 'default'
}


def draw_wordline(canvas, x, y, size):
    canvas.create_line(x - size * 0.25, y, x, y, fill="black", width=2)
    canvas.create_line(x + size, y, x + size * 1.25, y, fill="black", width=2)


def draw_circle(canvas, x, y, size):
    canvas.create_oval(x, y, x + size, y + size, outline="black", width=2)


def draw_consonant(canvas, char, x, y, size):
    base_char, consonant_type = {
        'b': (draw_cut_circle, CONSONANT_TYPES['cut_circle']),
        'c': (draw_c, CONSONANT_TYPES['floating_circle']),
        'd': (draw_d, CONSONANT_TYPES['cut_circle']),
        'f': (draw_f, CONSONANT_TYPES['cut_circle']),
        'g': (draw_g, CONSONANT_TYPES['cut_circle']),
        'h': (draw_h, CONSONANT_TYPES['cut_circle']),
        'j': (draw_floating_circle, CONSONANT_TYPES['floating_circle']),
        'k': (draw_k, CONSONANT_TYPES['floating_circle']),
        'l': (draw_l, CONSONANT_TYPES['floating_circle']),
        'm': (draw_m, CONSONANT_TYPES['floating_circle']),
        'n': (draw_n, CONSONANT_TYPES['floating_circle']),
        'p': (draw_p, CONSONANT_TYPES['floating_circle']),
        'q': (draw_q, CONSONANT_TYPES['combined_circle']),
        'r': (draw_r, CONSONANT_TYPES['semicircle']),
        's': (draw_s, CONSONANT_TYPES['semicircle']),
        't': (draw_semicircle, CONSONANT_TYPES['semicircle']),
        'v': (draw_v, CONSONANT_TYPES['semicircle']),
        'w': (draw_w, CONSONANT_TYPES['semicircle']),
        'x': (draw_x, CONSONANT_TYPES['combined_circle']),
        'y': (draw_y, CONSONANT_TYPES['combined_circle']),
        'z': (draw_z, CONSONANT_TYPES['combined_circle']),
        'ch': (draw_ch, CONSONANT_TYPES['cut_circle']),
        'sh': (draw_sh, CONSONANT_TYPES['semicircle']),
        'th': (draw_combined_circle, CONSONANT_TYPES['combined_circle']),
        'ng': (draw_ng, CONSONANT_TYPES['combined_circle']),
        'ph': (draw_ph, CONSONANT_TYPES['floating_circle']),
        'wh': (draw_wh, CONSONANT_TYPES['semicircle']),
        'nt': (draw_nt, CONSONANT_TYPES['semicircle']),
        'nd': (draw_nd, CONSONANT_TYPES['cut_circle']),
        'qu': (draw_qu, CONSONANT_TYPES['combined_circle']),
        'gh': (draw_gh, CONSONANT_TYPES['combined_circle'])
    }.get(char, (draw_circle, CONSONANT_TYPES['default']))

    base_char(canvas, x, y, size)
    draw_wordline(canvas, x, y, size)
    return consonant_type


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
    canvas.create_line(x, y, x + size, y, fill="black", width=2)


def draw_standalone_vowel(canvas, char, x, y, size, consonant_type=None):
    draw_vowel(canvas, char, x, y, size * 0.3, consonant_type)  # Vowels are 30% size
    draw_line_under_vowel(canvas, x, y, size)


def draw_attached_vowel(canvas, char, x, y, size, consonant_type):
    draw_vowel(canvas, char, x, y, size * 0.3, consonant_type, attached=True)  # Vowels are 30% size


def draw_line_under_vowel(canvas, x, y, size):
    canvas.create_line(x - size * 0.25, y, x + size * 0.45, y, fill="black", width=2)


def draw_vowel(canvas, char, x, y, size, consonant_type, attached=False):
    if char == 'a':
        draw_triangle_a(canvas, x, y, size, consonant_type, attached)
    elif char == 'e':
        draw_triangle_e(canvas, x, y, size, consonant_type, attached)
    elif char == 'i':
        draw_triangle_i(canvas, x, y, size, consonant_type, attached)
    elif char == 'o':
        draw_triangle_o(canvas, x, y, size, consonant_type, attached)
    elif char == 'u':
        draw_triangle_u(canvas, x, y, size, consonant_type, attached)


def draw_triangle_a(canvas, x, y, size, consonant_type, attached):
    if attached:
        x += size * 1.15
        if consonant_type == CONSONANT_TYPES['cut_circle']:
            y -= size * 0.75
        elif consonant_type == CONSONANT_TYPES['floating_circle']:
            y -= size * 2
        elif consonant_type == CONSONANT_TYPES['combined_circle']:
            y -= size * 0.3
        elif consonant_type == CONSONANT_TYPES['semicircle']:
            y -= size * 0.3
    elif not attached:
        y -= size * 0.3

    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")


def draw_triangle_e(canvas, x, y, size, consonant_type, attached):
    if attached:
        x += size * 1.15
        if consonant_type == CONSONANT_TYPES['cut_circle']:
            y -= size * 0.75
        elif consonant_type == CONSONANT_TYPES['floating_circle']:
            y -= size * 2
        elif consonant_type == CONSONANT_TYPES['combined_circle']:
            y -= size * 0.3
        elif consonant_type == CONSONANT_TYPES['semicircle']:
            y -= size * 0.3
    elif not attached:
        y -= size * 0.3

    canvas.create_polygon(x, y - size, x + size, y - size, x + size / 2, y, outline="black", width=2, fill="")


def draw_triangle_i(canvas, x, y, size, consonant_type, attached):
    if attached:
        x += size * 1.15
        if consonant_type == CONSONANT_TYPES['cut_circle']:
            y -= size * 0.75
        elif consonant_type == CONSONANT_TYPES['floating_circle']:
            y -= size * 2
        elif consonant_type == CONSONANT_TYPES['combined_circle']:
            y -= size * 0.3
        elif consonant_type == CONSONANT_TYPES['semicircle']:
            y -= size * 0.3
    elif not attached:
        y -= size * 0.3

    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")
    canvas.create_line(x + size / 2, y - size * 2.75, x + size / 2, y - size, fill="black", width=2)


def draw_triangle_o(canvas, x, y, size, consonant_type, attached):
    if attached:
        x += size * 1.15
        if consonant_type == CONSONANT_TYPES['cut_circle']:
            y -= size * 2.4
        elif consonant_type == CONSONANT_TYPES['floating_circle']:
            y -= size * 3.75
        elif consonant_type == CONSONANT_TYPES['combined_circle']:
            y -= size * 1.25
        elif consonant_type == CONSONANT_TYPES['semicircle']:
            y -= size * 1.25
    elif not attached:
        y += size * 0.4

    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")


def draw_triangle_u(canvas, x, y, size, consonant_type, attached):
    if attached:
        x += size * 1.15
        if consonant_type == CONSONANT_TYPES['cut_circle']:
            y -= size * 0.75
        elif consonant_type == CONSONANT_TYPES['floating_circle']:
            y -= size * 2
        elif consonant_type == CONSONANT_TYPES['combined_circle']:
            y -= size * 0.3
        elif consonant_type == CONSONANT_TYPES['semicircle']:
            y -= size * 0.3
    elif not attached:
        y -= size * 0.3

    canvas.create_polygon(x, y, x + size, y, x + size / 2, y - size, outline="black", width=2, fill="")
    canvas.create_line(x + size / 2, y, x + size / 2, y - size * -1.75, fill="black", width=2)

