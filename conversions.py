from rendering import *

double_consonants = {'ch', 'sh', 'th', 'ng', 'ph', 'wh', 'nt', 'nd', 'qu', 'gh'}


def is_consonant(char):
    return char in 'bcdfghjklmnpqrstvwxyz' or char in double_consonants


def render_shape(canvas, char, x, y, size=30, prev_char=None, prev_consonant_type=None, line_color="black"):
    if char in double_consonants:
        prev_consonant_type = draw_consonant(canvas, char, x, y, size, line_color)
        x += size * 1.25
    elif char in 'bcdfghjklmnpqrstvwxyz':
        prev_consonant_type = draw_consonant(canvas, char, x, y, size, line_color)
        x += size * 1.25
    elif char in 'aeiou':
        if prev_char and is_consonant(prev_char):
            x -= size * 1.25
            draw_attached_vowel(canvas, char, x, y, size, line_color, prev_consonant_type)
            x += size * 1.25
        else:
            draw_standalone_vowel(canvas, char, x, y, size, line_color)
            x += size * 0.4
        prev_consonant_type = None
    elif char == '?!':
        draw_interrobang(canvas, x, y, size, line_color)
        x += size * 0.6
        prev_consonant_type = None
    elif char == '...':
        draw_ellipsis(canvas, x, y, size, line_color)
        x += size * 1.5
        prev_consonant_type = None
    elif char in '.,;:-?!\'"()[]/&':
        line_size = draw_punctuation(canvas, char, x, y, size, line_color)
        x += size * line_size
        prev_consonant_type = None
    else:
        prev_consonant_type = None

    return x, prev_consonant_type


