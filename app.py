import os
from flask import Flask, request
import twilio.twiml
from twilio.rest import TwilioRestClient


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    from_number = request.args.get('From')
    text_content = request.args.get('Body').lower()

    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'],
                              os.environ['TWILIO_AUTH_TOKEN'])
    client.sms.messages.create(to="+17187535039",
                                from_=from_number,
                                body="fresh message!")

    message = from_number + ", thanks for the donation!"
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
