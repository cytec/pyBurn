# pyBurn

ive rewritten my bash scripts to python... yeah!
so now pyBurn is a hook for pyLoad itself.

## NOTE!
Currently this is in heavy development.
So if you like to test, feel free to do so but notice that this is still a verry early version 

## Current features:

**Add new Links over Twitter**
Usage: AddLinks {CONTAINERNAME} LINK LINK LINK
If no Containername it generates one based on DM Sendername and Date.

**Twitter Response**
Activate the Twitter Response Options in the Settings and pyBurn will send you either an DM or an @ reply after adding the links from your AddLinks command.


##Requiers:

* pyLoad
* python-twitter
* twitter API keys (http://twitter.com/apps)

## How To:

Install pyLoad.

Install python-twitter

go to http://twitter.com/apps and create an app, be sure you select DM access under rights.

**Download pyBurn*** <br />
open pyBurn in your Favorite text editor and change this line:
<code>api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')</code>
to contain your app keys
(copy/move it to module/plugins/hooks)

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
