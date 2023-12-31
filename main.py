import os
import sys
from tkinter import PhotoImage, Tk
from mathmatetk import MathMateTk


def launch():
    """Launches the MathMateTk application."""
    script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(script_dir, 'images/calculator_icon.png')

    root = Tk()
    
    if sys.platform.startswith('darwin'):
        root.geometry("200x200")
    else:
        root.geometry("178x180")
    
    MathMateTk(root)
    center_window(root)
    root.title("MathMateTk")
    photo = PhotoImage(file=icon_path)
    root.iconphoto(False, photo)
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
