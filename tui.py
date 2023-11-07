from textual import log
from textual.app import App
from textual.widgets import Footer, Header

from setup_screen import Setup
from config_screen import Config

class TCPTextual(App):
    token = ""
    client_id = ""
    channel = ""

    CSS_PATH = "tcptextual.css"

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

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

        self.push_screen("setup", get_setup)
        
    
if __name__ == "__main__":
    app = TCPTextual()
    app.run()
