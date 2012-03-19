# -*- coding: utf-8 -*-

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.
    
    @author: cytec
    @interface-version: 0.1
"""

from os import makedirs
from os import listdir
from os.path import exists
from os.path import join
from os.path import isfile
from shutil import move
import time
import twitter
import re

from module.plugins.Hook import Hook
from module.Api import Api
class pyBurn(Hook):
    __name__ = "pyBurn"
    __version__ = "0.1"
    __description__ = """Control pyLoad via Twitter and other cool stuff"""
    __config__ = [ ("activated", "bool", "Activated" , "False"),
                    ("twinterval", "int", "Interval", "10"),
                    ("UserWhitelist", "str", "DM Whitelist", "YOUR USER NAME"),
                    ("whiteUserOnly", "bool", "Use DM Whitelist", "False"),
                    ("twitresponse", "bool", "Twitter Response", "False"),
                    ("twitify", "bool", "Twitter Notify", "False"),
                    ("twitifyFile", "bool", "Twitter Notify for every File", "False"),
                    ("twitifyDM", "bool", "Use DM for Notify", "True"),
                    ("twitifyUser", "str", "Twitter Notify User", "YOUR USER NAME")]
    __threaded__ = []
    __author_name__ = ("cytec")
    __author_mail__ = ("iamcytec@googlemail.com")
    
    def setup(self):
        self.interval = self.getConfig('twinterval')

    def periodical(self):
        api = twitter.Api(consumer_key='**', consumer_secret='**', access_token_key='**', access_token_secret='**')
        self.logDebug("Getting DirectMessages from Twitter")
        messages = api.GetDirectMessages()
        if self.getConfig('whiteUserOnly'):
            self.logDebug("Useing Whitelist Filter for DMs")
            self.logDebug("Whitelisted User(s) %s" % (self.getConfig('UserWhitelist')) ) 
        for dm in messages:
            fromUser = dm.sender_screen_name
            if self.getConfig('whiteUserOnly'):
                if fromUser in self.getConfig('UserWhitelist'):
                    dmcontent = dm.text
                    self.logDebug("Message from: %s with text: %s" % (fromUser, dmcontent))
                else:
                    dmcontent = "User @%s not in whitelist..." % (fromUser)
                    self.logDebug("User @%s not in whitelist..." % (fromUser))
            else:
                dmcontent = dm.text
                self.logDebug("Message from: %s with text: %s" % (fromUser, dmcontent))
            splitDM = dmcontent.split()
            if splitDM[0].lower() == "addlink" or splitDM[0].lower() == "addlinks":
                splitDM.remove(splitDM[0])
                if splitDM[0].startswith('http'):
                    pkgname = "Twitter_%s_%s" % (fromUser, time.strftime("%H-%M-%S_%d%b%Y"))
                    self.core.api.addPackage(pkgname, splitDM, 1)
                else:
                    pkgname = splitDM[0]
                    splitDM.remove(splitDM[0])
                    self.core.api.addPackage(pkgname, splitDM, 1)
                #for link in splitDM:
                self.logInfo("Added: %s Links to Package: %s" % (len(splitDM), pkgname))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))
                if self.getConfig('twitresponse'):
                    if self.getConfig('twitifyUser') != "YOUR USER NAME" or self.getConfig('twitifyUser') != "" or self.getConfig('twitifyUser') != " ":
                        twitifyUser = self.getConfig('twitifyUser')
                    else:
                        twitifyUser = fromUser
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "Added: %s Links to Package: %s" % (len(splitDM), pkgname))
                        self.logDebug("DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s Added: %s Links to Package: %s" % (twitifyUser, len(splitDM), pkgname))
                        self.logDebug("Note send to @%s" % (twitifyUser))
            
            if splitDM[0].lower() == "status":
                status = self.core.api.statusServer()
                self.logDebug(status)
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, status)
                        self.logDebug("Status DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s %s" % (twitifyUser, status))
                        self.logDebug("Status Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))

            if splitDM[0].lower() == "restart":
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "Restarting...")
                        self.logDebug("Restart DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s Restarting..." % (twitifyUser))
                        self.logDebug("Restart Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))
                self.core.api.restart()

            if splitDM[0].lower() == "shutdown":
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "good by sir...")
                        self.logDebug("Shoutdown DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s good bye sir..." % (twitifyUser))
                        self.logDebug("Shoutdown Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))
                self.core.api.kill()

            if splitDM[0].lower() == "help":
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "Need Help? my commands: addlinks NAME LINK, status, restart, shutdown, version, about")
                        self.logDebug("Help DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s Need Help? my commands: addlinks NAME LINK, status, restart, shutdown, version, about" % (twitifyUser))
                        self.logDebug("Help Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))

            if splitDM[0].lower() == "about":
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "pyBurn Version: %s created by cytec, @icytec more info: https://github.com/cytec/pyBurn – use help for list of commands" % (self.__version__))
                        self.logDebug("Help DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s pyBurn Version: %s created by cytec, @icytec more info: https://github.com/cytec/pyBurn – use help for list of commands" % (self.__version__))
                        self.logDebug("Help Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))

            if splitDM[0].lower() == "version":
                pyVersion = self.core.api.getServerVersion()
                if self.getConfig('twitify'):
                    twitifyUser = self.getConfig('twitifyUser')
                    if self.getConfig('twitifyDM'):
                        api.PostDirectMessage(twitifyUser, "Im Running pyLoad: %s with pyBurn: %s" % (pyVersion, self.__version__))
                        self.logDebug("Help DM send to %s" % (twitifyUser))
                    else:
                        api.PostUpdate("@%s Im Running pyLoad: %s with pyBurn: %s" % (pyVersion, self.__version__))
                        self.logDebug("Help Note send to @%s" % (twitifyUser))
                api.DestroyDirectMessage(dm.id)
                self.logDebug("Deleted: DM with id %s and text: %s from User: %s" % (dm.id, dm.text, fromUser))



    def downloadFinished(self, pyfile):
        if self.getConfig('twitifyFile'):
            if self.getConfig('twitifyUser'):
                twitifyUser = self.getConfig('twitifyUser')
                api = twitter.Api(consumer_key='**', consumer_secret='**', access_token_key='**', access_token_secret='**')
                api.PostDirectMessage(twitifyUser, "Download of File: %s finished" % (pyfile.name))
                self.logDebug("Note send to @%s" % (twitifyUser))
            else:
                self.logError("Please set User to Notify in Settings")

    def packageFinished(self, pypack):
        if self.getConfig('twitify'):
            if self.getConfig('twitifyUser'):
                twitifyUser = self.getConfig('twitifyUser')
                api = twitter.Api(consumer_key='**', consumer_secret='**', access_token_key='**', access_token_secret='**')
                api.PostDirectMessage(twitifyUser, "Download of Package: %s finished" % (pypack.name))
                self.logDebug("Note send to @%s" % (twitifyUser))
            else:
                self.logError("Please set User to Notify in Settings")

    def allDownloadsFinished(self):
        if self.getConfig('twitify'):
            if self.getConfig('twitifyUser'):
                twitifyUser = self.getConfig('twitifyUser')
                api = twitter.Api(consumer_key='**', consumer_secret='**', access_token_key='**', access_token_secret='**')
                api.PostDirectMessage(twitifyUser, "All current downloads finished")
                self.logDebug("Note send to @%s" % (twitifyUser))
            else:
                self.logError("Please set User to Notify in Settings")


