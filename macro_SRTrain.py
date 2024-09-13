import configparser
import json
import time, logging
import requests

from SRT import SRT, SeatType
from SRT.errors import SRTResponseError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', )

# Read the configuration file
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    logging.info('read config.ini', config)
    return config

def reserve_train(srt, config):

    if 'time_limit' in config['reservation']:
        trains = srt.search_train(config['reservation']['departure'],
                               config['reservation']['destination'],
                                 config['reservation']['date'],
                                   config['reservation']['time'],
                                   time_limit = config['reservation']['time_limit'],
                                     available_only=False)
    else:
        trains = srt.search_train(config['reservation']['departure'],
                                config['reservation']['destination'],
                                    config['reservation']['date'],
                                    config['reservation']['time'],
                                        available_only=False)
    logging.info(f"예매를 시도합니다: {trains}")
    trials = 0
    while True:
        for train in trains:
            try:
                res = srt.reserve(train, special_seat=SeatType.GENERAL_FIRST)
                logging.info("reservation succeeded")
                return res
            except SRTResponseError as e:
                if e.msg != "잔여석없음":
                    logging.info("Error. Re logging in...")
                    srt = SRT(config['login']['username'], config['login']['password'])
            except json.decoder.JSONDecodeError as e:
                pass
            except Exception as e:
                logging.error(f"An error occurred: {e}")

        time.sleep(0.9)
        trials += 1
        logging.info(f"trial {trials}: Trains full, retrying...")

    return res

def send_message(message: str, url: str, userid: str):
    data = {
        "content": f"<@{userid}>",
        "embeds": [
            {
                "title": "SRT Booked",
                "description": f"{message}"
            }
        ]
    }
    requests.post(url, json=data)

def main():
    config = read_config()
    # Create an SRT instance
    srt = SRT(config['login']['username'], config['login']['password'])
    res = reserve_train(srt, config)
    send_message(str(res), config['discord']['url'], config['discord']['userid'])
    print(res)

if __name__ == '__main__':
    main()
