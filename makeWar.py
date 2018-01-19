import os, time
import shutil
import myLogger

class CrateWar:

    def __init__(self, path):
        self.name = "Make war"
        self.path = path
        self.logging = myLogger.MyLogger().mylogging()
        self.target_path = '\\target\menuCenter_web-0.0.1-SNAPSHOT.war'
        self.target_name = "menuCenter_web-0.0.1-SNAPSHOT.war"
        self.file_name = 'menuCenter.war'

    def make_war(self):
        os.chdir(self.path)
        os.system('mvn clean install')
        self.logging.info("created new war [mvn clean install]")

    def copy_to_backup(self):
        os.chdir(self.path)
        shutil.copy2(self.path + self.target_path, self.file_name)
        local_time = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
        os.chdir('D:\Data\YumWar')
        if not os.path.exists(local_time):
            os.mkdir(local_time)
            os.chdir(self.path)
            shutil.copy2(self.file_name, 'D:\Data\YumWar\\'+local_time + '\menuCenter.war')
            self.logging.info("war 包备份至: " + os.getcwd() + "\\" + local_time)
            shutil.copy2(self.file_name,'D:\Data\YumWar\\uat\\'+self.file_name)
