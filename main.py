from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class FirstStage(Screen):
    pass

class SecondStage(Screen):
    pass

class ThirdStage(Screen):
    pass

class FourthStage(Screen):
    pass
	
class FifthStage(Screen):
    pass
	
class SixthStage(Screen):
    pass

class RunStage(Screen):
    pass

class MyScreenManager(ScreenManager):
    def new_color_screen(self):
        name = str(time.time())
        s = ColorScreen(name=name,
                         color=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name
	first_Stage_Enable = 1
	
#	def first_En_State(self):
#		if first_Stage_Enable == 0:
#			first_Stage_Enable = 1
#			return "Enabled"
#		else:
#			first_Stage_Enable = 0
#			return "Disabled"




#####################################
#UI 
#####################################


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstStage:
    SecondStage:
	ThirdStage:
	FourthStage:
	FifthStage:
	SixthStage:
	RunStage:
	
<FirstStage>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
			Label:

				text: 'Enable First Stage: '
				font_size: 10
			ToggleButton:
				id: first_Stage_Enable

        Button:
			font_size: 10
            text: ' %s' % first_Stage_Enable.state
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: '.'
				font_size: 1
			Button:
				text: "goop"
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<SecondStage>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<ThirdStage>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Third screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<FourthStage>:
    name: 'fourth'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'fourth screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<FifthStage>:
    name: 'fifth'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Fifth screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto fourth screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<SixthStage>:
    name: 'sixth'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Sixth screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto run screen'
                font_size: 10
                on_release: app.root.current = 'runstage'
<RunStage>:
    name: 'runstage'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'run screen!'
            font_size: 30

        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 10
                on_release: app.root.current = 'first'
            Button:
                text: 'goto second screen'
                font_size: 10
                on_release: app.root.current = 'second'
            Button:
                text: 'goto third screen'
                font_size: 10
                on_release: app.root.current = 'third'
            Button:
                text: 'goto fourth screen'
                font_size: 10
                on_release: app.root.current = 'fourth'
            Button:
                text: 'goto fifth screen'
                font_size: 10
                on_release: app.root.current = 'fifth'
            Button:
                text: 'goto sixth screen'
                font_size: 10
                on_release: app.root.current = 'sixth'
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
