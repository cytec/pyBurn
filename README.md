# pyBurn

ive rewritten my bash scripts to python... yeah!
so now pyBurn is a hook for pyLoad itself.

## NOTE!
Currently this is in heavy development.<br />
So if you like to test, feel free to do so but notice that this is still a verry early version <br />

## Current features:

**Add new Links over Twitter**<br />
Usage: AddLinks {CONTAINERNAME} LINK LINK LINK<br />
If no Containername it generates one based on DM Sendername and Date.<br />
<br />
**Twitter Response**<br />
Activate the Twitter Response Options in the Settings and pyBurn will send you either an DM or an @ reply after adding the links from your AddLinks command.

**Twitter Commands**<br />
status: returns the current status<br />
help: list of commands<br />
version: display pyLoad and pyBurn version<br />
about: some infos about pyBurn<br />
restart: restart pyLoad<br />
shoutdown: shoutdown pyLoad<br />


##Requiers:

* pyLoad
* python-twitter
* twitter API keys (http://twitter.com/apps)

## How To:

Install pyLoad.

Install python-twitter

go to http://twitter.com/apps and create an app, be sure you select DM access under rights.

**Download pyBurn**<br />
open pyBurn in your Favorite text editor and change this line:<br />
<code>api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')</code><br />
to contain your app keys<br />
(copy/move it to module/plugins/hooks)<br />

Start pyLoad

Activate/Change Settings in the Webinterface.

## The Settings:

**Activated:**<br />
Plugin Activated (no/yes) <br />
default: no<br />
<br />
**Interval:**<br />
Interval to run in seconds<br />
default: 30<br />
<br />
**Twitter Response:**<br />
Sends back a Response after a command was executed to nitify you (no/yes)<br />
default no<br />
<br />
**Use DM Whitelist**<br />
Use Whitelist of Twitter users (no/yes)<br />
YOU NEED TO SET THE USERNAME IN "DM Whitelist" (seperated by blanks)<br />
default no<br />
<br />
**DM Whitelist:**<br />
only accept DM's from this User (ONLY NEEDED IF "Use DM Whitelist" is TRUE)<br />
default none<br />
<br />
**Twitter Notify:**<br />
Send Notifications when Package Downloads are finished (no/yes)<br />
default no<br />
<br />
**Use DM for Notify:**<br />
Use DM instead of @ reply for ANY KIND notifications/replys (no/yes)<br />
default no<br />
<br />
**Twitter Notify User:**<br />
Use this if you like to Notify another like the one who send the connand, leve it as it is to send notes back to the sender<br />
default none<br />
