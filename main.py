import SpawnThread
from Database.database import Database
from Entries.reminders import Reminders
from Entries.todos import TODOS
from UI.QtUIInterface import UiInterface
from Beeper import Beeper

# TODO: Now make it show up every 10 min or something like that
# Alarm does not stop!!! help D:

db = Database()
todos = TODOS(db.GetTODOs(), db)
reminders = Reminders(db.GetReminders(), db)

beeper = Beeper(reminders)
beeper.Start()
# beeper.StartBeeping()

ui = UiInterface(todos, reminders, db, beeper)
spawnThread = SpawnThread.SpawnThread(15 * 60, ui)

# ui.ConsoleSubmit('rmd 10:55')
# ui.ConsoleSubmit('rmd 10:55 |test123')
# ui.ConsoleSubmit('rmd 26.11 10:55 |test123')
# quit()

ui.Start()