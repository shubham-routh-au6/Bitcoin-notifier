import argparse
import requests
from time import sleep
from datetime import datetime
from pytz import timezone


parser = argparse.ArgumentParser(
    description='''\
        Get Notification of latest Bitcoin price.
        Requirements:
        1 - IFTTT Account
        2 - Applet create with webhooks.
        3 - Two events one for normal alerts and another for emergency alerts.
        4 - IFTTT token of webhook
        5 - Time interval''')
parser.add_argument(
    '-c',
    '--Countrycode',
    type=str,
    default='INR',
    help='Country code of a'
    ' specific country for Bitcoin price')
parser.add_argument(
    '-l',
    '--Threshlimit',
    type=str,
    default='500000',
    help='Limit amount to '
    'get emergency alert'
    )
parser.add_argument(
    '-n',
    '--NormalUpdate',
    type=str,
    default='Final_Check',
    help='IFTTT event to get'
    ' normal update for any destination')
parser.add_argument(
    '-e',
    '--EmergencyUpdate',
    type=str,
    default='Emergency_check',
    help='IFTTT event to'
    ' get Emergency update for any destination')
parser.add_argument(
    '-f',
    '--IFTTTtoken',
    type=str,
    help='IFTTT event to get normal'
    ' update for any destination', required=True)
parser.add_argument(
    '-t',
    '--TimeInterval',
    default=2,
    type=int,
    help='Time frequency for alerts')
args = parser.parse_args()


if __name__ == '__main__':

    def link_telegram():
        def _end():
            print('Server has encountered error ! ')
            return
        try:
            country = args.Countrycode
            thresh = args.Threshlimit
            event = args.NormalUpdate
            threshevent = args.EmergencyUpdate
            ifttt_TOKEN = args.IFTTTtoken
            timer = args.TimeInterval
            print('Your Project is getting created !!!')
            sleep(5)
            print('IFTTT is linked.')
        except Exception:
            print("Input is invalid !")
            _end()

        def get_data(country):
            try:
                connection = requests.get(url='https://blockchain.info/ticker')
                data_in__json = connection.json()
                return (str(data_in__json[country.upper()]['last']) +
                        ' ' + str(data_in__json[country.upper()]['symbol']))
            except Exception:
                print('Data is not accessable from the url provided.')

        def formatdata():
            try:
                data = get_data(country)
                format = "Date: %Y-%m-%d || Time: %H:%M:%S"
                now_utc = datetime.now(timezone('UTC'))
                now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
                time = (now_asia.strftime(format))
                return (f'Price : {data} <br>{time} <br> <br> ')
            except Exception:
                print("Problem occured in formatting !")

        def sendtoIFTTT():
            datahistory = []
            i = 1
            while True:
                data = formatdata()
                try:
                    com = float(data.split(" ")[2])
                    if com < int(thresh):
                        price = com
                        symbol = (data.split(' ')[3])
                        string = f'{price} {symbol}'
                        requests.post(
                            url=f'https://maker.ifttt.com/trigger/{threshevent}/with/key/{ifttt_TOKEN}', # noqa
                            json={
                                'value1': (string)})
                        print('Posted Emergency Alert!')
                    else:
                        datahistory.append(data)
                except Exception:
                    print('Entered Wrong Details!')
                try:
                    print(f'Data collected {i} times !')
                    i += 1
                    sleep(timer)
                    ifttt_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{ifttt_TOKEN}' # noqa
                except Exception:
                    print("Project is not setupp Properly !")
                if len(datahistory) == 5:
                    try:
                        string = "".join([x + '\n' for x in datahistory])
                        data = {'value1': (string)}
                        s = requests.session()
                        requests.post(ifttt_url, json=data)
                        print('\nsent !')
                        s.close
                        del data
                        datahistory = []

                        print('Starting New Session !')
                        sendtoIFTTT()

                    except Exception:
                        print('something went wrong !!')
                        sendtoIFTTT()

        def starter():
            from time import sleep
            from tqdm import tqdm
            import sys
            try:
                animation = "✒✔༼ つ ◕_◕ ༽つ|/-\\"
                for i in range(25):
                    sleep(0.1)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()

                loop = tqdm(total=100, position=0, leave=False)
                for _ in range(100):
                    loop.set_description("Starting the Server ! ")
                    sleep(.1)
                    loop.update(1)
                loop.close()
                sendtoIFTTT()
            except(Exception):
                print('Starting the Project !')
                sendtoIFTTT()
        starter()


link_telegram()
