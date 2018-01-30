from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import yweather
import wikipedia

client = yweather.Client()


# Format text input with this function
def removeHead(fromThis, removeThis):
    if fromThis.endswith(removeThis):
        fromThis = fromThis[:-len(removeThis)].strip()
    elif fromThis.startswith(removeThis):
        fromThis = fromThis[len(removeThis):].strip()

    return fromThis

# formulate a response based on message input.
def getReply(message):

    # Make the message lower case and without spaces on the end for easier handling
    message = message.lower().strip().encode('ascii','ignore')
    # This is the variable where we will store our response
    answer = ""

    if "weather" in message:
        message = removeHead(message, "weather")
        local_iden = client.fetch_woeid(message)
        weather = client.fetch_weather(local_iden)

        try:
         # Get the weather from certain plain

            answer = weather["condition"]["text"]
        except:
            # handle errors
            answer = "Request was not found using yweather. Enter your location as City, State or City, Country."

    # check to see if the keyword "wiki" is in the message?
    elif "wiki" in message:
        # strip "wiki" from the message
        message = removeHead(message, "wiki")
        # Get the wikipedia summary for the request
        try:
         # Get the summary off wikipedia
            answer = wikipedia.summary(message)
        except:
            # handle errors
            answer = "Request was not found using wiki. Be more specific?"

    # error handling prompt
    else:
        answer = "\n Welcome! These are the commands you may use: \nWIKI \"wikipedia request\"\nWEATHER \"place\""

    # shortening message due to constraints
    if len(answer) > 1500:
        answer = answer[0:1500] + "..."

    # return the formulated answer
    return answer

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sms():

    message_body = request.form['Body']
    resp = MessagingResponse()

    replyText = getReply(message_body)
    resp.message('Hi\n\n' + replyText )
    return str(resp)

if __name__ == '__main__':
    app.run()