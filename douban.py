import requests
import urllib
from urllib import request

start_list=[]
# you can revise the range of the url
for i in range(0, 2):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=' + str(i*20)
    start_list.append(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0'

image_list=[]

def get_json(url):
    '''
    :param url: the url of you want to crawl
    :return: json
    '''

    try:
        r = requests.get(url, headers=headers,timeout = 2)
        r.encoding = 'utf-8'
        if 200 == r.status_code:
            # print(r.json())
            rr = r.json()
            return rr
    except requests.ConnectionError:
        print(" ConnectionError")


def get_images(json):
    '''
    :param json: input the json fomat you have been saved
    :return: image list of the url
    '''
    if json.get('subjects'):
        data = json.get('subjects')
        for item in data:
            if item.get('cover') is None:
                continue
            images = item.get('cover')
            image_list.append(images)
        return image_list
    else:
        print("There is no subjects!")

def save_images(image_list):
    '''
    :param image_list: input the image list of the url
    :return: None
    '''
    for image_url in image_list:
        urllib.request.urlretrieve(image_url, filename=dirname + str(image_list.index(image_url)) + '.jpg')

if __name__ == '__main__':

    dirname = '/Users/zhangyujuan/Downloads/douban_pics-master/douban_movies/tutorial/Image_Douban/'

    for url in start_list:
        html = get_json(url)
        image_lists = get_images(html)
        save_images(image_lists)
