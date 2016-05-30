from multiprocessing import Pool
from parsing_web import get_items_from,get_items_info
from channels_url import channels_url

#channels_url=['http://bj.ganji.com/shouji/']


if __name__=='__main__':
    pool=Pool(processes=6)
    pool.map(get_items_from,channels_url)
    pool.close()
    pool.join()
