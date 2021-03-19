# Death Note Telegram Bot
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwaydk%2FDeathNoteBot&count_bg=%23000000&title_bg=%23000000&icon=riseup.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
## How to use
- Rename .env.dist to .env
### in the .env file
- Get a bot token from [@BotFather](http://telegram.me/BotFather) and replace BOT_TOKEN with your own
- Replace ADMINS with your id 
- Replace PGPASSWORD with your own
- Replace DATABASE with your own
#### compile languages
pybabel compile -d locales -D death_note_bot
### If there are questions: [Telegram](https://t.me/waydk)

<br>available commands:</br>
<br>/start - start a conversation</br>
/help - get info
<br>/rules - rules for the use of the death note</br>
/write_down - write in the death note
<br>/death_list - show victim list</br>
***
At the command to start:
<br>A user database is created and the user is added to it and a welcome message is displayed</br>
<br>![Image alt](https://github.com/waydk/death-note_bot/blob/main/src/examples/start_command.PNG)</br>
***
If a person clicks on the /rules:
<br>Then the rules with the page turnover keyboard will be displayed</br>
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/src/examples/rules_command.PNG)</br>
***
If the user presses /write_down, he will be sent to the death note entry state
<br>The first state will ask for the first and last name, the second the cause of death, and it will all be added to the database</br>
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/src/examples/death_note.PNG)</br>
*** 
The last command /death_list takes from the database, the people recorded in the death note, and displays the list to the user.
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/src/examples/death_note_list.PNG)</br>
