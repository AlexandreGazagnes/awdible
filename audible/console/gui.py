from cleo.commands.command import Command
from cleo.helpers import argument, option


class GuiCommand(Command):
    """GUI Command"""

    name = "gui"
    description = "Launch Streamlit local Web App someone"

    def handle(self):

        self.line("Launching Streamlit Web App...")
