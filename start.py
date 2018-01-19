import FTP_SFTP_Client
import myLogger
import makeWar
import MySVN
import changeFiles

myLog = myLogger.MyLogger().mylogging()
ftp = FTP_SFTP_Client.FTPClient()
''' ## 方式一 从jenkins 服务器拉取War包
myLog.info("download war from jenkins server ...")
ftp.conn_jenkins()
myLog.info("重命名 WAR 包.")
ftp.rename_war()
myLog.info("备份 war 包")
ftp.copy_to_backup()
myLog.info("替换ESBClient.xml")
ftp.change_ESBClient_xml()
myLog.info("准备上传UAT...")
'''

''' 方式二 pysvn 拉取代码,本地打包
'''

target = 'uat'
cf = changeFiles.ChangeFiles()
if target == 'uat':
    my_svn = MySVN.McSVN()
    my_svn.mc_update()
    cf.change_file_uat()
elif target == 'prd':
    cf.change_file_prd()

mw = makeWar.CrateWar()
mw.make_war()

update_uat = input("\nupdate uat: [y/n]: ")

if update_uat == 'y':
    # sftp = SFTPClient.SftpClient()
    update_57 = input("update 57 ? [y/n]: ")
    if update_57 == 'y':
        ftp.upload_to_57()
        myLog.info("57 updated.")
        print("57 updated")
    update_201 = input("update 201? [y/n]: ")
    if update_201 == 'y':
        ftp.upload_to_201()
        myLog.info("201 updated.")
        print("201 updated")
    update_202 = input("update 202 ?[y/n]: ")
    if update_202 == 'y':
        ftp.upload_to_202()
        myLog.info("202 updated.")
        print("202 updated.")
else:
    myLog.info("no update")
    print("no update.")

