from ftplib import FTP
import Config
import os
import shutil
import pysftp


class FTPClient:

    def __init__(self):
        self.filename = "menuCenter_web-0.0.1-SNAPSHOT.war"
        self.filename_local = "menuCenter.war"
        self.config = Config.Env()
        self.ftp = FTP()
        self.ftp.set_debuglevel(2)
        self.local_dir = self.config.local_env()
        if os.path.notexists(self.local_dir):
            os.mkdir(self.local_dir, 'wr')
            os.chdir(self.local_dir)
        else:
            os.chdir(self.local_dir)
        print("current workspace: " + self.local_dir)

    def conn_jenkins(self):
        jenkins = self.config.host_jenkins()
        hosts = jenkins['host']
        port = jenkins['port']
        username = jenkins['username']
        password = jenkins['password']
        dir = jenkins['remote_dir']
        self.ftp.connect(hosts, port, 3000)
        self.ftp.login(username, password)
        print (self.ftp.getwelcome())
        self.ftp.cwd(dir)
        self.ftp.nlst()
        file_handle = open(self.filename, 'wb')
        print ("start downloading...")
        self.ftp.retrbinary("RETR " + self.filename, file_handle.write, 1024)
        self.ftp.set_debuglevel(0)
        self.ftp.close()
        print("download complete...")
        print("path: " + self.local_dir)
        shutil.copyfile(self.filename, self.filename_local)
        print("copy " + self.filename + "  to " + self.filename_local)

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
            print("current path: " + sftp.pwd)
            sftp.put(self.filename_local)
            print("上传成功!")

