from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from misc import bot
from config import USERID
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from bs4 import BeautifulSoup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import json

a1 = KeyboardButton(text='Посмотреть')
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(a1)

async def command_start(message: types.Message):
    '''Пиздец тут'''
    auth = 'https://trade.aliexpress.ru/orderList.htm'

    s = Service('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument(r'--user-data-dir=data')
    chrome_options.add_argument(r'--remote-debugging-port=9222')
    chrome_options.headless = False
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(auth)
    main = driver.page_source
    sleep(1)

    with open('page.html', 'w+', encoding='utf-8') as f:
        f.write(main)
        f.close()

    with open(r'page.html', 'r', encoding='utf-8') as fb:
        datas = fb.read()

    soup = BeautifulSoup(datas, 'html.parser')
    script = soup.find(name='script', id='__AER_DATA__')

    with open(r'al.json', 'r+', encoding='utf-8') as f:
        f.read()
        f.close()

    with open('al.json', 'w', encoding='utf-8') as f:
        f.write(str(script).replace('<script id="__AER_DATA__" type="application/json">', '').replace('</script>', ''))

    with open('al.json', 'r', encoding='utf-8') as f:
        contents = json.load(f)

    try:
        with open('al.json', 'r', encoding='utf-8') as f:
            contents = json.load(f)

            orderNumber = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][0]['orderNumber']
            name = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][0]['items'][0]['name']
            detailLink = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][0]['detailLink']
            imgUrl = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][0]['items'][0]['imgUrl']
            imgUrl = str(imgUrl)
            imgUrl = imgUrl.replace('50x50', '500x500')

            orderNumber1 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][1]['orderNumber']
            name1 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][1]['items'][0]['name']
            detailLink1 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][1]['detailLink']
            imgUrl1 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][1]['items'][0]['imgUrl']
            imgUrl1 = str(imgUrl1)
            imgUrl1 = imgUrl1.replace('50x50', '500x500')

            orderNumber2 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][2]['orderNumber']
            name2 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][2]['items'][0]['name']
            detailLink2 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][2]['detailLink']
            imgUrl2 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][2]['items'][0]['imgUrl']
            imgUrl2 = str(imgUrl2)
            imgUrl2 = imgUrl2.replace('50x50', '500x500')

            orderNumber3 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][3]['orderNumber']
            name3 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][3]['items'][0]['name']
            detailLink3 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][3]['detailLink']
            imgUrl3 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][3]['items'][0]['imgUrl']
            imgUrl3 = str(imgUrl3)
            imgUrl3 = imgUrl3.replace('50x50', '500x500')

            orderNumber4 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][4]['orderNumber']
            name4 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][4]['items'][0]['name']
            detailLink4 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][4]['detailLink']
            imgUrl4 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][4]['items'][0]['imgUrl']
            imgUrl4 = str(imgUrl4)
            imgUrl4 = imgUrl4.replace('50x50', '500x500')

            orderNumber5 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][5]['orderNumber']
            name5 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][5]['items'][0]['name']
            detailLink5 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][5]['detailLink']
            imgUrl5 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][5]['items'][0]['imgUrl']
            imgUrl5 = str(imgUrl5)
            imgUrl5 = imgUrl5.replace('50x50', '500x500')

            orderNumber6 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][6]['orderNumber']
            name6 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][6]['items'][0]['name']
            detailLink6 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][6]['detailLink']
            imgUrl6 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][6]['items'][0]['imgUrl']
            imgUrl6 = str(imgUrl6)
            imgUrl6 = imgUrl6.replace('50x50', '500x500')

            orderNumber7 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][7]['orderNumber']
            name7 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][7]['items'][0]['name']
            detailLink7 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][7]['detailLink']
            imgUrl7 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][7]['items'][0]['imgUrl']
            imgUrl7 = str(imgUrl7)
            imgUrl7 = imgUrl7.replace('50x50', '500x500')

            orderNumber8 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][8]['orderNumber']
            name8 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][8]['items'][0]['name']
            detailLink8 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][8]['detailLink']
            imgUrl8 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][8]['items'][0]['imgUrl']
            imgUrl8 = str(imgUrl8)
            imgUrl8 = imgUrl8.replace('50x50', '500x500')

            orderNumber9 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][9]['orderNumber']
            name9 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][9]['items'][0]['name']
            detailLink9 =  contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][9]['detailLink']
            imgUrl9 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][9]['items'][0]['imgUrl']
            imgUrl9 = str(imgUrl9)
            imgUrl9 = imgUrl9.replace('50x50', '500x500')

            orderNumber10 =  contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][10]['orderNumber']
            name10 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][10]['items'][0]['name']
            detailLink10 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][10]['detailLink']
            imgUrl10 = contents['widgets'][4]['children'][1]['children'][0]['children'][2]['props']['orderList']['orders'][10]['items'][0]['imgUrl']
            imgUrl10 = str(imgUrl10)
            imgUrl10 = imgUrl10.replace('50x50', '500x500')
    except IndexError:
        pass


        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink}">Перейти</a>\n'
                 f'<a href="{imgUrl}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name1}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber1}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink1}">Перейти</a>\n'
                 f'<a href="{imgUrl1}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name2}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber2}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink2}">Перейти</a>\n'
                 f'<a href="{imgUrl2}">&#8203;</a>',
            parse_mode='HTML',
            reply_markup=kb_main
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name3}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber3}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink3}">Перейти</a>\n'
                 f'<a href="{imgUrl3}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name4}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber4}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink4}">Перейти</a>\n'
                 f'<a href="{imgUrl4}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name5}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber5}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink5}">Перейти</a>\n'
                 f'<a href="{imgUrl5}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name6}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber6}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink6}">Перейти</a>\n'
                 f'<a href="{imgUrl6}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name7}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber7}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink7}">Перейти</a>\n'
                 f'<a href="{imgUrl7}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name8}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber8}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink8}">Перейти</a>\n'
                 f'<a href="{imgUrl8}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name9}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber9}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink9}">Перейти</a>\n'
                 f'<a href="{imgUrl9}">&#8203;</a>',
            parse_mode='HTML'
        )

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'👓 Название заказа: \n{name10}\n'
                 f'🆔 Номер заказа: <strong>{orderNumber10}</strong>\n'
                 f'💬 Подробнее о заказе: <a href="{detailLink10}">Перейти</a>\n'
                 f'<a href="{imgUrl10}">&#8203;</a>',
            parse_mode='HTML'
        )

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, Text(equals=['Посмотреть', '/start']))
