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
        mydict = {}
        mydict['host'] = self.cp.get('jenkins', 'host_ip')
        mydict['port'] = self.cp.getint('jenkins', 'host_port')
        mydict['username'] = self.cp.get('jenkins', 'username')
        mydict['password'] = self.cp.get('jenkins', 'password')
        mydict['remote_dir'] = self.cp.get('jenkins', 'remote_dir')
        return mydict

    def host_201(self):
        host_201 = self.cp.items('mc_201')
        mydict = {}
        mydict['host'] = self.cp.get('mc_201', 'host_ip')
        mydict['port'] = self.cp.getint('mc_201', 'host_port')
        mydict['username'] = self.cp.get('mc_201', 'username')
        mydict['password'] = self.cp.get('mc_201', 'password')
        mydict['remote_dir'] = self.cp.get('mc_201', 'remote_dir')
        return mydict

    def host_202(self):
        host_202 = self.cp.items('mc_202')
        mydict = {}
        mydict['host'] = self.cp.get('mc_202', 'host_ip')
        mydict['port'] = self.cp.getint('mc_202', 'host_port')
        mydict['username'] = self.cp.get('mc_202', 'username')
        mydict['password'] = self.cp.get('mc_202', 'password')
        mydict['remote_dir'] = self.cp.get('mc_202', 'remote_dir')
        return mydict

    def host_57(self):
        mydict = {}
        mydict['host'] = self.cp.get('mc_57', 'host_ip')
        mydict['port'] = self.cp.getint('mc_57', 'host_port')
        mydict['username'] = self.cp.get('mc_57', 'username')
        mydict['password'] = self.cp.get('mc_57', 'password')
        mydict['remote_dir'] = self.cp.get('mc_57', 'remote_dir')
        return mydict
