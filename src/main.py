import kivent_core
import kivent_cymunk
import kivent_particles

from kivy.app import App
from kivy.uix.label import Label

class KiventApp(App):
    def build(self):
        return Label(text='it works!')


if __name__ == '__main__':
    KiventApp().run()
