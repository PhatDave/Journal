from Database.database import Database
from Entries.reminders import Reminders
from Entries.todos import TODOS
from UI.QtUIInterface import UiInterface
from Beeper import Beeper

# TODO: Still need to create alarm and beeper

db = Database()
todos = TODOS(db.GetTODOs(), db)
reminders = Reminders(db.GetReminders(), db)

beeper = Beeper(reminders)
beeper.Start()

ui = UiInterface(todos, reminders, db, beeper)

# ui.ConsoleSubmit('rmd 10:55')
# ui.ConsoleSubmit('rmd 10:55 |test123')
# ui.ConsoleSubmit('rmd 26.11 10:55 |test123')
# quit()

ui.Start()