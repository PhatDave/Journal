from Entries.entry import Entry
from Entries.todoEntry import TodoEntry
from Entries.reminderEntry import ReminderEntry
from Entries.todos import TODOS
from Entries.reminders import Reminders
from UI.ui import ui
from Database.database import Database
from datetime import datetime
import random

ui = ui()
db = Database()
todos = TODOS(db.GetTODOs(), db)
reminders = Reminders(db.GetReminders(), db)

print(str(reminders))
reminders.RemoveEntry(13)
print(str(reminders))

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


# for i in range(50):
# 	dummyReminder = ReminderEntry(f'reminder 101 {random.randint(0, 100)}', datetime.now())
# 	todos.AddEntry(dummyReminder)


# Also handle reminder beepage somehow, worry about that later, should not be problem

# ui.Start()