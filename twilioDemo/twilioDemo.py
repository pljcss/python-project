from twilio.rest import Client

def message(client):
    message = client.messages \
        .create(
        body="hello,弟弟",
        from_='+13392253360',
        to='+8613196986255'
    )
    print(message.sid)

def calls(client):
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+8613196986255',
        from_='+13392253360'
    )

    print(call.sid)

if __name__ == '__main__':
    account_sid = 'AC39040bbcf30ea09f0fd4d3a7f959076f'
    auth_token = '686b58f3657a8697ba56f9da813143c7'
    client = Client(account_sid, auth_token)

    calls(client)