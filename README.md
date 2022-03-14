# ZeroSeg

[![Known Vulnerabilities](https://snyk.io/test/github/JakubBialoskorski/ZeroSeg/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/JakubBialoskorski/ZeroSeg?targetFile=requirements.txt)

Various python scripts for the 8-digits display. 

Install required module with ```sudo python setup.py install``` and then ```pip install -r requirements.txt``` . SPI needs to be manually enabled by running ```sudo raspi-config``` --> Interfacing Options.

You have to adjust market ticker(s) /  API key / developer token / number of your stocks inside the files.

```stock.py``` - display stock value (taken from alpha_vantage API)

```how_rich.py``` - display calculated value of your stocks

```clock.py``` - display four-digits clock (without seconds)

```ynab.py``` - display balance of selected YNAB category

```bitcoin.py``` - checks the current Bitcoin value in $US via Coindesk API (you may need to run `sudo apt-get install haveged` if the device is headless)

```kraken.py``` - checks Kraken account balance in Euro (put your key / secret pair into `kraken.key`)

For crons you can use expression like:

`*/10 * * * * python PATH/script.py`