from audible.console.gui import GuiCommand

from audible.console.run import RunCommand

from cleo.application import Application

# from cleo.commands.command import Command
# from cleo.helpers import argument, option


# class GuiCommand(Command):
#     """GUI Command"""

#     name = "gui"
#     description = "Launch Streamlit local Web App someone"

#     def handle(self):

#         self.line("Launching Streamlit Web App...")


def main() -> int:
    application = Application()

    application.add(GuiCommand())
    application.add(RunCommand())

    exit_code: int = Application().run()
    return exit_code


if __name__ == "__main__":
    application = Application()

    application.add(GuiCommand())
    application.add(RunCommand())

    application.run()

    # main()
