"""
    Author: Matthias Steinwendner
    Created: 2018.12.20
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty

from kivy.core.window import Window

# Set the window size
Window.size = 350, 450
# Set the window position
Window.left = 800
Window.top = 250

class CalcGridLayout(GridLayout):
    def input(self, entry_string):
        pass

    def calculate(self, calculation):
        """
        Evaluates a given String and displaying
        it on the Calculators TextInput. Flags are set
        according to whether or not the evaluation
        finished without errors.

        :param calculation: String to be evaluated
        """
        if calculation:
            try:
                calculation = calculation.replace("^", "**")

                # Calculation completed, set result flag
                self.display.text = str(eval(calculation))
                app.res_flag = True
            except (SyntaxError, NameError, Exception):
                # Calculation aborted, set error flag
                self.display.text = "Error"
                app.clear_flag = True

    def append_input_string(self, input_string):
        """
        Tries to append the text value of a pressed button.
        When the result flag is set and a numerical button
        is pressed, clear the input field and start a new calculation.
        If an operator-button was pressed, continue the calculation.
        Having the Error flag set will also result in a new calculation.

        :param input_string: String representation of pressed button
        """
        if app.res_flag:
            app.res_flag = False
            if input_string.isdigit():
                self.display.text = input_string
            else:
                self.display.text += input_string
        elif app.clear_flag:
            self.display.text = input_string
            app.clear_flag = False
        else:
            self.display.text += input_string


class CalculatorApp(App):
    clear_flag = BooleanProperty(False)
    res_flag = BooleanProperty(False)

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
