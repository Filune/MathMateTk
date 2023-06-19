import sys
from tkinter import Button, Frame, Label


class MathMateTk:
    """A simple calculator application using Tkinter, Windows UI."""
    
    def __init__(self, master):
        """Initialize the MathMateTk calculator.
        
        Args:
            master (Tk): The root Tk instance.
        """
        
        self.supported_exponent_length = 58
        self.master = master
        frame = Frame(self.master)
        
        self.define_operation_buttons(frame)
        self.define_number_buttons(frame)
        self.draw_operation_buttons_on_screen(frame)
        self.draw_number_buttons_on_screen()
        self.assign_commands_to_special_buttons(frame)
        frame.pack()
    
    def define_operation_buttons(self, frame):
        """Define the operation buttons for the calculator."""
        self.plus = Button(frame, text="+", command=lambda text=str("+"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        self.minus = Button(frame, text="-", command=lambda text=str("-"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        self.multiply = Button(frame, text="*", command=lambda text=str("*"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        self.divide = Button(frame, text="/", command=lambda text=str("/"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        self.dot = Button(frame, text=".", command=lambda text=str("."): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        self.power_of = Button(frame, text="^", command=lambda text=str("**"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())

    def define_number_buttons(self, frame):
        """Define the number buttons for the calculator."""
        self.buttons = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.zero = Button(frame, text="0", command=lambda text=str("0"): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())
        for i in range(9):
            self.buttons[i] = Button(frame, text=i, command=lambda text=str(i+1): self.put_on_display(text), width=self.get_button_width(), height=self.get_button_height())

    
    def draw_operation_buttons_on_screen(self, frame):
        """Draw the operation buttons on the screen."""
        self.display = Label(frame, text="", wraplength=170, height=3)
        self.display.grid(row=0, columnspan=4, sticky="ew")
        self.display.config(bg="#EDEADE", fg="black")
        self.plus.grid(row=1, column=0, sticky="ew")
        self.minus.grid(row=1, column=1, sticky="ew")
        self.multiply.grid(row=1, column=2, sticky="ew")
        self.divide.grid(row=5, column=2, sticky="ew")
        self.dot.grid(row=5, column=1, sticky="ew")
        self.power_of.grid(row=1, column=3, sticky="ew")

    def draw_number_buttons_on_screen(self):
        """Draw the number buttons on the screen."""
        button_index = 0
        self.zero.grid(row=5, sticky="ew")
        for row in range(2, 5):
            for column in range(3):
                self.buttons[button_index].grid(row=row, column=column, sticky="ew")
                self.buttons[button_index].config(text=str(button_index + 1))
                button_index += 1
                
    def assign_commands_to_special_buttons(self, frame):
        """Assign commands to the special buttons."""
        self.equal = Button(frame, text="=", command=self.equal, width=self.get_button_width(), height=self.get_button_height())
        self.equal.grid(row=5, column=3, sticky="ew")
        
        self.clearAll = Button(frame, text="C", command=self.clearAll, width=self.get_button_width(), height=self.get_button_height())
        self.clearAll.grid(row=3, column=3, sticky="ew")
        
        self.delete = Button(frame, text="<", command=self.delete, width=self.get_button_width(), height=self.get_button_height())
        self.delete.grid(row=2, column=3, sticky="ew")
    
    def put_on_display(self, text):
        """Append the given text to the display."""
        current_text = self.display.cget("text")
    
        last_char = ""
        if current_text:
            last_char = current_text[-1]
            
            if current_text in ["Error", "", "Result > ∣∣10^" + str(self.supported_exponent_length) + "∣∣", "Division by Zero not allowed!", "Numbers are too big!"]:
                current_text = ""
            if len(current_text) > self.supported_exponent_length:
                self.display.config(text="Numbers are too big!")
                return
        
        
        if not current_text and (text == "*" or text == "/" or text == "+" or text == "**"):
            return
    
        if last_char in ["+", "*", "/", "**"] and text in ["+", "*", "/", "**"]:
            return
    
        self.display.config(text=current_text + text)
    
    def equal(self):
        """Perform the calculation and display the result."""
        current_text = self.display.cget("text")
        
        try:
            result = eval(current_text)
            if result > 10**self.supported_exponent_length or result < -(10**self.supported_exponent_length):
                self.display.config(text="Result > ∣∣10^" + str(self.supported_exponent_length) + "∣∣")
            else:
                self.display.config(text=str(result))
        except (SyntaxError, ValueError):
            self.display.config(text="Error")
        except (ZeroDivisionError):
            self.display.config(text="Division by Zero not allowed!")
        
    def delete(self):
        """Delete the last character from the display."""
        current_text = self.display.cget("text")
        
        if current_text in ["Error", "", "Result > ∣∣10^" + str(self.supported_exponent_length) + "∣∣", "Numbers are too big!"]:
            self.display.config(text="")
        else:
            self.display.config(text=current_text[:-1])
    
    def clearAll(self):
        """Clear the display."""
        self.display.config(text="")
        
    def get_button_width(self):
        """Get the button width based on the operating system."""
        if sys.platform.startswith('darwin'):
            return None
        else:
            return 5

    def get_button_height(self):
        """Get the button height based on the operating system."""
        if sys.platform.startswith('darwin'):
            return None
        else:
            return 1