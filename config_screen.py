from textual import on
from textual.containers import VerticalScroll
from textual.screen import Screen
from config_generator import create_config, Controller_Config
from textual.widgets import Button,  Header, Static, Input, Label
class Config(Screen):
    def compose(self):
        yield Header(show_clock=True)
        with VerticalScroll(id="configs"):
            yield Path()
            yield Key_Config()
        yield Button("Add Key Config", id="add_key", variant="primary")
        yield Button("Generate", id="generate", variant="success")

    @on(Button.Pressed, "#add_key")
    def add_key(self):
        self.query_one("#configs").mount(Key_Config())

    @on(Button.Pressed, "#generate")
    def generate(self):
        controller_configs: Controller_Config = []
        folder = self.query_one(Path).query_one("#folder").value
        filename = self.query_one(Path).query_one("#filename").value
        configs = self.query(Key_Config)
        for config in configs:
            children = config.query(Input)
            for child in children:
                if child.id == "command_name":
                    command_name = child.value
                if child.id == "keys":
                    keys = child.value.split(",")
                if child.id == "duration":
                    duration = float(child.value)
                if child.id == "chance":
                    chance = float(child.value)
                if child.id == "cooldown":
                    cooldown = float(child.value)
            controller_configs.append(Controller_Config(command_name=command_name, keys=keys, duration=duration, cooldown=cooldown, chance=chance))
        create_config(controller_configs, filename, folder)
        self.dismiss((filename, folder))
class Path(Static):
    
    def compose(self):
        yield Label("Folder: (Default: config)")
        yield Input("config", id="folder")
        yield Label("Filename: (Default: test)")
        yield Input("test", id="filename")

class Key_Config(Static):

    def compose(self):
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
