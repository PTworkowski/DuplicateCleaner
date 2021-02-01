import kivy
from kivy.app import App
from kivy.uix.label import Label


class DuplicateCleaner(App):
    def build(self):
        return Label(text="DuplicateCleaner")


if __name__ == "__main__":
    DuplicateCleaner().run()  # sfdsd
