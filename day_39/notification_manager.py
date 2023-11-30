from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, flight_data):
        city_from = flight_data["data"][0]['cityFrom']
        code_from = flight_data["data"][0]['flyFrom']
        city_to = flight_data["data"][0]['cityTo']
        code_to = flight_data["data"][0]['flyTo']
        price = f"{flight_data['data'][0]['price']} GBP"
        flight_from = flight_data["data"][0]['route'][0]['local_departure'].split("T")[0]
        flight_to = flight_data["data"][0]['route'][1]['local_departure'].split("T")[0]

        message = f'Low price alert! Only {price} GBP to fly from {city_from}-{code_from} to {city_to}-{code_to}, from {flight_from} to {flight_to}'

        account_sid = 'AC4e7278511d438c2e09ce64876767b8fb'
        auth_token = 'a90993fc42dc322a61f4bee733911f4d'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{message}',
            to='whatsapp:+5212211250450'
        )

        print(message.sid)