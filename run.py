from flask import Flask, request
from twilio import twiml


app = Flask(__smschat__)

@app.route('/', methods=['POST'])
def sms():

    message_body = request.form['Body']

    resp = twiml.Response()

    replyText = getReply(message_body)

    resp.message('Hi\n\n' + replyText )
    return str(resp)

if __smschat__ == '__main__':
    app.run()


