from audible.console.gui import GuiCommand
from audible.console.run import RunCommand

from cleo.application import Application


def main() -> int:

    application = Application()

    application.add(GuiCommand())
    application.add(RunCommand())

    exit_code: int = Application().run()
    return exit_code


if __name__ == "__main__":
    main()
