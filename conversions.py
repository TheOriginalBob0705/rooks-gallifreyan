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
        x += size * 1.25
    elif char in 'bcdfghjklmnpqrstvwxyz':
        rendering.draw_consonant(canvas, char, x, y, size)
        x += size * 1.25
    elif char in 'aeiou':
        if prev_char and is_consonant(prev_char):
            # Backtrack x to attach vowel to the consonant
            x -= size * 1.25
            rendering.draw_attached_vowel(canvas, char, x, y, size)
            x += size * 1.25  # Move forward after drawing
        else:
            rendering.draw_standalone_vowel(canvas, char, x, y, size)
            x += size * 0.4  # Smaller spacing for standalone vowels
    return x  # Return updated x position
