from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.utils import get_color_from_hex
class CanvasWidget(Widget):
    pass
class LogicGateSimulator(App):
    def build(self):
        CanvasWidget()
Config.set('graphics','width','960')
Config.set('graphics','height','540')
if __name__=='__main__':
    from kivy.core.window import Window
    Window.clearcolor=get_color_from_hex('#005566')
    LogicGateSimulator().run()
