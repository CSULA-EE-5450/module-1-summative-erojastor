from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty

class TicTacToe(App):

    gameboard = ListProperty([ '' for i in range(9)])

    def build(self):

        return Builder.load_string("""

GridLayout:
    cols: 3
    spacing: 10
    
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
    
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
        
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
    
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X' 
        
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
    
    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'

    Button:
        text: 'Enter your sign here'
        size_hint_x: 10
        background_color: 1, .25, 1, 1
        font_size: 35
        on_press: self.text = 'X'
""")


if __name__ == '__main__':
    TicTacToe().run()
