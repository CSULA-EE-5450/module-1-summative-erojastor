"""
Don't wanna get sued or anything so was told to paste this if I downloaded the tune:

    Monkeys Spinning Monkeys Kevin MacLeod (incompetech.com)
    Licensed under Creative Commons: By Attribution 3.0 License
    http://creativecommons.org/licenses/by/3.0/
    Music promoted by https://www.chosic.com/


"""

import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import CoreLabel
from kivy.graphics import Color


class GameSetup(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_done, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas.before:
            Rectangle(source='Background.png', size=(1550, 800))
        with self.canvas:

            Player1xpos = random.randrange(0, Window.width - 25, 50)
            Player1ypos = random.randrange(0, Window.height - 25, 50)
            Player2xpos = random.randrange(0, Window.width - 25, 50)
            Player2ypos = random.randrange(0, Window.height - 25, 50)
            self.player1 = Rectangle(source='Sonic.png', pos=(Player1xpos, Player1ypos), size=(60, 60))
            self.player2 = Rectangle(source='Eggman.png', pos=(Player2xpos, Player2ypos), size=(60, 60))

        self.keysPressed = set()

    def _on_keyboard_done(self):
        self._keyboard.unbind(on_key_press=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        """

        :param keyboard: Keyboard that is emitting the event
        :param keycode: Numeric value that corresponds to a certain key on keyboard
        :param text: Textual representation of the key pressed
        :param modifiers: Modifier keys such as Ctrl, Alt, Shift, etc.

        """
        self.keysPressed.add(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        """
        :param keyboard: Keyboard that is emitting the event
        :param keycode: Numeric Value that corresponds to a certain key on board
        :return:
        """
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)


class Actions(GameSetup):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.sound = SoundLoader.load('start.mp3')
        self.sound.volume = 0.1
        self.sound.play()
        Clock.schedule_interval(self._player1_, 0)
        Clock.schedule_interval(self._player2_, 0)
        self._player1score_label = CoreLabel(text="Player 1 score: 0", font_size=40)
        self._player1score_label.refresh()
        self._player1score = 0

        self._player2score_label = CoreLabel(text="Player 2 score: 0", font_size=40)
        self._player2score_label.refresh()
        self._player2score = 0
        with self.canvas:
            Color(1, 0, .3)
            self._player1score_instruction = Rectangle(texture=self._player1score_label.texture, pos=(
                100, 750), size=self._player1score_label.texture.size)
            Color(0, 1, .6)
            self._player2score_instruction = Rectangle(texture=self._player2score_label.texture, pos=(
                1100, 750), size=self._player2score_label.texture.size)

    @property
    def player1_score(self):
        return self._player1score

    @player1_score.setter
    def player1_score(self, value):
        self._player1score = value
        self._player1score_label.text = f"Player 1 score: {self._player1score}"
        self._player1score_label.refresh()
        self._player1score_instruction.texture = self._player1score_label.texture
        self._player1score_instruction.size = self._player1score_label.texture.size

    @property
    def player2_score(self):
        return self._player2score

    @player2_score.setter
    def player2_score(self, value):
        self._player2score = value
        self._player2score_label.text = f"Player 2 score: {self._player2score}"
        self._player2score_label.refresh()
        self._player2score_instruction.texture = self._player2score_label.texture
        self._player2score_instruction.size = self._player2score_label.texture.size

    def _player1_(self, dt):
        """

        :param dt:delta-time, time since last frame
        :return: player position
        """
        player1xsize = self.player1.size[0]
        player1ysize = self.player1.size[1]
        player1xpos = self.player1.pos[0]
        player1ypos = self.player1.pos[1]

        step_size = 100 * dt

        if 'w' in self.keysPressed:
            player1ypos += step_size

        if 's' in self.keysPressed:
            player1ypos -= step_size

        if 'a' in self.keysPressed:
            player1xpos -= step_size

        if 'd' in self.keysPressed:
            player1xpos += step_size

        if 'a' in self.keysPressed and 'spacebar' in self.keysPressed:
            player1xpos -= step_size*5

        if 'w' in self.keysPressed and 'spacebar' in self.keysPressed:
            player1ypos += step_size*5

        if 's' in self.keysPressed and 'spacebar' in self.keysPressed:
            player1ypos -= step_size*5

        if 'd' in self.keysPressed and 'spacebar' in self.keysPressed:
            player1xpos += step_size*5

        self.player1.pos = (player1xpos, player1ypos)

        if player1xpos <= -.5 * player1xsize or player1xpos >= Window.width - 0.5 * player1xsize or \
                player1ypos <= -.5 * player1ysize or player1ypos >= Window.height - 0.5 * player1ysize:
            popup = Popup(content=Label(text='Player 1 get back in the box!'), size_hint=(None, None),
                          size=(300, 300), auto_dismiss=False)
            popup.open()
            popup.dismiss()
            self.player1_score -= 2

        return self.player1.pos

    def _player2_(self, dt):
        """

        :param dt:delta-time, time since last frame
        :return: enemy position
        """
        player2xsize = self.player2.size[0]
        player2ysize = self.player2.size[1]
        player2xpos = self.player2.pos[0]
        player2ypos = self.player2.pos[1]

        step_size = 1000 * dt

        if 'up' in self.keysPressed:
            player2ypos += step_size

        if 'down' in self.keysPressed:
            player2ypos -= step_size

        if 'left' in self.keysPressed:
            player2xpos -= step_size

        if 'right' in self.keysPressed:
            player2xpos += step_size

        self.player2.pos = (player2xpos, player2ypos)
        if player2xpos <= -.5 * player2xsize or player2xpos >= Window.width - 0.5 * player2xsize or \
                player2ypos <= -.5 * player2ysize or player2ypos >= Window.height - 0.5 * player2ysize:
            popup = Popup(content=Label(text='Player 2 get back in the box!'), size_hint=(None, None),
                          size=(300, 300), auto_dismiss=False)
            popup.open()
            popup.dismiss()
            self.player2_score -= 4

        if self.catch((self.player1.pos, self.player1.size), (self.player2.pos, self.player2.size)):
            self.player1_score += 1.5
            self.player2_score -= 1
        else:
            self.player2_score += 0.5

        return self.player2.pos


class Catch(Actions):

    @staticmethod
    def catch(player1, player2):
        """
        :param player1: Player 1
        :param player2: Player 2
        :return: True if catch, False if no catch
        """
        P1x = player1[0][0]
        P1y = player1[0][1]
        P1w = player1[1][0]
        P1h = player1[1][1]
        P2x = player2[0][0]
        P2y = player2[0][1]
        P2w = player2[1][0]
        P2h = player2[1][1]

        if P1x < P2x + P2w and P1x + P1w > P2x and P1y < P2y + P2h and P1y + P1h > P2y:
            popup = Popup(content=Label(text='Caught you!'), size_hint=(None, None),
                          size=(300, 300), auto_dismiss=False)
            popup.open()
            popup.dismiss()

            return True
        else:

            return False


class Game(App):
    def build(self):
        return Catch()


if __name__ == '__main__':
    Game().run()
