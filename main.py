import kivy
from kivy.app import App
from kivy.graphics import Rotate, Rectangle, Color
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (800, 480)
kivy.require("2.0.0")


class WheelTop(Widget):
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.angle = 0
        # self.wheelColor = (1, 1, 1, 1)

    def rotate(self, angle):
        self.canvas.clear()
        self.angle += angle

        with self.canvas:
            Rotate(origin=self.center, angle=self.angle)
            Color(rgba=self.wheelColor)
            Rectangle(pos=self.pos, size=self.size, source=self.source)


class HalfShaft(Widget):
    pass


class Engine(Widget):
    pass


class CentreDiff(Widget):
    pass


class RearDiff(Widget):
    pass


class CenterDiff(Widget):
    pass


class VehiclePlan(Widget):
    engine = ObjectProperty(None)
    wheel_front_left = ObjectProperty(None)
    wheel_front_right = ObjectProperty(None)

    def turn_wheel(self, dt):
        self.wheel_front_left.rotate(dt.angle)
        self.wheel_front_right.rotate(dt.angle)

    def update(self, dt):
        self.wheel_front_left.rotate()
        self.wheel_front_right.rotate()


class ControlPanel(BoxLayout):
    pass


class VehicleControl(BoxLayout):
    display = ObjectProperty(None)
    control_panel = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        BoxLayout.__init__(self, *args, **kwargs)

        # self.control_panel.button_1.bind(on_press=self.display.update)


class Launcher(BoxLayout):
    pass


class ControlScreen(BoxLayout):
    task = ObjectProperty(None)
    launcher = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        BoxLayout.__init__(self, *args, **kwargs)
        self.task.control_panel.button_1.angle = 15
        self.task.control_panel.button_1.bind(on_press=self.task.display.turn_wheel)
        self.task.control_panel.button_1.bind(on_release=self.task.display.turn_wheel)
        self.launcher.button_exit.bind(on_press=App.get_running_app().stop)

    def update(self, dt):
        self.task.display.update(dt)


class DiscomApp(App):

    def build(self):
        control_screen = ControlScreen()

        # Clock.schedule_interval(control_screen.update, 1.0 / 60.0)

        return control_screen


if __name__ == '__main__':
    DiscomApp().run()
