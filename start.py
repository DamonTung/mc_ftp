import FtpClient

ftp = FtpClient.FTPClient()
print("download war from jenkins server ...")
ftp.conn_jenkins()
update_uat = input("\nupdate uat: [y/n]: ")
if update_uat == 'y':
    # sftp = SFTPClient.SftpClient()
    update_57 = input("update 57 ? [y/n]: ")
    if update_57 == 'y':
        ftp.upload_to_57()
        print("57 updated")
    update_201 = input("update 201? [y/n]: ")
    if update_201 == 'y':
        ftp.upload_to_201()
        print("201 updated")
    update_202 = input("update 202 ?[y/n]: ")
    if update_202 == 'y':
        ftp.upload_to_202()
        print("202 updated.")
else:
    print("no update.")

