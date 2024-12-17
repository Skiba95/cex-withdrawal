
# Token Withdrawal Script for Centralized Exchanges

## Overview

This script facilitates the withdrawal of tokens from major centralized exchanges, including Binance, MEXC, KuCoin, Gate, OKX, Huobi, Bybit, Bitget, and CoinEx. It provides an automated way to manage token transfers using APIs provided by the respective exchanges.

## Prerequisites

1. **Python Version**: Ensure you have Python 3.11.5 installed.
2. **API Keys**: Obtain API keys for each exchange you intend to use. Ensure the keys have appropriate permissions for withdrawals.
3. **Dependencies**: Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

## Installation

1. Clone this repository or copy the script files to your desired directory.
2. Set up your `requirements.txt` file, which should contain the necessary libraries such as `ccxt`, `loguru`, and others you may need.
3. Configure your environment variables or configuration file for API keys and security information.

## Usage

1. **Run the Script**: Use the following command to execute the script:

    ```bash
    python main.py
    ```

2. **Arguments**: Depending on your implementation, you may be able to provide arguments such as token symbols, withdrawal amounts, and target addresses.


## Supported Exchanges

The following exchanges are supported by the script:

- Binance
- MEXC
- KuCoin
- Gate.io
- OKX
- Huobi
- Bybit
- Bitget
- CoinEx


## License

This project is licensed under the [MIT License](LICENSE).
