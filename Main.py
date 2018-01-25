import FTP_SFTP_Client
import myLogger
import makeWar
import MySVN
import changeFiles
import time


def main(target_server):
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
    start_time = time.time()
    # target = 'prd'
    target = target_server.lower()
    path = 'D:\Data\menuCeter_web'
    my_svn = MySVN.McSVN()
    cf = changeFiles.ChangeFiles(target, path)
    if target == 'uat':
        myLog.info("target server is {}".format(target_server))
        my_svn.mc_update()
        cf.change_file_uat()
    elif target == 'prd':
        myLog.info("target server is {}".format(target_server))
        my_svn.mc_update()
        cf.change_file_prd()
    else:
        print("请确认打包环境,[uat] or [prd]")
        myLog.info("输入参数 {} 有误.".format(target_server))
        exit(0)
    mw = makeWar.CrateWar(path, target)
    mw.make_war()
    update_uat = input("\nupdate uat: [y/n]: ")
    if update_uat.lower() == 'y':
        # sftp = SFTPClient.SftpClient()
        update_57 = input("update 57 ? [y/n]: ")
        if update_57.lower() == 'y':
            ftp.upload_to_57()
            myLog.info("57 updated.")
            print("57 updated")
        time.sleep(3)
        update_201 = input("update 201? [y/n]: ")
        if update_201.lower() == 'y':
            ftp.upload_to_201()
            myLog.info("201 updated.")
            print("201 updated")
        time.sleep(3)
        update_202 = input("update 202 ?[y/n]: ")
        if update_202.lower() == 'y':
            ftp.upload_to_202()
            myLog.info("202 updated.")
            print("202 updated.")
    else:
        myLog.info("no update")
        print("no update.")
    end_time = time.time()
    myLog.info("success, 用时 {}s".format(str(end_time - start_time)))


if __name__ == '__main__':
    server = input('请输入要打包的对应Server [uat/prd]: ')
    main(server.lower())
