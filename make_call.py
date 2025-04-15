import json
from twilio.rest import Client

def load_config():
    with open("config.json") as f:
        return json.load(f)

def make_call():
    config = load_config()
    client = Client(config["ACCOUNT_SID"], config["AUTH_TOKEN"])
    call = client.calls.create(
        to="+15555551234",
        from_=config["TWILIO_NUMBER"],
        url=config["TWIML_URL"]
    )
    print("Call initiated:", call.sid)

if __name__ == "__main__":
    make_call()
