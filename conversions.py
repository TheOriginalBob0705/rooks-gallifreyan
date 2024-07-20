import rendering

double_consonants = {
    'ch': 'ch',
    'sh': 'sh',
    'th': 'th',
    'ng': 'ng',
    'ph': 'ph',
    'wh': 'wh',
    'nt': 'nt',
    'nd': 'nd',
    'qu': 'qu',
    'gh': 'gh'
}

# Adding function to check if the previous character is a consonant
def is_consonant(char):
    return char in 'bcdfghjklmnpqrstvwxyz' or char in double_consonants

def render_shape(canvas, char, x, y, size=30, prev_char=None):
    char = char.lower()
    if char in double_consonants:
        rendering.draw_consonant(canvas, double_consonants[char], x, y, size)
    elif char in 'bcdfghjklmnpqrstvwxyz':
        rendering.draw_consonant(canvas, char, x, y, size)
    elif char in 'aeiou':
        if prev_char and is_consonant(prev_char):
            rendering.draw_attached_vowel(canvas, char, x, y, size)
        else:
            rendering.draw_standalone_vowel(canvas, char, x, y, size)
    return x + size * 1.25  # Update x position for next shape with spacing
