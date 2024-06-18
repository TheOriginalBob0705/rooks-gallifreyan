import tkinter as tk
import conversions


class ShapeRenderer:
    def __init__(self, master):
        self.master = master
        self.master.title("Rooks Gallifreyan")

        # Create entry widget
        self.text_entry = tk.Entry(master)
        self.text_entry.pack(fill=tk.X, padx=10, pady=10)
        self.text_entry.bind("<KeyRelease>", self.on_text_change)

        # Create size control widget
        self.size_scale = tk.Scale(master, from_=10, to=100, orient=tk.HORIZONTAL,
                                   command=self.on_size_change)
        self.size_scale.pack(padx=1)

        # Create canvas
        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.prev_text = ""
        self.x = 10  # Initial x position
        self.y = 50  # Fixed y position
        self.size = 30  # Initial size

    def on_text_change(self, event):
        current_text = self.text_entry.get()

        if current_text != self.prev_text:
            new_char = current_text[len(self.prev_text):]
            self.x = conversions.render_shape(self.canvas, new_char, self.x, self.y)
            self.prev_text = current_text

    def on_size_change(self, value):
        self.size = int(value)
        self.redraw_shapes()

    def redraw_shapes(self):
        self.canvas.delete("all")
        self.x = 10
        self.y = 50
        self.prev_text = ""
        for char in self.text_entry.get():
            self.x = conversions.render_shape(self.canvas, char, self.x, self.y, size=self.size)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    app = ShapeRenderer(root)
    root.mainloop()
