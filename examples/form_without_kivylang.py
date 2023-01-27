import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    """Grid Layout"""
    def __init__(self, **kwargs):
        """"""
        super(MyGridLayout, self).__init__(**kwargs)

        """Set Columns"""
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        """Add Widgets"""
        self.top_grid.add_widget(
            Label(
                text="Name: ",
                size_hint_y=None,
                height=50
            )
        )
        self.name = TextInput(
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(
            Label(
                text="Favorite Pizza: "
            )
        )
        self.pizza = TextInput(
            multiline=False
        )
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(
            Label(
                text="Favorite Color: "
            )
        )
        self.color = TextInput(
            multiline=False
        )
        self.top_grid.add_widget(self.color)

        self.add_widget(self.top_grid)

        self.submit = Button(
            text="Submit",
            font_size=32,
            size_hint_y=None,
            height=50
        )
        """Button Bind"""
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        """Function to execute when button pressed"""
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, you like {color}!"))
        print(f"Hello {name}, you like {pizza} pizza, you like {color}!")

        """Clear Text Boxes"""
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    """Root Application"""
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
