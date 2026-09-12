import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class GuessingGame(App):

    def build(self):
        self.number = random.randint(1, 10)
        self.score = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="🎮 GUESS THE NUMBER",
            font_size=28
        )

        self.result = Label(
            text="Guess a number from 1 to 10!",
            font_size=20
        )

        self.input = TextInput(
            hint_text="Enter a number",
            input_filter="int",
            font_size=24,
            multiline=False
        )

        guess_button = Button(
            text="GUESS",
            font_size=22
        )
        guess_button.bind(on_press=self.guess)

        self.score_label = Label(
            text="Score: 0",
            font_size=20
        )

        restart_button = Button(
            text="RESTART",
            font_size=20
        )
        restart_button.bind(on_press=self.restart)

        layout.add_widget(title)
        layout.add_widget(self.result)
        layout.add_widget(self.input)
        layout.add_widget(guess_button)
        layout.add_widget(self.score_label)
        layout.add_widget(restart_button)

        return layout

    def guess(self, instance):
        if not self.input.text:
            self.result.text = "Enter a number!"
            return

        guess = int(self.input.text)

        if guess == self.number:
            self.score += 1
            self.result.text = "🎉 CORRECT!"
            self.score_label.text = "Score: " + str(self.score)
            self.number = random.randint(1, 10)
            self.input.text = ""

        elif guess < self.number:
            self.result.text = "Too low! ⬆️"

        else:
            self.result.text = "Too high! ⬇️"

    def restart(self, instance):
        self.number = random.randint(1, 10)
        self.score = 0
        self.result.text = "New game! 🎮"
        self.score_label.text = "Score: 0"
        self.input.text = ""


GuessingGame().run()