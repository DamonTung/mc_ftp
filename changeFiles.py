import  os, shutil
import myLogger

class ChangeFiles:

    def __init__(self, server, path):
        self.target = server
        self.logging = myLogger.MyLogger().mylogging()
        self.esbclient_xml = 'D:\Data\YumWar\\uat\ESBClient\\UAT_ESBclient\ESBClient.xml'
        self.resource_path = 'src\main\\resources\\'
        self.config_path = 'src\main\\resources\config\\'
        self.lib_path = 'src\main\webapp\WEB-INF\lib\\'
        self.changed_files_prd_path = 'D:\Data\YumWar\product\destFiles\\'
        self.path = path

    def change_file_prd(self):
        # -- classes/config
        FILE_JDBC_PROPERTIES = 'jdbc.properties'
        FILE_REDIS_CONFIG_PROPERTIES = 'redisConfig.properties'
        FILE_DS_NEW_CONFIG_PROPERTIES = 'DS_NEW_CONFIG.properties'
        # -- classes
        FILE_ESBCLIENT_XML = 'ESBClient.xml'
        FILE_LOG_BACK_XML = 'logback.xml'

        LIB_OAUTH_SDK = 'yum-oauth2-sdk4prod.jar'
        LIB_MESSAGECENTER_CLIENT = 'MessageCenter_client-1.1.2.jar'
        LIB_MESSAGECENTER_CLIENT_REMOVE = 'MessageCenter_client-1.1.1.jar'
        LIB_REMOVE_TEST = 'yum-oauth2-sdk4test.jar'

        file_list = {FILE_ESBCLIENT_XML, FILE_LOG_BACK_XML}
        file_list_config = {FILE_DS_NEW_CONFIG_PROPERTIES, FILE_JDBC_PROPERTIES, FILE_REDIS_CONFIG_PROPERTIES}
        lib_list = {LIB_OAUTH_SDK, LIB_MESSAGECENTER_CLIENT}
        lib_list_remove = {LIB_MESSAGECENTER_CLIENT_REMOVE, LIB_REMOVE_TEST}
        os.chdir(self.path)
        # --- 替换配置文件
        for file in self.file_list:
            sourceFile = self.changed_files_prd_path + file
            destFile = self.resource_path + file
            if os.path.isfile(sourceFile):
                self.logging.info("文件替换： src: %s -> dest: %s " % (sourceFile, destFile))
                shutil.copyfile(sourceFile, destFile)

        # --- 替换配置文件
        for file in self.file_list_config:
            sourceFile = self.changed_files_prd_path + file
            destFile = self.config_path + file
            if os.path.isfile(sourceFile):
                self.logging.info("文件替换： src: %s -> dest: %s " % (sourceFile, destFile))
                shutil.copyfile(sourceFile, destFile)
        # --- 替换 jar文件
        for fileJar in self.lib_list:
            sourceJar = self.changed_files_prd_path + fileJar
            destJar = self.lib_path + fileJar
            if os.path.isfile(sourceJar):
                self.logging.info("jar 包替换： src: %s -> dest: %s" % (sourceJar, destJar))
                print("jar 包替换： src: %s -> dest: %s" % (sourceJar, destJar))
                shutil.copyfile(sourceJar, destJar)

        # --- 删除jar包
        for fileJar in self.lib_list_remove:
            filename = self.lib_path + fileJar
            if os.path.isfile(filename):
                self.logging.info("删除 jar 包： %s " % filename)
                print("删除 jar 包： %s " % filename)
                os.remove(filename)

    def change_file_uat(self):
        os.chdir(self.path)
        shutil.copy2(self.esbclient_xml, self.resource_path+'ESBClient.xml')
        self.logging.info("changed ESBClient.xml from {} to {} ".format(self.esbclient_xml, self.resource_path))

