from textual.app import App
from textual.containers import VerticalScroll, Grid
from textual.screen import Screen
from config_generator import create_config, Controller_Config
from textual.widgets import Button,  Header, Static, Input, Label
class Config(Screen):
    def compose(self):
        yield Header(show_clock=True)
        with VerticalScroll(id="configs"):
            yield Path()
            yield Key_Config()
            yield Key_Config()
            yield Key_Config()
            yield Key_Config()
        yield Button("Add Key Config", id="add_key", variant="primary")
        yield Button("Generate", id="generate", variant="success")

    

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
        # with Grid(id="key_config"):
        yield Static("Command: ")
        yield Input(placeholder="Command Name", id="command_name")
        yield Static("Keys: ")
        yield Input(placeholder="Key(s) seperated by a comma", id="keys")
        yield Static("Duration: ")
        yield Input(placeholder="Duration (Seconds)", id="duration")
        yield Static("Chance: ")
        yield Input(placeholder="Chance (0-1, Optional)", id="chance")
        yield Static("Cooldown: ")
        yield Input(placeholder="Cooldown (Seconds, Optional)", id="cooldown")
