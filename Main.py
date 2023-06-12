from tkinter import *

class Main:
    
    def __init__(self, master):
        frame = Frame(master)
        self.master = master
        
        master.title("MathMateTk")
        
        self.plus = Button(frame, text="+", command=lambda text=str("+"): self.put_on_display(text))
        self.minus = Button(frame, text="-", command=lambda text=str("-"): self.put_on_display(text))
        self.multiply = Button(frame, text="*", command=lambda text=str("*"): self.put_on_display(text))
        self.divide = Button(frame, text="/", command=lambda text=str("/"): self.put_on_display(text))
        self.dot = Button(frame, text=".", command=lambda text=str("."): self.put_on_display(text))
        self.power_of = Button(frame, text="^", command=lambda text=str("**"): self.put_on_display(text))
        
        self.buttons = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.zero = Button(frame, text="0", command=lambda text=str("0"): self.put_on_display(text))
        for i in range(9):
            self.buttons[i] = Button(frame, text=i, command=lambda text=str(i+1): self.put_on_display(text))
           
        self.display = Label(frame, text="")   
        
        frame.pack()
        self.display.grid(row=0, columnspan=4)
        self.plus.grid(row=1)
        self.minus.grid(row=1, column=1)
        self.multiply.grid(row=1, column=2)
        self.divide.grid(row=5, column=2)
        self.dot.grid(row=5, column=1)
        self.zero.grid(row=5)
        self.power_of.grid(row=1, column=3)

        button_index = 0
        for row in range(2, 5):
            for column in range(3):
                self.buttons[button_index].grid(row=row, column=column)
                self.buttons[button_index].config(text=str(button_index + 1))
                button_index += 1
        
        self.equal = Button(frame, text="=", command=self.equal)
        self.equal.grid(row=5, column=3)
        
        self.clearAll = Button(frame, text="C", command=self.clearAll)
        self.clearAll.grid(row=3, column=3)
        
        self.delete = Button(frame, text="<", command=self.delete)
        self.delete.grid(row=2, column=3, sticky=E)
        
    def put_on_display(self, text):
        current_text = self.display.cget("text")
    
        last_char = ""
        if current_text:
            last_char = current_text[-1]
            
            if current_text in ["Error", "", "Result > ∣∣10^19∣∣", "Division by Zero not allowed!", "Numbers are too big!"]:
                current_text = ""
            if len(current_text) > 19:
                self.display.config(text="Numbers are too big!")
                return
        
        
        if not current_text and (text == "*" or text == "/" or text == "+" or text == "**"):
            return
    
        if last_char in ["+", "*", "/", "**"] and text in ["+", "*", "/", "**"]:
            return
    
        self.display.config(text=current_text + text)
    
    def equal(self):
        current_text = self.display.cget("text")
        
        try:
            result = eval(current_text)
            if result > 10**19 or result < -(10**19):
                self.display.config(text="Result > ∣∣10^19∣∣")
            else:
                self.display.config(text=str(result))
        except (SyntaxError, ValueError):
            self.display.config(text="Error")
        except (ZeroDivisionError):
            self.display.config(text="Division by Zero not allowed!")
        
    def delete(self):
        current_text = self.display.cget("text")
        
        if current_text in ["Error", "", "Result > ∣∣10^19∣∣", "Division by Zero not allowed!", "Numbers are too big!"]:
            self.display.config(text="")
        else:
            self.display.config(text=current_text[:-1])
    
    def clearAll(self):
        self.display.config(text="")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.update()

root = Tk()
root.geometry("200x170")
center_window(root)
calc = Main(root)
root.mainloop()