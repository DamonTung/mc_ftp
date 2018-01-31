import FTP_SFTP_Client
import myLogger
import makeWar
import MySVN
import changeFiles
import time
from multiprocessing import Process as process


def main(target_server,myLog,ftp):

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
    update_source = input("是否从SVN更新本地代码[Y/N]?")
    if update_source.lower() == 'y':
        myLog.info("====== 开始从SVN更新源码======")
        my_svn.mc_update(target)
        myLog.info("====== 源码更新完毕 ======")
    if target == 'pro' or target == 'mobile':
        my_svn.mc_update(target)
        cf.change_file_prd()
    '''
    if target in('uat', 'mbrand', 'prepro'):
        my_svn.mc_update(target)
        # cf.change_file_uat()
    elif target == 'pro':
        # myLog.info("target server is {}".format(target_server))
        my_svn.mc_update(target)
        cf.change_file_prd()
    elif target == 'mobile' or target == 'dev':
        # myLog.info("target server is {}".format(target_server))
        my_svn.mc_update(target)
    else:
        print("请确认打包环境,[uat][pro][dev][mobile][mbrand][prepro]")
        myLog.info("输入参数 {} 有误.".format(target_server))
        exit(0)
        '''
    mw = makeWar.CrateWar(path, target)
    mw.make_war()
    if target == 'pro' or target == 'mobile':
        return
    update_uat = input("\ndeploy to server: [y/n]: ")
    if update_uat.lower() == 'y' and target == 'uat':
        # sftp = SFTPClient.SftpClient()
        update_57 = input("update 57 ? [y/n]: ")
        if update_57.lower() == 'y':
            deploy_to_57(ftp, myLog)
            # p_57 = process(target=deploy_to_57, args=(ftp, myLog))
            # print("child process start..")
            # p_57.start()
            # print("child process end..")

    if update_uat.lower() == 'y' and target == 'mbrand':
        update_201 = input("update 201? [y/n]: ")
        if update_201.lower() == 'y':
            deploy_to_201(ftp,myLog)
            # p_201 = process(target=deploy_to_201,args=(ftp, myLog))
            # p_201.start()

    if update_uat.lower() == 'y' and target == 'prepro':
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
    myLog = myLogger.MyLogger().mylogging()
    ftp = FTP_SFTP_Client.FTPClient()
    servers = input('Deploy Server [uat][pro][dev][mobile][mbrand][prepro]: ').split()
    myLog.info(servers)
    for server in servers:
        main(server.lower(), myLog, ftp)

