import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/VJ_Bots')
    START_TXT = environ.get("START_TXT", '''HELLO {} ๐๐ป  ๐ธ ๐ฐ๐ผ ๐ฐ๐ฝ ๐ฐ๐ณ๐๐ฐ๐ฝ๐ฒ๐ด๐ณ ๐ฐ๐๐๐พ-๐ต๐ธ๐ป๐๐ด๐ ๐ฑ๐พ๐. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐ฐ๐ฝ๐ ๐๐ท๐พ๐๐๐ฝ๐ด๐ ๐ธ๐ฝ๐๐พ ๐ผ๐ด ๐๐ท๐ด๐ฝ ๐ธ ๐๐ธ๐ป๐ป ๐ถ๐ธ๐๐ด ๐๐พ๐๐ ๐ป๐ธ๐ฝ๐บ๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ @Anjel_Nehaโค๏ธโ๐ฅ</i>''')
    HELP_TXT = """สแดส {}
สแดสแด ษชs สแดสแด sแดแดแดษชแดษด. ."""
    ABOUT_TXT = """<b>แดสแดแดแด แดแด <i>๐ค แดส ษดแดแดแด : <a href=https://t.me/LinkSearchVJbot><b>สษชษดแด sแดแดสแดส สแดแด</b></a>\n
๐จโ๐ป แดแดแด แดสแดแดแดส : <a href=https://t.me/anjel_neha><b>แดษดแดแดส_ษดแดสแด</b></a>\n
๐ก สแดsแดแดแด แดษด : ๐๐๐๐ ๐๐๐\n
๐ข แดแดแดแดแดแดs แดสแดษดษดแดส : <a href=https://t.me/vj_bots><b></b>แดสษชแดแด สแดสแด</a>\n"""
    SOURCE_TXT = """<b>๐๐ซ๐๐๐ญ๐ ๐๐ง๐ ๐๐ข๐ค๐ ๐๐ก๐ข๐ฌ:</b>
ยป ๐๐๐ฃ๐ฉ ๐๐ค ๐๐๐ฅ๐ค ๐๐ ๐๐๐๐จ ๐ฝ๐ค๐ฉ ๐ฝ๐ช๐๐๐ฎ! <b>
ยป ๐๐ผ๐ป๐๐ฎ๐ฐ๐ ๐๐๐๐๐ ๐พ๐๐๐๐ผ๐พ๐ ๐ฝ๐๐ @Anjel_Neha<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/vj_bots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>แโบ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>แโบ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>แโบ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ  
    
<b>แโบ ๐๐ - <code>{}</code></b>
<b>แโบ ๐๐๐ฆ๐ - {}</b>
"""
    NORSLTS = """
โ #๐ก๐ผ๐ฅ๐ฒ๐๐๐น๐๐ โ
๐๐ <b>: {}</b>
๐ก๐ฎ๐บ๐ฒ <b>: {}</b>
๐ ๐ฒ๐๐๐ฎ๐ด๐ฒ <b>: {}</b>"""
