from textual import log
from textual.app import App
from textual.widgets import Footer, Header, Static, Button
from textual.containers import Grid, Container, Center 

from setup_screen import Setup
from config_screen import Config

class TCPTextual(App):
    token = ""
    client_id = ""
    channel = ""

    CSS_PATH = "tcptextual.css"

    def compose(self):
        yield Header(show_clock=True)
        with Container(id="homescreen"):
            yield Center(Button("1 Click Setup (Recommended)", id="setup_btn", variant="success"))

            with Container(id="individual_steps"):
                is_label = Static("Individual Steps", id="is_label")
                is_label.border_subtitle = "Advanced Users Only"
                yield Center(is_label)
                with Container(id="btn_container"):
                    yield Button("Bot Setup", id="bot_setup")
                    yield Button("Command & Key Config", id="bot_key_config")
                    yield Button("Run Twitch Chat Plays", id="run")
            yield Center(Static("Support me by buying me hot chocolate or giving me a job :P"))
        # yield Footer()

    def on_mount(self) -> None:
        self.title = "Twitch Chat Plays"
        self.sub_title="Created by AKK"
        self.install_screen(Setup(), "setup")
        self.install_screen(Config(), "config")

        def get_setup(data:tuple[str,str,str]):
            self.token, self.client_id, self.channel = data
            log(f"Token: {self.token}, Client ID: {self.client_id}, Channel: {self.channel}")
            self.push_screen("config", get_config)
        
        def get_config(data:tuple[str,str]):
            self.filename, self.folder = data
            log(f"Token: {self.filename}, Client ID: {self.folder}")

        # self.push_screen("setup", get_setup)
        
    
if __name__ == "__main__":
    app = TCPTextual()
    app.run()
