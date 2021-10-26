import Entries.entry
from UI.ui import ui
from Database.database import Database
from datetime import datetime

ui = ui()
db = Database()

# UI Post events
# ui.window.ui.currentEntry.returnPressed.connect(SubmitEntry)
# ui.window.ui.console.returnPressed.connect(SubmitConsole)

# Create a few more files
# One for entry, maybe a class in UI to format UI input to entry class
# One for TODO and one for Reminder, on the same principle

# dummyEntry = entry.Entry('test123', datetime.now())
# db.WriteEntry(dummyEntry)

print(db.GetLastEntry())

# Also handle reminder beepage somehow, worry about that later, should not be problem

# ui.Start()