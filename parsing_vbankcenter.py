import requests
import lxml
from bs4 import BeautifulSoup
import os
from methods import *

dir_name = '711211'
list_files = creator_lisr_files(f'vb_data/{dir_name}')
creator_file_csv(f'report_{dir_name}.csv', 'Код', 'Название', 'ФИО', 'Должность', 'Телефон', 'Адрес', 'Email', 'ИНН',
                 'Налоговый орган')

count = 1
for item in list_files:

    content = reader_file(f'vb_data/{dir_name}/{item}')
    soup = BeautifulSoup(content, 'lxml')
    try:
        status_org = soup.find(
                class_='text-sm font-normal uppercase border rounded-2xl py-0.5 px-3 text-green border-green').text.strip()

        if status_org == 'Действует':
            list_info = soup.findAll(class_='gweb-copy relative inline-block mb-0 py-0 copy-available z-10 cursor-pointer '
                                            'copy-right-padding')

            code = list_info[3].text.strip()
            title = soup.find(class_='text-3xl mr-6').text.strip()
            fio = soup.find(class_='inline-block mb-1 w-max').text.strip()
            dolgnost = soup.findAll(class_='mb-1 text-premium-600')[1].text.strip(':')
            phone = list_info[5].text.strip()
            adres = list_info[4].text.strip()
            email = soup.find(class_='requisites-info-badge font-bold mb-1').findNext('a').text.strip()
            if len(email) > 30:
                email = ''
            inn = list_info[1].text.strip()
            nalog_org = list_info[6].text.strip()
            adder_data_in_file(f'report_{dir_name}.csv', code, title, fio, dolgnost, phone, adres, email, inn, nalog_org)
            print(count)
            count += 1
    except Exception:
        continue
