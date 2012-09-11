import os
from flask import Flask, request
import twilio.twiml
from charity import Charity


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    text_content = request.args.get('Body').lower()
    if text_content == '5':
        charity = Charity(5)
        amount = '$5'
    elif text_content == '5':
        charity = Charity(10)
        amount = '$10'
    else:
        resp = twilio.twiml.Response()
        resp.sms("Please enter 5 or 10 to specify the amount you wish donate.")
        return str(resp)
    message = "Text %s to %s to donate %s to %s" % (charity.code,
                                                    charity.to_number,
                                                    amount,
                                                    charity.name)
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
