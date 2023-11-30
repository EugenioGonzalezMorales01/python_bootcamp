from smtplib import SMTP

from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def create_message(self, flight_data):
        city_from = flight_data["data"][0]['cityFrom']
        code_from = flight_data["data"][0]['flyFrom']
        city_to = flight_data["data"][0]['cityTo']
        code_to = flight_data["data"][0]['flyTo']
        price = f"{flight_data['data'][0]['price']} GBP"
        flight_from = flight_data["data"][0]['route'][0]['local_departure'].split("T")[0]
        flight_to = flight_data["data"][0]['route'][1]['local_departure'].split("T")[0]

        message = f'Low price alert! Only {price} GBP to fly from {city_from}-{code_from} to {city_to}-{code_to}, from {flight_from} to {flight_to}'

        routes = flight_data['data'][0]['route']
        cities_from = []
        cities_to = []
        if len(routes) > 2:
            for stop_over in routes:
                cities_from.append(stop_over['cityFrom'])
                cities_to.append(stop_over['cityTo'])

            message += "\n\nSTOP OVER(s) IN ARRIVING:\n"
            for x in range(len(cities_to)):
                if x < len(cities_to) / 2:
                    message += f"{cities_from[x]} --> {cities_to[x]}\n"
                elif x == len(cities_to) / 2:
                    message += f'\nSTOP OVER(s) COMING BACK:\n'
                    message += f"{cities_from[x]} --> {cities_to[x]}\n"
                else:
                    message += f"{cities_from[x]} --> {cities_to[x]}\n"
        return message
    def send_message(self, flight_data):

        message = self.create_message(flight_data)

        account_sid = 'AC4e7278511d438c2e09ce64876767b8fb'
        auth_token = 'a90993fc42dc322a61f4bee733911f4d'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{message}',
            to='whatsapp:+5212211250450'
        )

        print(message.body)

    def send_email(self, flight_data, users_data):

        my_email = "eugenio.de.astora@gmail.com"
        password = "mxenjbgvqivxmpst"
        server = "smtp.gmail.com"
        tls_port = 587

        message = self.create_message(flight_data)
        for user in users_data['users']:
            with SMTP(server, tls_port) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=user['email'],
                                    msg=f"Subject:Flight Found!\n\n{message}")





