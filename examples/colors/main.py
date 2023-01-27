import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder


Builder.load_file('whatever.kv')


class MyGridLayout(Widget):
    """Widget"""
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        """Function to execute when button pressed"""
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, you like {color}!"))
        print(f"Hello {name}, you like {pizza} pizza, you like {color}!")

        """Clear Text Boxes"""
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


# Kivy.kv files look at name of class (exclude 'App')
class Awesome(App):
    """Root Application"""
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Awesome().run()
