import pysvn
import myLogger
import base64
import os


class McSVN:
    def __init__(self):
        self.name = "svn"
        self.mc_web_remote = 'svn://15.107.29.25/trunk/40. CUT/40.10 SRC/menuCenter_web/trunk'
        self.mc_web_local = 'D:\Data\menuCeter_web'
        self.client = pysvn.Client()
        self.logging = myLogger.MyLogger().mylogging()
        self.svn_name = base64.b64decode('ZG9uZ2d1YW5nemhlbg==')
        self.svn_pass = base64.b64decode('ZG9uZ2d1YW5nemhlbg==')

        def callback_get_login(realm, username, may_save):
            name = 'dongguangzhen'
            password = 'dongguangzhen'
            return True, name, password, True

        self.client.callback_get_login = callback_get_login

    def get_login(realm, username, may_save):
        retcode = True
        username = base64.b64decode('ZG9uZ2d1YW5nemhlbg==')
        password = base64.b64decode('ZG9uZ2d1YW5nemhlbg==')
        save = True
        return retcode, username, password, save

    def check_out(self):
        self.logging.info("check out from {} to {} ".format(self.mc_web_remote, self.mc_web_local))
        self.client.checkout(self.mc_web_remote, self.mc_web_local)
        self.logging.info("check out finished.")

    def mc_update(self, target):
        self.logging.info("update menuCenter_web")
        if not os.path.exists(self.mc_web_local):
            self.check_out()
        headrev_curr = self.client.info(self.mc_web_local).revision.number
        self.logging.info("Current Head Revision: " + str(headrev_curr))
        if target in ('uat','prepro','mbrand'):
            self.client.update(self.mc_web_local)
            self.check_revision_after_update(headrev_curr)
        elif target == 'pro':
            self.logging.info("Revision: {},path: {}".format(headrev_curr, 'D:\Data\YumWar\product\config\\bak\\revision'))
            rev = open('D:\Data\YumWar\product\config\\bak\\revision.log', 'w')
            rev.write(str(headrev_curr))
            rev.flush()
            rev.close()
        else:
            self.client.update(self.mc_web_local)
            self.check_revision_after_update(headrev_curr)

    def check_revision_after_update(self, headrev_curr):
        headrev_after = self.client.info(self.mc_web_local).revision.number
        self.logging.info("updated.")
        self.logging.info("updated records: ")
        self.logging.info(self.client.diff_summarize(
            url_or_path1=self.mc_web_remote,
            revision1=pysvn.Revision(pysvn.opt_revision_kind.number, headrev_curr),
            url_or_path2=self.mc_web_remote,
            revision2=pysvn.Revision(pysvn.opt_revision_kind.number, headrev_after),
            recurse=True, ignore_ancestry=False))
        self.logging.info("updated Head Revision: " + str(headrev_after))

    def get_changes(self):
        changes = self.client.status(self.mc_web_local)
        self.logging.info('files to be added:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.added])
        self.logging.info('files to be removed:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.deleted])
        self.logging.info('files that have changed:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.modified])
        self.logging.info('files with merge conflicts:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.conflicted])
        self.logging.info('unversioned files:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.unversioned])




