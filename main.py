from tkinter import Tk
from mathmatetk import MathMateTk


def launch():
    """Launches the MathMateTk application."""
    root = Tk()
    root.geometry("200x200")
    center_window(root)
    MathMateTk(root)
    root.title("MathMateTk")
    root.mainloop()
    
def center_window(window):
    """Centers the given window on the screen.

    Args:
        window (Tk): The window to be centered.
    """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.update()
    
if __name__ == "__main__":
    launch()
