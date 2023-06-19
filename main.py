import os
import sys
from tkinter import PhotoImage, Tk
from mathmatetkmac import MathMateTkMac
from mathmatetkwindows import MathMateTkWindows


def launch():
    """Launches the MathMateTk application."""
    script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(script_dir, 'images/calculator_icon.png')

    root = Tk()
    root.geometry("178x180")
    center_window(root)
    
    if sys.platform.startswith('darwin'):
        MathMateTkMac(root)
    else:
        MathMateTkWindows(root)

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
