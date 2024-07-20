import rendering


def render_shape(canvas, char, x, y, size=30):
    char = char.lower()
    if char in 'bcdfghjklmnpqrstvwxyz':
        rendering.draw_consonant(canvas, char, x, y, size)
    elif char in 'aeiou':
        rendering.draw_vowel(canvas, char, x, y, size)
    return x + size * 1.25  # Update x position for next shape with spacing
