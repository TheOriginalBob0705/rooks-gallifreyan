import rendering


def render_shape(canvas, char, x, y, size=30):
    if char.lower() == 'b':
        rendering.draw_cut_circle(canvas, x, y, size)
    elif char.lower() == 'j':
        rendering.draw_floating_circle(canvas, x, y, size)
    elif char.lower() == 't':
        rendering.draw_semicircle(canvas, x, y, size)

    return x + size * 1.25  # Update x position for next shape with spacing
