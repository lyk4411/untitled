from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import requests
def get(url):
    r=requests.get(url)
    return {'url':url,'text':r.text}
def parse(future):
    dic=future.result()          #future对象调用result方法取其值、
    print(dic)
    f=open('db.text','a')
    date='url:%s\n'%len(dic['text'])
    f.write(date)
    f.close()
if __name__ == '__main__':
    executor=ThreadPoolExecutor()
    url_l = ['http://cn.bing.com/', 'http://www.cnblogs.com/wupeiqi/', 'http://www.cnblogs.com/654321cc/',
                 'https://www.cnblogs.com/', 'http://society.people.com.cn/n1/2017/1012/c1008-29581930.html',
                 'http://www.xilu.com/news/shaonianxinzangyou5gedong.html', ]
    futures=[]
    for url in url_l:
        executor.submit(get,url).add_done_callback(parse)         #与Pool进程池回调函数接收的是A函数的返回值(对象ApplyResult.get()得到的值)。
    executor.shutdown()                                           #这里回调函数parse，接收的参数是submit生成的 Future对象。
    print('主')