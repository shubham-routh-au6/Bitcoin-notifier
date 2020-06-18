# Bitcoin Notifier

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


As we all know, the Bitcoin price keeps on fluctuating every hour/minute/day, we never really know what it is going to be at the end of the day. So instead of contstantly checking various sites, one can get the price notify to the desired destination with the help of this app. 

# Prerequisite 

    
  - 1 - Python3
  - 2 - IFTTT Account.
  - 3 - Applet created with webhooks.
  - 4 - Two event for emergency alert and normal alert.
  - 5 - IFTTT Webhook Token.

# Installation Guide for Windows

---------------------
- Step 1
    Download the Repo which you will find at the top right of the Repo link or clone it in your Local machine.
- Step 2
    Go into the Folder containing the Project files
    ```sh
     cd bitcoinNotifier
    ```
- Step 3
    Run the following Command
    ```sh
     cd bitcoinNotifier.py --help
    ```
    You'll see the following details:
    
    -h, --help            show this help message and exit
    
  -c COUNTRYCODE, --Countrycode COUNTRYCODE
                        Country code of a specific country for Bitcoin price
                        
  -l THRESHLIMIT, --Threshlimit THRESHLIMIT
                        Limit amount to get emergency alert
                        
  -n NORMALUPDATE, --NormalUpdate NORMALUPDATE
                        IFTTT event to get normal update for any destination
                        
  -e EMERGENCYUPDATE, --EmergencyUpdate EMERGENCYUPDATE
                        IFTTT event to get Emergency update for any destination
                        
  -f IFTTTTOKEN, --IFTTTtoken IFTTTTOKEN
                        IFTTT event to get normal update for any destination
                        
  -t TIMEINTERVAL, --TimeInterval TIMEINTERVAL
                        Time frequency for alerts

> You can enter a country code by passing -c (country code), by default it is set to INR.

> You can enter a treshold limit to get any emergency alert by passing -l (any_limit), by default it is set to (500000) for currency INR, if you use other currency then the limit should be entered with respect of the currency value.

> You can enter the applet event name to get the notification of normal update to the destined target by writting -n (event name), by default it is set to personal(Final_Check)

> You can enter the applet event name to get the notification of emergency update to the destined target by writting -e (event name), by default it is set to personal(Emergency_check).

> IFTTTTOKEN doesn't have a default value and you can enter your Webhook token by passing -f (token).

> You can enter the time frequency for alerts by passing -t (it works in second and doesn't take float value)
 

### Python Packages & Libraries Used

- Request
- time
- Argparser
- Tqdm

### Python Packages & Libraries Used
- Python 3.8
- HTTPS
- Webhooks
- IFTTT Applets


License
----

Shubham Routh **Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

