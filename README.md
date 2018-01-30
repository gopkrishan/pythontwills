![Python Twills](https://github.com/omarjcameron/pythontwills/blob/master/appscreenshot1.png)
![Python Twills](https://github.com/omarjcameron/pythontwills/blob/master/appscreenshot2.png)

### Synopsis

Python Twills - A Python/Twilio Based Chatbot helping you research life's questions on the fly. 

### Motivation

Have you ever wanted to pass the time by texting wikipedia queries to an automated chatbot? Of course you have! Who hasn't? Settle those pressing debates and arguments with knowledge at your disposal!

### Usage

You'll need a Twilio account, python installed, pip, wikipedia and yweather

If you have Python and Pip installed you can just use "pip install" to acquire these other dependencies. 

Clone this repo and start up your python server by running: 

python run.py

Fire up that ngrok partition by running (port number is visible after you start the python server):

“ngrok http [port number]”

Visit your Twilio dashboard and copy over your ngrok forwarding address to incoming messaging webhook.

Shoot over a text to your Twilio number. If you're hungry try "Wiki Cheeseburger"!

### Languages, Frameworks & APIs

Python
Twilio
Wikipedia API 
Yweather API (deprecated)
