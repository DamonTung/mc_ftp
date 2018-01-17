import Config
import myLogger
import pysftp
import os
import shutil


class GetLogFromServer:

    def __init__(self):
        self.config = Config.Env()
        self.local_log = 'D:\Data\YumWar\log'
        self.logging = myLogger.MyLogger().mylogging()

    def log_201(self):
        dict_201 = self.config.host_201()
        self.get_log_from_server(dict_201)

    def log_202(self):
        dict_202 = self.config.host_202()
        self.get_log_from_server(dict_202)

    def log_57(self):
        dict_57 = self.config.host_57()
        self.get_log_from_server(dict_57)

    def log_prd_82_12(self):
        dict_82_12 = self.config.host_prd_nh_12()
        self.get_log_from_server(dict_82_12)

    def log_prd_82_9(self):
        dict_82_9 = self.config.host_prd_nh_9()
        self.get_log_from_server(dict_82_9)

    def log_prd_62_12(self):
        dict_62_12 = self.config.host_prd_zr_12()
        self.get_log_from_server(dict_62_12)

    def log_prd_62_9(self):
        dict_62_9 = self.config.host_prd_zr_9()
        self.get_log_from_server(dict_62_9)

    def get_log_from_server(self, my_dict):
        print(my_dict)
        host = my_dict['host']
        password = my_dict['password']
        username = my_dict['username']
        port = my_dict['port']
        log_dir = my_dict['log_dir']
        os.chdir('D:\Data\YumWar\log')
        with pysftp.Connection(host=host, username=username, password=password, port=port, default_path=log_dir) as sftp:
            sftp.get('server.log')
            self.logging.info("download log from server: {}".format(host))
            sftp.close()
            shutil.copy2('server.log', 'server.{}.log'.format(host))
            self.logging.info("sftp closed")
