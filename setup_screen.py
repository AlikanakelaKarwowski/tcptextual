from textual import on
from textual.app import App
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label


class Setup(Screen):

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
        token = self.query_one("#token").value 
        client_id = self.query_one("#client_id").value
        channel = self.query_one("#channel").value
        self.dismiss((token, client_id, channel))
        
