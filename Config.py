import configparser
import json


class Env:

    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.cp.read(".\config\config.ini")
        self.secs = self.cp.sections()

    def local_env(self):
        local_path = self.cp.get('local_path', 'local_dir')
        return local_path

    def host_jenkins(self):
        dict['host'] = self.cp.get('jenkins', 'host_ip')
        dict['port'] = self.cp.getint('jenkins', 'host_port')
        dict['username'] = self.cp.get('jenkins', 'username')
        dict['password'] = self.cp.get('jenkins', 'password')
        dict['remote_dir'] = self.cp.get('jenkins','remote_dir')
        return dict

    def host_201(self):
        host_201 = self.cp.items('mc_201')
        dict = {}
        dict['host'] = self.cp.get('mc_201', 'host_ip')
        dict['port'] = self.cp.getint('mc_201', 'host_port')
        dict['username'] = self.cp.get('mc_201', 'username')
        dict['password'] = self.cp.get('mc_201', 'password')
        dict['remote_dir'] = self.cp.get('mc_201', 'remote_dir')
        return dict

    def host_202(self):
        host_202 = self.cp.items('mc_202')
        dict = {}
        dict['host'] = self.cp.get('mc_202', 'host_ip')
        dict['port'] = self.cp.getint('mc_202', 'host_port')
        dict['username'] = self.cp.get('mc_202', 'username')
        dict['password'] = self.cp.get('mc_202', 'password')
        dict['remote_dir'] = self.cp.get('mc_202', 'remote_dir')
        return dict

    def host_57(self):
        dict = {}
        dict['host'] = self.cp.get('mc_57', 'host_ip')
        dict['port'] = self.cp.getint('mc_57', 'host_port')
        dict['username'] = self.cp.get('mc_57', 'username')
        dict['password'] = self.cp.get('mc_57', 'password')
        dict['remote_dir'] = self.cp.get('mc_57', 'remote_dir')
        return dict
