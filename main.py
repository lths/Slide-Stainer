from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.graphics import Line

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
	def test_Callback(self):
		print "test1"
		
		
	button_val = "OPEN"
	



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
			orientation: 'horizontal'
			Label:
				text: 'Enable First Stage: '
				font_size: 12
			ToggleButton:
				id: first_Stage_Enable
		BoxLayout:
		
			BoxLayout:
				orientation: 'horizontal'
				Label:
					text: 'Heating Stage: '
					font_size: 12
				ToggleButton:
					id: first_Stage_Type
					on_release: app.root.test_Callback()
					text: 
			BoxLayout:
				orientation: 'horizontal'
				Label:
					text: 'Liquid Stage: '
					font_size: 12
				ToggleButton:
					id: first_Stage_Type
					on_release: app.root.test_Callback()
					text: 
		BoxLayout:
			BoxLayout:
				Label:
					text: 'Stage 1 Time (seconds)'
				TextInput:
					id: stage_1_time
			BoxLayout:
				Label:
					text: 'Stage 1 Temperature (C)'
				TextInput:

		BoxLayout:
			orientation: 'horizontal'
			ToggleButton:
				text: 'Liquid Feed 1: '
				font_size: 12
			ToggleButton:
				font_size: 12
				on_release: app.root.test_Callback()
				text: 'Liquid Feed 2: '
			ToggleButton:
				text: 'Liquid Feed 3: '
				font_size: 12
			ToggleButton:
				font_size: 12
				on_release: app.root.test_Callback()
				text: 'Liquid Feed 4:'
			ToggleButton:
				font_size: 12
				on_release: app.root.test_Callback()
				text: 'Liquid Feed 5: '			
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: '........................'
				font_size: 10
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
<heating_Param>
	label_widget: heating_parameters
	BoxLayout:
		Button:
			text: 'this is heating.'
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget
	

ScreenManagerApp().run()