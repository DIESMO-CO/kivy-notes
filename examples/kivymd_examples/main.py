import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivymd.app import MDApp

Builder.load_file('main.kv')


class MyLayout(Widget):
    """Widget"""
    pass


# Kivy.kv files look at name of class (exclude 'App')
class Awesome(MDApp):
    """Root Application"""
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return MyLayout()

if __name__ == '__main__':
    Awesome().run()
