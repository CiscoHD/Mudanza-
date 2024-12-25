from kivy.app import App
from kivy.uix.label import Label

class KivySaludo(App):
    
    def build(self):
        
        return Label(text="Hola Mundo")

KivySaludo().run()