from urllib import request
from urllib.parse import urlencode
import re
import csv
from tqdm import tqdm


def get_one_page(city, keyword):
    paras = {
        'pageSize': 60,
        'cityId': city,  # 深圳编号
        'industry': 10100,  # 服务业
        'workExperience': -1,  # 工作经验不限
        'education': -1,  # 之后都是默认值
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': keyword,
        'kt': 3,
        'lastUrlQuery': {"pageSize": "60", "jl": "765", "in": "10100", "kw": "python", "kt": "3"}
    }
    url = 'https://fe-api.zhaopin.com/c/i/sou?' + urlencode(paras)
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

    r = request.urlopen(req)
    return r.read().decode('utf-8')


def parse_one_page(data):
    pattern = re.compile('.htm","name":"(.*?)","size":{"code":.*?''"positionURL":"(.*?)","workingExp":.*?''"salary":"(.*?)","emplType":.*?''"jobName":"(.*?)","industry"', re.S)
    items = re.findall(pattern, data) #items为一个列表
    print(items)
    for item in items:
        yield {
            'job': item[3],
            'company': item[0],
            'salary': item[2],
            'URL': item[1]
        }


def write_csv_rows(path, headers, rows):
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)


def write_csv_headers(path, headers):
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()


def main(city, keyword, pages=5):
    filename = 'zl_' + city + '_' + keyword + '.csv'
    headers = ['job', 'company', 'salary', 'URL']
    write_csv_headers(filename, headers)
    '''
    获取该页中所有职位信息，写入csv文件
    '''
    jobs = []
    html = get_one_page(city, keyword)
    items = parse_one_page(html)
    for item in items:
        jobs.append(item)
    write_csv_rows(filename, headers, jobs)


if __name__ == '__main__':
    city = input('城市')
    keyword = input('职位')
    main(city, keyword)
