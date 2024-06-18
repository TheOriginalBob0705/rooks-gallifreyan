import tkinter as tk


class ShapeRenderer:
    def __init__(self, master):
        self.master = master
        self.master.title("Shape Renderer")

        # Create entry widget
        self.text_entry = tk.Entry(master)
        self.text_entry.pack(fill=tk.X, padx=10, pady=10)
        self.text_entry.bind("<KeyRelease>", self.on_text_change)

        # Create canvas
        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.prev_text = ""
        self.x = 10  # Initial x position
        self.y = 50  # Fixed y position

    def on_text_change(self, event):
        current_text = self.text_entry.get()

        if current_text != self.prev_text:
            new_char = current_text[len(self.prev_text):]
            self.render_shape(new_char)
            self.prev_text = current_text

    def render_shape(self, char):
        size = 20  # Size of the shapes
        spacing = 30  # Spacing between shapes

        if char.lower() == 'c':
            self.canvas.create_oval(self.x, self.y, self.x + size, self.y + size, outline="black", width=2)
        elif char.lower() == 'l':
            self.canvas.create_line(self.x, self.y, self.x + size, self.y + size, fill="black", width=2)
        elif char.lower() == 'd':
            self.canvas.create_oval(self.x + size // 2 - 2, self.y + size // 2 - 2, self.x + size // 2 + 2,
                                    self.y + size // 2 + 2, outline="black", fill="black")

        # Update x position for the next shape
        self.x += spacing


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x200")
    app = ShapeRenderer(root)
    root.mainloop()
