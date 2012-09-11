import os
from flask import Flask, request
import twilio.twiml
from charity import Charity


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    text_content = request.form['Body']

    if '5' in text_content:
        charity = Charity(5)
    elif '10' in text_content:
        charity = Charity(10)

    if charity is not None:
        message = "Text %s to %s to donate %s to %s" % (charity.code,
                                                        charity.to_number,
                                                        charity.amount,
                                                        charity.name)
    else:
        message = "Please enter 5 or 10 to specify the amount you wish donate."

    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
