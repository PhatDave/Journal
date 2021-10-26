from Entries.entry import Entry
from Entries.todoEntry import TodoEntry
from Entries.reminderEntry import ReminderEntry
from Entries.todos import TODOS
from UI.ui import ui
from Database.database import Database
from datetime import datetime
import random

ui = ui()
db = Database()

# UI Post events
# ui.window.ui.currentEntry.returnPressed.connect(SubmitEntry)
# ui.window.ui.console.returnPressed.connect(SubmitConsole)

# Create a few more files
# One for entry, maybe a class in UI to format UI input to entry class
# One for TODO and one for Reminder, on the same principle

# dummyEntry = Entry('test123', datetime.now())
# dummyTODO = TodoEntry('do stuff', datetime.now())
# dummyReminder = ReminderEntry('d ostuff sometime later mayeb', datetime.now())
# db.WriteEntry(dummyEntry)
# db.WriteEntry(dummyTODO)
# db.WriteEntry(dummyReminder)
# quit()

todos = TODOS(db.GetTODOs())
todos.db = db

# for i in range(50):
# 	dummyTODO = TodoEntry(f'do stuff {random.randint(0, 100)}', datetime.now())
# 	todos.AddEntry(dummyTODO)

print(todos.tlist)
print(str(todos))
todos.RemoveEntry(1)
print(todos.tlist)
print(str(todos))

# Also handle reminder beepage somehow, worry about that later, should not be problem

# ui.Start()