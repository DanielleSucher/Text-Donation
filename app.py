import os
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.sms("Hello, Mobile Monkey")
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
