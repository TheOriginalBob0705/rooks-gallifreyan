import tkinter as tk
from conversions import render_shape, double_consonants


class ShapeRenderer:
    def __init__(self, master):
        self.master = master
        self.master.title("Rooks Gallifreyan")

        # Create entry widget
        self.text_entry = tk.Entry(master)
        self.text_entry.pack(fill=tk.X, padx=10, pady=10)
        self.text_entry.bind("<KeyRelease>", self.redraw_shapes)

        # Create size control widget
        self.size_scale = tk.Scale(master, from_=10, to=100, orient=tk.HORIZONTAL, command=self.update_size)
        self.size_scale.pack(padx=1)
        self.size_scale.set(30)

        # Create canvas
        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas.bind("<Configure>", self.redraw_shapes)

        self.size = 30  # Initial size
        self.update_layout_params()

    def update_size(self, value):
        self.size = int(value)
        self.update_layout_params()
        self.redraw_shapes()

    def update_layout_params(self):
        self.line_height = self.size * 1.5
        self.top_margin = self.size * 1.75

    def redraw_shapes(self, event=None):
        self.canvas.delete("all")
        x, y = 10, self.top_margin
        text = self.text_entry.get().lower()
        prev_char, prev_consonant_type = None, None

        for i, char in enumerate(text):
            if x + self.size * 1.25 > self.canvas.winfo_width():
                x, y = 10, y + self.line_height * 2

            if char == ' ':
                x += self.size
                prev_char, prev_consonant_type = None, None
            else:
                if i < len(text) - 1 and text[i:i + 2] in double_consonants:
                    char = text[i:i + 2]
                x, prev_consonant_type = render_shape(self.canvas, char, x, y, self.size, prev_char, prev_consonant_type)
                prev_char = char


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x800")
    app = ShapeRenderer(root)
    root.mainloop()
