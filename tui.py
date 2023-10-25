from textual.app import App
from textual import on, log
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Input
from setup_screen import Setup
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

        def get_setup(data:tuple[str,str,str]):
            self.token, self.client_id, self.channel = data
            log(f"Token: {self.token}, Client ID: {self.client_id}, Channel: {self.channel}")
        
        self.push_screen("setup", get_setup)
        
    
if __name__ == "__main__":
    app = TCPTextual()
    app.run()
