import os
from flask import Flask, request
import twilio.twiml
from charity import Charity


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    text_content = request.form['Body']

    if '5' in text_content:
        donee = Charity(5)
    elif '10' in text_content:
        donee = Charity(10)

    message = "Please enter 5 or 10 to specify the amount you wish donate."
    if donee is not None:
        message = "Text %s to %s to donate %s to %s" % (donee.code,
                                                        donee.to_number,
                                                        donee.amount,
                                                        donee.name)

    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
