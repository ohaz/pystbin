# Pystbin

Pystbin is a pastebin application written in Python 3.
It currently allows everybody who has access to a certain token to upload text, which then gets show with syntax highlighting.

## Installation

* Install Python
* pip install -r requirements.txt

Then, copy the config.default.py to config.py and replace the two strings with better secrets.
If you want to generate secrets, try running: `python -c "import uuid; print(uuid.uuid4().hex)"` in a console.

Edit port and debug if you want to.
You should not run the server in debug mode, if you want to use it in production!

Now, simply run `python pystbin.py` in a console and the server should run!


## API

### Reading a paste
Run a HTTP GET on example.com/s/*id*/ to get the paste. Replace the id with the id of a paste!

### Posting a paste
Run a HTTP Post on example.com/u/*key* with the key you set as the auth_key in the config file.
The request has to contain the following HTTP POST parameters:

* "title" (the title of the paste)
* "text" (the text to paste)
* "language" (string out of the dict in app.py)
* "hllines" (comma seperated list of integers)

Additionally, you can go to example.com/u/*key* in a browser and enter your paste there.

Example:
title="Test", text="print('Hello World!')", language="python", hllines="1"