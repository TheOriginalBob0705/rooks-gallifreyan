import tkinter as tk
from tkinter import filedialog, colorchooser
from conversions import render_shape, double_consonants


class ShapeRenderer:
    def __init__(self, master):
        self.master = master
        self.master.title("Rook's Gallifreyan")

        self.create_menu()
        self.create_toolbar()

        self.paned_window = tk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        self.text_entry = tk.Text(self.paned_window, wrap=tk.WORD)
        self.canvas = tk.Canvas(self.paned_window, bg="white")

        self.paned_window.add(self.text_entry)
        self.paned_window.add(self.canvas)

        self.paned_window.update_idletasks()
        self.paned_window.sash_place(0, self.master.winfo_width() // 3, 0)

        self.text_entry.bind("<KeyRelease>", self.on_text_change)
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.size = 30
        self.line_height = self.size * 1.5
        self.space_size = self.size
        self.line_color = "black"
        self.top_margin = self.size * 1.75
        self.canvas_width = self.canvas.winfo_width()
        self.prev_consonant_type = None

        self.master.geometry("1080x800")
        self.master.bind("<Control-s>", self.save_text_to_file)
        self.master.bind("<Control-S>", self.save_canvas_to_image)
        self.master.bind("<Control-o>", self.open_file)

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save Text", command=self.save_text_to_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save Image", command=self.save_canvas_to_image, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        menu_bar.add_cascade(label="View", menu=view_menu)

        self.master.config(menu=menu_bar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.master, bd=1, relief=tk.RAISED)

        line_color_button = tk.Button(toolbar, text="Line Colour", command=self.choose_line_color)
        line_color_button.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    def toggle_dark_mode(self):
        if self.canvas["bg"] == "white":
            self.canvas.config(bg="#222222")
            self.text_entry.config(bg="#222222", fg="white", insertbackground="white")
            self.line_color = "white"
        else:
            self.canvas.config(bg="white")
            self.text_entry.config(bg="white", fg="black", insertbackground="black")
            self.line_color = "black"
        self.redraw_shapes()

    def choose_line_color(self):
        color = colorchooser.askcolor(title="Choose Line Colour")
        if color:
            self.line_color = color[1]
            self.redraw_shapes()

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, text)
            self.redraw_shapes()

    def save_canvas_to_image(self, event=None):
        # TODO: FIGURE THIS SHIT OUT
        return None

    def save_text_to_file(self, event=None):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_entry.get())

    def on_canvas_resize(self, event):
        self.canvas_width = event.width
        self.redraw_shapes()

    def on_text_change(self, event):
        self.redraw_shapes()

    def on_size_change(self, value):
        self.size = int(value)
        self.line_height = self.size * 1.5
        self.space_size = self.size
        self.redraw_shapes()

    def on_line_height_change(self, value):
        self.line_height = int(value)
        self.redraw_shapes()

    def on_space_size_change(self, value):
        self.space_size = int(value)
        self.redraw_shapes()

    def redraw_shapes(self):
        self.canvas.delete("all")
        x = 10
        y = self.top_margin
        text = self.text_entry.get(1.0, tk.END).strip().lower()
        i = 0
        prev_char = None
        self.prev_consonant_type = None

        while i < len(text):
            if x + self.size * 1.25 > self.canvas_width:
                x = 10
                y += self.line_height * 2

            if text[i] == '\n':
                x = 10
                y += self.line_height * 2
                i += 1
                continue

            if i < len(text) - 2 and text[i:i + 3] == "...":
                char = "..."
                i += 3
            elif i < len(text) - 1 and text[i:i + 2] in double_consonants:
                char = text[i:i + 2]
                i += 2
            else:
                char = text[i]
                i += 1

            if char == ' ':
                x += self.space_size
                prev_char = None
                self.prev_consonant_type = None
            else:
                x, self.prev_consonant_type = render_shape(self.canvas, char, x, y, self.size, prev_char, self.prev_consonant_type, self.line_color)
                prev_char = char


if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeRenderer(root)
    root.mainloop()
