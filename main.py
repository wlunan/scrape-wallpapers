import requests
from lxml import etree
import os
import time
import random
import yaml
from datetime import datetime

# 加载配置文件
def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 设置请求头，模拟浏览器访问
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# 创建日志文件
def create_logger(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    start_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'{start_time}.log')
    return log_file

# 写入日志
def write_log(log_file, filename, url, status):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'{now} | {filename} | {url} | {status}\n')

# 获取每页页面html（支持toplist、search和hot三种模式）
def get_html_info(page, mode='toplist', keyword=''):
    if mode == 'search':
        url = f'https://wallhaven.cc/search?q={keyword}&page={page}'
    elif mode == 'hot':
        url = f'https://wallhaven.cc/hot?page={page}'
    else:
        url = f'https://wallhaven.cc/toplist?page={page}'
    resp = requests.get(url, headers=headers)
    resp_html = etree.HTML(resp.text)
    return resp_html

# 获取每页图片的链接
def get_pic(resp_html, save_dir, log_file, config):
    pic_url_list = []
    lis = resp_html.xpath('//*[@id="thumbs"]/section[1]/ul/li')
    
    for li in lis:
        pic_url = li.xpath('./figure/a/@href')[0]
        pic_url_list.append(pic_url)

    for pic_url in pic_url_list:
        try:
            resp2 = requests.get(pic_url, headers=headers)
            r_html2 = etree.HTML(resp2.text)
            
            # 获取分辨率
            pic_size_list = r_html2.xpath('//*[@id="showcase-sidebar"]/div/div[1]/h3/text()')
            if not pic_size_list:
                print(f'无法获取图片信息，跳过: {pic_url}')
                write_log(log_file, '未知', pic_url, '失败-无法获取图片信息')
                continue
            pic_size = pic_size_list[0]
            
            # 获取原图地址
            final_url_list = r_html2.xpath('//*[@id="wallpaper"]/@src')
            if not final_url_list:
                print(f'无法获取下载地址，跳过: {pic_url}')
                write_log(log_file, '未知', pic_url, '失败-无法获取下载地址')
                continue
            final_url = final_url_list[0]
            
            # 下载图片
            pic = requests.get(url=final_url, headers=headers).content
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            
            filename = pic_size + final_url[-10:]
            with open(os.path.join(save_dir, filename), mode='wb') as f:
                f.write(pic)
            
            count = len(os.listdir(save_dir))
            print(f'{filename}，下载完毕，已下载{count}张壁纸')
            write_log(log_file, filename, final_url, '成功')
            
            # 随机休眠
            time.sleep(random.uniform(config['request_delay_min'], config['request_delay_max']))
            
        except Exception as e:
            print(f'下载失败: {pic_url}, 错误: {e}')
            write_log(log_file, '未知', pic_url, f'失败-{str(e)}')
        
# 获取实际保存目录
def get_save_dir(config):
    save_dir = config['save_dir']
    
    # 按日期创建子文件夹
    if config.get('create_date_subfolder', False):
        today = datetime.now().strftime('%Y-%m-%d')
        save_dir = os.path.join(save_dir, today)
    
    # 按关键词创建子文件夹（仅搜索模式）
    if config['mode'] == 'search' and config.get('create_keyword_subfolder', False):
        keyword = config.get('search_keyword', '')
        if keyword:
            save_dir = os.path.join(save_dir, keyword)
    
    return save_dir

def main():
    config = load_config()
    log_file = create_logger(config['log_dir'])
    save_dir = get_save_dir(config)
    
    print(f'日志文件: {log_file}')
    print(f'保存目录: {save_dir}')
    print(f'运行模式: {config["mode"]}')
    if config['mode'] == 'search':
        print(f'搜索关键词: {config["search_keyword"]}')
    print('=' * 50)
    
    page_range = range(config['page_start'], config['page_end'])
    for i in page_range:
        r = get_html_info(i, config['mode'], config['search_keyword'])
        get_pic(r, save_dir, log_file, config)
        print(f'===============第{i}页下载完毕=============')
    
    print(f'爬取完成！日志已保存到: {log_file}')
        
if __name__ == '__main__':
    main()