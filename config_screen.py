from textual.app import App
from textual.containers import ScrollableContainer
from textual.screen import Screen
from config_generator import create_config, Controller_Config
from textual.widgets import Button, Footer, Header, Static, Input, Label
class Config(Screen):
    def compose(self):
        yield Header(show_clock=True)
        with ScrollableContainer(id="configs"):
            yield Path()
            yield Key_Config()
            yield Key_Config()
            yield Key_Config()
            yield Key_Config()
        yield Button("Generate", id="generate")

class Path(Static):
    folder = "config"
    filename = "test"

    def compose(self):
        yield Label("Folder: (Default: config)")
        yield Input("config", id="folder")
        yield Label("Filename: (Default: test)")
        yield Input("test", id="filename")

class Key_Config(Static):

    def compose(self):
        yield Label("Command: ", id="command_label")
        yield Static("For Multi-Key commands, seperate each key with a comma.")
        yield Input(placeholder="Command Name", id="command_name")
        yield Input(placeholder="Keys", id="keys")
        yield Input(placeholder="Duration (Seconds)", id="duration")
        yield Input(placeholder="Chance (0-1,Optional)", id="chance")
        yield Input(placeholder="Cooldown (Seconds, Optional)", id="cooldown")
