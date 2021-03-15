# EE 5450 Summative Assignment 1
Building a game with Kivy and accessing through HTTP request

#Introduction:
In this assignment, we were given the task to create a game using a library of our choice.
I decided to use the Kivy library and implement a GUI. To play the game one must click run
on `MainGameTag` under the Tag folder, in which two players can play on the same computer using the WASD and 
arrow keys as well as spacebar.

Other game attempts were made such as `TicTacToeKivy_attempt1`, `Ghetto_Scrabble_attempt1` and `RegularTicTacToe`
but didn't have much success implementing them with Kivy.

This `MainGameTag` implements the Kivy library which is designed to make GUIs for devices such as smartphones. Certain 
functions from the Kivy library have to be called such as kivy.uix.label to use certain features like making a rectangle 
or being able to write/draw on a canvas. To use a physical keyboard for inputs one must also import a function named windows 
and can be called using the Window.request_keyboard command.

Couldn't get the `web_Tag` to run correctly. I would get a blank screen for my gui but if `MainGameTag` is ran directly 
the game will run fine. Press esc to exit the GUI window.

The game might not be the best, but I found it a bit entertaining. I hope you enjoy.