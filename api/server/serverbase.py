from api.network import network
from abc import ABCMeta, abstractmethod


class serverbase(metaclass=ABCMeta):
    host = None
    userid = None
    key = None
    headers = None
    err = None
    client = None

    @abstractmethod
    def __init__(self, host : str, userid : str, key : str) -> None:
        """
        :param host
        :param userid
        :param key
        """
        self.host = host
        self.userid = userid
        self.key = key
        self.headers = {'Content-Type':'application/json'}
        self.client = network(maxnumconnect=10, maxnumcache=20)
    
    @abstractmethod
    def get_items(self, parentid : str = ''):
        """
        获取项目列表
        :param parentid 父文件夹ID
        :return True or False, items
        """
        pass

    @abstractmethod
    def get_items_count(self):
        """
        获取项目数量
        :return True or False, iteminfo
        """
        pass

    @abstractmethod
    def get_item_info(self, itemid : str):
        """
        获取项目
        :param itemid 项目ID
        :return True or False, iteminfo
        """
        pass

    @abstractmethod
    def set_item_info(self, itemid : str, iteminfo):
        """
        更新项目
        :param iteminfo 项目信息
        :return True or False, iteminfo
        """
        pass

    @abstractmethod
    def set_item_image(self, itemid : str, imageurl : str):
        """
        更新项目图片
        :param imageurl 图片URL
        :return True or False
        """
        pass

    @abstractmethod
    def search_movie(self, itemid, tmdbid):
        """
        搜索视频
        :param itemid 项目ID
        :param tmdbid TMDB ID
        :return True or False, iteminfo
        """
        pass

    @abstractmethod  
    def apply_search(self, itemid, iteminfo):
        """
        应用搜索
        :param itemid 项目ID
        :param iteminfo 项目信息
        :return True or False
        """
        pass

    @abstractmethod  
    def refresh(self, itemid):
        """
        刷新元数据
        :param itemid 项目ID
        :return True or False
        """

    @abstractmethod
    def __get_status__(self, p, err):
        pass