import Config
import pysftp
import os


class SftpClient:

    def __init__(self):
        self.filename_local = "menuCenter.war"
        self.config = Config.Env()
        self.local_dir = self.config.local_env()
        print("local path: " + self.local_dir)
        os.chdir(self.local_dir)

    def upload_to_201(self):
        mc_201 = self.config.host_201()
        hosts = mc_201['host']
        port = mc_201['port']
        username = mc_201['username']
        password = mc_201['password']
        remote_dir = mc_201['remote_dir']
        print(mc_201)
        self.upload(hosts, username, password, port, remote_dir)

    def upload_to_202(self):
        mc_202 = self.config.host_202()
        hosts = mc_202['host']
        port = mc_202['port']
        username = mc_202['username']
        password = mc_202['password']
        remote_dir = mc_202['remote_dir']
        print(mc_202)
        self.upload(hosts, username, password, port, remote_dir)

    def upload_to_57(self):
        mc_57 = self.config.host_57()
        hosts = mc_57['host']
        port = mc_57['port']
        username = mc_57['username']
        password = mc_57['password']
        remote_dir = mc_57['remote_dir']
        print(mc_57)
        self.upload(hosts, username, password, port, remote_dir)

    def upload(self, hosts, username, password, port, remote_dir):
        with pysftp.Connection(host=hosts, username=username, password=password, port=port, default_path=remote_dir) as sftp:
            #sftp.chdir(remote_dir)
            print("current path: " + sftp.pwd)
            #sftp.put(self.filename_local)
            print("上传成功!")