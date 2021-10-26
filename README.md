# Personal Journal

The main window consists of several text areas, in order from right-down:
- The previous journal entry (Read only)
- TODO list (Read only)
- The current journal entry
- Console used for manipulating the TODO list and the reminder list
- Markdown preview of the current entry (Read only)
- Reminder list (Read only)

## Console "commands"

The console allows the adding and removing of items to the todo and reminder list
- Adding to the TODO list `add <text>`
- Removing an item from the TODO list `rem <index>`
- Adding to the Reminder list `rmd add <datetime> |<text, optional>`
- Removing from the Reminder list `rmd rem <index>`

When adding reminders the datetime can be in following formats:
- %Y-%m-%d %H:%M:%S
- %Y/%m/%d %H:%M:%S
- %Y.%m.%d %H:%M:%S

- %Y-%m-%d %H:%M
- %Y/%m/%d %H:%M
- %Y.%m.%d %H:%M

- %m-%d %H:%M:%S
- %m/%d %H:%M:%S
- %d.%m %H:%M:%S

- %m-%d %H:%M
- %m/%d %H:%M
- %d.%m %H:%M

- %H:%M:%S
- %H:%M

Where y represents the year, m the month, d the day, h the hour, m the minute and s the second

All other entries are timestamped at the time of creation