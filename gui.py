import tkinter as tk
from conversions import render_shape, double_consonants


class ShapeRenderer:
    def __init__(self, master):
        self.master = master
        self.master.title("Rooks Gallifreyan")

        self.text_entry = tk.Entry(master)
        self.text_entry.pack(fill=tk.X, padx=10, pady=10)
        self.text_entry.bind("<KeyRelease>", self.on_text_change)

        self.size_scale = tk.Scale(master, from_=10, to=100, orient=tk.HORIZONTAL, command=self.on_size_change)
        self.size_scale.pack(padx=1)
        self.size_scale.set(30)

        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.prev_text = ""
        self.size = 30
        self.line_height = self.size * 1.5
        self.top_margin = self.size * 1.75
        self.canvas_width = self.canvas.winfo_width()
        self.prev_consonant_type = None

    def on_canvas_resize(self, event):
        self.canvas_width = event.width
        self.redraw_shapes()

    def on_text_change(self, event):
        current_text = self.text_entry.get()
        if current_text != self.prev_text:
            self.redraw_shapes()
        self.prev_text = current_text

    def on_size_change(self, value):
        self.size = int(value)
        self.line_height = self.size * 1.5
        self.top_margin = self.size * 1.75
        self.redraw_shapes()

    def redraw_shapes(self):
        self.canvas.delete("all")
        x = 10
        y = self.top_margin
        text = self.text_entry.get().lower()
        i = 0
        prev_char = None
        self.prev_consonant_type = None

        while i < len(text):
            if x + self.size * 1.25 > self.canvas_width:
                x = 10
                y += self.line_height * 2

            if i < len(text) - 1 and text[i:i+2] in double_consonants:
                char = text[i:i+2]
                i += 2
            else:
                char = text[i]
                i += 1

            if char == ' ':
                x += self.size
                prev_char = None
                self.prev_consonant_type = None
            else:
                x, self.prev_consonant_type = render_shape(self.canvas, char, x, y, self.size, prev_char, self.prev_consonant_type)
                prev_char = char


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x800")
    app = ShapeRenderer(root)
    root.mainloop()
