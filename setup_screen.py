from textual.app import App
from textual import on
from textual.screen import Screen
from textual.widgets import Static, Label, Input, Button, Footer, Header

class Setup(Screen):

    token = ""
    client_id = ""
    channel = ""

    def compose(self):
        yield Header(show_clock=True)
        yield Label("Access Token:")
        yield Input("", password=True, id="token")
        yield Label("Client ID:")
        yield Input("", password=True, id="client_id")
        yield Label("Channel Name:")
        yield Input("", id="channel")
        yield Button("Submit", variant="success", id="submit")
        yield Footer()
    @on(Button.Pressed, "#submit")
    def submit(self):
        self.token = self.query_one("#token").value 
        self.client_id = self.query_one("#client_id").value
        self.channel = self.query_one("#channel").value
        self.dismiss((self.token, self.client_id, self.channel))
        
