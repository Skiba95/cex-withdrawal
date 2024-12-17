from config import cex, symbolWithdraw, network, decimal_places, amount, shuffle_wallets, chat, bot_id, delay, proxy_server
from config import binance_apikey, binance_apisecret, okx_apikey, okx_apisecret ,okx_passphrase ,bybit_apikey, bybit_apisecret
from config import gate_apikey, gate_apisecret, kucoin_apikey, kucoin_apisecret, kucoin_passphrase, mexc_apikey, mexc_apisecret
from config import huobi_apikey, huobi_apisecret, bitget_apikey, bitget_apisecret, bitget_password, coinex_apikey, coinex_apisecret


from loguru import logger
import time, random, ccxt, telebot


#--------------------------------------------------------- cex-withdraw ---------------------------------------------------------#

def binance_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.binance({
        'apiKey': API.binance_apikey,
        'secret': API.binance_apisecret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def okx_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.okx({
        'apiKey': API.okx_apikey,
        'secret': API.okx_apisecret,
        'password': API.okx_passphrase,
        'enableRateLimit': True,
        'proxies': proxies,
    })

    try:
        chainName = symbolWithdraw + "-" + network
        fee = get_withdrawal_fee(symbolWithdraw, chainName)
        exchange.withdraw(symbolWithdraw, amount_to_withdrawal, address,
            params={
                "toAddress": address,
                "chainName": chainName,
                "dest": 4,
                "fee": fee,
                "pwd": '-',
                "amt": amount_to_withdrawal,
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def bybit_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.bybit({
        'apiKey': API.bybit_apikey,
        'secret': API.bybit_apisecret,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "forceChain": 1,
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def gate_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.gate({
        'apiKey': API.gate_apikey,
        'secret': API.gate_apisecret,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def kucoin_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.kucoin({
        'apiKey': API.kucoin_apikey,
        'secret': API.kucoin_apisecret,
        'password': API.kucoin_passphrase,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def mexc_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.mexc({
        'apiKey': API.mexc_apikey,
        'secret': API.mexc_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def huobi_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.huobi({
        'apiKey': API.huobi_apikey,
        'secret': API.huobi_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


def bitget_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.bitget({
        'apiKey': API.bitget_apikey,
        'secret': API.bitget_apisecret,
        'password': API.bitget_password,
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
        }) 
    
    try:

        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={"network": network}
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')

def coinex_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.coinex({
        'apiKey': API.coinex_apikey,
        'secret': API.coinex_apisecret
        # 'withdraw_method' : 'on_chain'
        }) 
    
    try:

        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={"network": network}
        )
        logger.success(f'[{wallet_number}][{address}] Withdrew {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n✅ Withdrew {amount_to_withdrawal} {symbolWithdraw}')
    except Exception as error:
        logger.error(f'[{wallet_number}][{address}] Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        send_telegram_message(f'[{wallet_number}] {address}\n\n❌ Cant Withdraw {amount_to_withdrawal} {symbolWithdraw}: {error}')


#----------------------------------------------------------- helpers -----------------------------------------------------------#

class API:
    # binance API
    binance_apikey = binance_apikey
    binance_apisecret = binance_apisecret
    # okx API
    okx_apikey = okx_apikey
    okx_apisecret = okx_apisecret
    okx_passphrase = okx_passphrase
    # bybit API
    bybit_apikey = bybit_apikey
    bybit_apisecret = bybit_apisecret
    # gate API
    gate_apikey = gate_apikey
    gate_apisecret = gate_apisecret
    # kucoin API
    kucoin_apikey = kucoin_apikey
    kucoin_apisecret = kucoin_apisecret
    kucoin_passphrase = kucoin_passphrase
    # mexc API
    mexc_apikey = mexc_apikey
    mexc_apisecret = mexc_apisecret
    # huobi API
    huobi_apikey = huobi_apikey
    huobi_apisecret = huobi_apisecret
    # bitget API
    bitget_apikey = bitget_apikey
    bitget_apisecret = bitget_apisecret
    bitget_password = bitget_password
    # coinex API
    coinex_apikey = coinex_apikey
    coinex_apisecret = coinex_apisecret

proxies = {
  "http": proxy_server,
  "https": proxy_server,
}

def choose_cex(address, amount_to_withdrawal, wallet_number):
    if cex == "binance":
        binance_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "okx":
        okx_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "bybit":
        print(f"\n>>> Bybit в больнице, у них API заболело, sorry") #bybit_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "gate":
        gate_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "huobi":
        huobi_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "kucoin":
        kucoin_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "mexc":
        mexc_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "bitget":
        bitget_withdraw(address, amount_to_withdrawal, wallet_number)
    elif cex == "coinex":
        coinex_withdraw(address, amount_to_withdrawal, wallet_number)
    else:
        raise ValueError("Invalid CEX. Supported are: binance, okx, bybit, gate, huobi, kucoin, mexc, bitget, coinex")

def get_withdrawal_fee(symbolWithdraw, chainName):
    exchange = ccxt.okx({
        'apiKey': API.okx_apikey,
        'secret': API.okx_apisecret,
        'password': API.okx_passphrase,
        'enableRateLimit': True,
        'proxies': proxies,
    })
    currencies = exchange.fetch_currencies()
    for currency in currencies:
        if currency == symbolWithdraw:
            currency_info = currencies[currency]
            network_info = currency_info.get('networks', None)
            if network_info:
                for network in network_info:
                    network_data = network_info[network]
                    network_id = network_data['id']
                    if network_id == chainName:
                        withdrawal_fee = currency_info['networks'][network]['fee']
                        if withdrawal_fee == 0:
                            return 0
                        else:
                            return withdrawal_fee
    raise ValueError(f" Unable to retrieve the commission amount, please check the values symbolWithdraw и network")

def shuffle(wallets_list, shuffle_wallets):
    numbered_wallets = list(enumerate(wallets_list, start=1))
    if shuffle_wallets.lower() == "yes":
        random.shuffle(numbered_wallets)
    elif shuffle_wallets.lower() == "no":
        pass
    else:
        raise ValueError("\n>>> Invalid value for the 'shuffle_wallets' variable. Expected 'yes' or 'no'.")
    return numbered_wallets

def send_telegram_message(message):

    bot = telebot.TeleBot(bot_id)
    chat_id = chat
    
    bot.send_message(chat_id, message)  


#------------------------------------------------------------- main -------------------------------------------------------------#


if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f if row.strip()]
        numbered_wallets = shuffle(wallets_list, shuffle_wallets)
        logger.info(f'Number of wallets: {len(wallets_list)}')
        logger.info(f"CEX: {cex}")
        logger.info(f"Amount: {amount[0]} - {amount[1]} {symbolWithdraw}")
        logger.info(f"Network: {network}")
        time.sleep(random.randint(2, 4))

        for wallet_number, address in numbered_wallets:
            amount_to_withdrawal = round(random.uniform(amount[0], amount[1]), decimal_places)
            choose_cex(address, amount_to_withdrawal, wallet_number)
            time.sleep(random.randint(delay[0], delay[1]))



