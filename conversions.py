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
    elif char == ".":
        draw_period(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == ',':
        draw_comma(canvas, x, y, size, line_color)
        x += size * 0.7
    elif char == ';':
        draw_semicolon(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == ':':
        draw_colon(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == '-':
        draw_dash(canvas, x, y, size, line_color)
        x += size
    elif char == '?':
        draw_question_mark(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == '!':
        draw_exclamation_mark(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == '‽':
        draw_interrobang(canvas, x, y, size, line_color)
        x += size * 0.6
    elif char == "'":
        draw_apostrophe(canvas, x, y, size, line_color)
        x += size * 0.3
    elif char == '"':
        draw_quote_mark(canvas, x, y, size, line_color)
        x += size * 0.5
    elif char == '...':
        draw_ellipsis(canvas, x, y, size, line_color)
        x += size * 1.5
    elif char == '(':
        draw_open_bracket(canvas, x, y, size, line_color)
        x += size
    elif char == ')':
        draw_close_bracket(canvas, x, y, size, line_color)
        x += size
    elif char == '[':
        draw_open_square_bracket(canvas, x, y, size, line_color)
        x += size
    elif char == ']':
        draw_close_square_bracket(canvas, x, y, size, line_color)
        x += size
    elif char == '/':
        draw_forward_slash(canvas, x, y, size, line_color)
        x += size * 1.5
    elif char == '&':
        draw_ampersand(canvas, x, y, size, line_color)
        x += size * 0.5
    else:
        prev_consonant_type = None

    return x, prev_consonant_type


