import FTP_SFTP_Client
import myLogger

ftp = FTP_SFTP_Client.FTPClient()
print("download war from jenkins server ...")
ftp.conn_jenkins()
print("重命名 WAR 包.")
ftp.rename_war()
print("备份 war 包")
ftp.copy_to_backup()

myLog = myLogger.MyLogger().mylogging()
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
    myLog.log("no update")
    print("no update.")

