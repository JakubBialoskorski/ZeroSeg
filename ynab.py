#!/usr/bin/env python

import requests, os, time, requests, json, urllib
import ZeroSeg.led as led
from datetime import datetime

device = led.sevensegment(cascaded=2)
device.clear()
level = 1
device.brightness(level)

SELECTED_CATEGORY = os.environ.get("SELECTED_CATEGORY", "MAIN_CATEGORY") # for example: Big expenses
SELECTED_SUBCATEGORY = os.environ.get("SELECTED_SUBCATEGORY", "SUBCATEGORY_UNDER_MAIN_CATEGORY") # for example: Own House

def get_all_category_data():
    headers = {'Authorization': 'Bearer DEVELOPER_TOKEN_HERE'}
    response = requests.get('https://api.youneedabudget.com/v1/budgets/BUDGET_ID/categories',headers=headers) # put your budget ID here
    return response.json()

def check_the_balance_of_the_selected_category(categories,selected_category=SELECTED_CATEGORY,selected_subcategory=SELECTED_SUBCATEGORY):
    for category in categories:
        category_name = category.get('name')
        subcategories = category.get('categories')
        if category_name == selected_category:
            for subcategory in subcategories:
                subcategory_name = subcategory.get('name')
                if subcategory_name == selected_subcategory:
                    balance = subcategory.get('balance')
                    return balance
def main():
    categories = get_all_category_data()['data']['category_groups']
    balance = check_the_balance_of_the_selected_category(categories)
    device.write_text(1, " " + "{0:.0f}".format(balance/1000)[:8]) #0f for no digits after dot, 2f for two digits

main()