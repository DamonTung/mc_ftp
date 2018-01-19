import getLog

gl = getLog.GetLogFromServer()
'''目前生产环境通过此方法连接不上'''
print("请输入要获取log的server: 57 / 201/ 202/ [prd nan hui .12] 8212/ "
      "[prd nan hui .9]829 / [zhen ru .12]6212/ [zhen ru .9]629")
print("目前生产环境通过此方法连接不上,有效的输入信息只接受57/201/202:")
server = input("请输入以上对应的数字[57][201][202]:\n ")
print("server is {}".format(str(server)))
if server == '57':
    gl.log_57()
    print("download from 57")
if server == '201':
    gl.log_201()
if server == '202':
    gl.log_202()

'''
if server == '8212':
    gl.log_prd_82_12()
if server == '829':
    gl.log_prd_82_9()
if server == '6212':
    gl.log_prd_62_12()
if server == '629':
    gl.log_prd_62_9()
'''