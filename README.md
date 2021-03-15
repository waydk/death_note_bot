# Death Note Telegram Bot

![Image alt](https://img.shields.io/badge/death%20note%20%F0%9F%93%93-telegram__bot-lightgrey)





<br>Death Note bot telegram is made for fun.</br>

## How to use
- Rename .env.dist to .env
### in the .env file
- Get a bot token from [@BotFather](http://telegram.me/BotFather) and replace BOT_TOKEN with your own
- Replace ADMINS with your id 
- Replace PGPASSWORD with your own
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
<br>![Image alt](https://github.com/waydk/death-note_bot/blob/main/examples/start_command.PNG)</br>
***
If a person clicks on the /rules:
<br>Then the rules with the page turnover keyboard will be displayed</br>
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/examples/rules_command.PNG)</br>
***
If the user presses /write_down, he will be sent to the death note entry state
<br>The first state will ask for the first and last name, the second the cause of death, and it will all be added to the database</br>
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/examples/death_note.PNG)</br>
*** 
The last command /death_list takes from the database, the people recorded in the death note, and displays the list to the user.
<br>![Image alt](https://github.com/waydk/DeathNoteBot/blob/main/examples/death_note_list.PNG)</br>
