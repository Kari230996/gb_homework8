'''Второе задание'''

import re

RE_REMOTE_ADDRESS = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}') # адрес ремовта
RE_REQUEST_DATETIME = re.compile(r'\d{1,2}\/\w+\/\d{4}(?::\d{2}){3}\s\+\d{4}') # дата реквеста
RE_REQUEST_TYPE = re.compile(r'"(\w+)') # тип реквеста
RE_REQUESTED_RESOURCE = re.compile(r' (/\w+/\w+)') # путь к реквесту
RE_RESPONSE_CODE_SIZE = re.compile('" (\d+) (\d+)') # код и размер ответа


with open('nginx_logs.txt') as file:
    for line in file:

        rm_addr = RE_REMOTE_ADDRESS.search(line).group()
        rq_datetime = RE_REQUEST_DATETIME.search(line).group()
        rq_type = RE_REQUEST_TYPE.search(line).group(1)
        re_resource = RE_REQUESTED_RESOURCE.search(line).group(1)
        rp_code = RE_RESPONSE_CODE_SIZE.search(line).group(1)
        rp_size = RE_RESPONSE_CODE_SIZE.search(line).group(2)


        parsed_raw = (rm_addr, rq_datetime, rq_type, re_resource, rp_code, rp_size)
        print(parsed_raw)






