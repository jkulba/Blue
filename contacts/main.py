# -*- coding: utf-8 -*-
# contacts/main.py

"""This module provides Blue Contacts application."""

import sys

from PyQt6.QtWidgets import QApplication

from .views import Window

def main():
    """Blue Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
