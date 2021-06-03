# -*- coding: utf-8 -*-
# contacts/main.py

"""This module provides Blue Contacts application."""

import sys, logging

from PyQt6.QtWidgets import QApplication

from .database import createConnection
from .views import Window

# Prepare the logger
_logger = logging.getLogger('contacts')

def main():
    """Blue Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
      # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    _logger.debug("Show window")
    # Run the event loop
    sys.exit(app.exec())
