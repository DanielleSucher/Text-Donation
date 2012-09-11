import os
from flask import Flask, request, redirect, session
import twilio.twiml
from twilio.rest import TwilioRestClient
from charity import Charity

SECRET_KEY = os.environ['DONATION_SECRET_KEY']
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    from_number = request.values.get('From', None)
    client = TwilioRestClient()
    charity = Charity()
    client.sms.messages.create(to="+17187535039",
                                from_=from_number,
                                body="fresh message!")

    message = from_number + ", thanks for the message!"
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
