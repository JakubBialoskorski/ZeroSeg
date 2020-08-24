## ZeroSeg

Various python scripts for the 8-digits display. 

Install required module with ```sudo python setup.py install``` and then ```pip install -r requirements.txt``` . SPI needs to be manually enabled by running ```sudo raspi-config``` --> Interfacing Options.

You have to adjust market ticker(s) /  API key / developer token / number of your stocks inside the files.

```stock.py``` - display stock value (taken from alpha_vantage API)

```how_rich.py``` - display calculated value of your stocks

```clock.py``` - display four-digits clock (without seconds)

```ynab.py``` - display balance of selected YNAB category

For crons you can use expression like:

`*/10 * * * * python PATH/script.py`