import FTP_SFTP_Client
import myLogger
import makeWar
import MySVN
import changeFiles
import time
from multiprocessing import Process as process


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
    myLog.info("target server is {}".format(target_server))
    if target == 'uat':
        my_svn.mc_update(target)
        # cf.change_file_uat()
    elif target == 'pro':
        # myLog.info("target server is {}".format(target_server))
        my_svn.mc_update(target)
        cf.change_file_prd()
    elif target == 'mobile' or target == 'dev' or target =='mbrand':
        # myLog.info("target server is {}".format(target_server))
        my_svn.mc_update(target)
    else:
        print("请确认打包环境,[uat][pro][dev][mobile][mbrand][prepro]")
        myLog.info("输入参数 {} 有误.".format(target_server))
        exit(0)
    mw = makeWar.CrateWar(path, target)
    mw.make_war()
    if target == 'pro' or target == 'mobile':
        return
    update_uat = input("\nupdate uat: [y/n]: ")
    if update_uat.lower() == 'y':
        # sftp = SFTPClient.SftpClient()
        update_57 = input("update 57 ? [y/n]: ")
        if update_57.lower() == 'y':
            deploy_to_57(ftp, myLog)
            # p_57 = process(target=deploy_to_57, args=(ftp, myLog))
            # print("child process start..")
            # p_57.start()
            # print("child process end..")
        time.sleep(3)
        update_201 = input("update 201? [y/n]: ")
        if update_201.lower() == 'y':
            deploy_to_201(ftp,myLog)
            # p_201 = process(target=deploy_to_201,args=(ftp, myLog))
            # p_201.start()
        time.sleep(3)
        update_202 = input("update 202 ?[y/n]: ")
        if update_202.lower() == 'y':
            deploy_to_202(ftp, myLog)
            # p_202 = process(target=deploy_to_202,args=(ftp, myLog))
            # p_202.start()
    else:
        myLog.info("no update")
        print("no update.")
    end_time = time.time()
    myLog.info("success, 用时 {}s".format(str(end_time - start_time)))


def deploy_to_202(ftp, myLog):
    ftp.upload_to_202()
    myLog.info("202 updated.")
    print("202 updated.")


def deploy_to_201(ftp, myLog):
    ftp.upload_to_201()
    myLog.info("201 updated.")
    print("201 updated")


def deploy_to_57(ftp, myLog):
    ftp.upload_to_57()
    myLog.info("57 updated.")
    print("57 updated")


if __name__ == '__main__':
    server = input('Deploy Server [uat][pro][dev][mobile][mbrand][prepro]: ')
    main(server.lower())
