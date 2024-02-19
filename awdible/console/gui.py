"""
GUI Command
"""

import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

import streamlit.web.cli as cli

# from ..gui.front import front


class GuiCommand(Command):
    """GUI Command"""

    name = "gui"
    description = "Launch Streamlit local Web App someone"

    def handle(self):
        self.line("Launching Streamlit Web App...")

        # dirname = os.path.dirname(__file__)
        # filename = os.path.join(dirname, "awdible", "gui", "front.py")
        # args = []
        # cli._main_run(filename, args)

        os.system("streamlit run awdible/gui/front.py")
