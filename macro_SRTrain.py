import configparser
from SRT import SRT, SeatType
import time, logging

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
                logging.info("reservation successed")
                break
            except Exception as e:
                pass
        
        time.sleep(0.1)
        trials += 1
        logging.info(f"trial {trials}: Trains full, retrying...")
        if trials % 10 == 0:    
            print(f"retrying... {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    return res

    

def main():
    config = read_config()
    # Create an SRT instance
    srt = SRT(config['login']['username'], config['login']['password'])
    res = reserve_train(srt, config)
    print(res)

if __name__ == '__main__':
    main()
    
