import requests
import os
from dotenv import load_dotenv
load_dotenv()

class CaesarCron:
    def __init__(self) -> None:
        # TODO The Token may change occasionally.
        response = requests.get('https://api.upstash.com/v2/qstash/user', auth=('amari.lawal05@gmail.com', os.getenv("QSTASH_API_KEY")))
        customer_info = response.json()
        self.token  = customer_info["token"]
        self.qstashurl = f"https://qstash.upstash.io/v1/publish/"
    def schedule(self,url,message=None,**kwargs):
        """
        Schedules a cron job to be sent using cron expressions  - * * * * * (https://crontab.guru/)
        https://console.upstash.com/qstash
        
        Parameters
        ----------
        url: str
            The POST url to schdule the cron job.
        message: dict, optional
            JSON message sent in the POST body,
        customschedule: str, kwarg(optional)
            Time interval to schedule the cronjob using custom cron expression(https://crontab.guru/).

        everyhour: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 * * * *.
        everyminute: bool, kwarg(optional)
            Time interval to schedule the cronjob - * * * * *.
        everytenminutes: bool, kwarg(optional)
            Time interval to schedule the cronjob - */10 * * * *.
        
        everymorning: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 9 * * *.
        everynight: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 22 * * *.

        everyweek: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 0 * * 0.
        every_day_at_midnight: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 0 * * *.
        every_day_at_twelve_pm: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 12 * * *.
        first_day_of_every_month: bool, kwarg(optional)
            Time interval to schedule the cronjob - 0 0 1 * *.

        Returns
        -------
        response: dict
            The schduleid of the cron job.

        """
        #
        customschedule = kwargs.get("customschedule")
        everyhour= kwargs.get("everyhour")
        everymorning = kwargs.get("everymorning")
        everynight = kwargs.get("everynight")
        everyminute = kwargs.get("everyminute")
        everytenminutes = kwargs.get("everytenminutes")
        every_week = kwargs.get("everyweek")
        every_day_at_midnight = kwargs.get("every_day_at_midnight")
        every_day_at_twelve_pm = kwargs.get("every_day_at_twelve_pm")
        first_day_of_every_month = kwargs.get("first_day_of_every_month")
        if kwargs:
            if customschedule:
                cronstring = customschedule
            if everyhour:
                cronstring = "0 * * * *"
            if everyminute:
                cronstring = "* * * * *"
            if everytenminutes:
                cronstring = "*/10 * * * *"
            
            if every_day_at_midnight:
                cronstring = "0 0 * * *"
            if every_day_at_twelve_pm:
                cronstring = "0 12 * * *"
            if every_week:
                cronstring = "0 0 * * 0"
            if first_day_of_every_month:
                cronstring = "0 0 1 * *"
            if everymorning:
                cronstring = "0 9 * * *"
            if everynight:
                cronstring = "0 22 * * *"
            
        elif not kwargs:
            cronstring = "0 * * * *"
        



        
        try:
            response = requests.post(f"{self.qstashurl}{url}",
                        headers={"Authorization": f"Bearer {self.token}","Upstash-Cron":cronstring,"Content-Type":"application/json"},
                        json=message
                        )
        except UnboundLocalError as uex:
            if "cronstring" in str(uex):
                cronstring = "0 * * * *"
                response = requests.post(f"{self.qstashurl}{url}",
                        headers={"Authorization": f"Bearer {self.token}","Upstash-Cron":cronstring,"Content-Type":"application/json"},
                        json=message
                        )
            else:
                print(f"{type(uex)},{uex}")

        return response.json()
    def send_delay(self,url,message=None,delay=0,**kwargs):
        seconds = kwargs.get("seconds")
        minutes = kwargs.get("minutes")
        hours= kwargs.get("hours")
        days = kwargs.get("days")
        if kwargs:
            if seconds:
                delaystr = "s"
            if minutes:
                delaystr = "m"
            if hours:
                delaystr = "h"
            if days:
                delaystr = "d"
        elif not kwargs:
            delaystr = "m"

        try:
            response = requests.post(f"{self.qstashurl}{url}",
                headers={"Authorization": f"Bearer {self.token}","Upstash-Delay":f"{delay}{delaystr}","Content-Type":"application/json"},
                json=message
                )
        except UnboundLocalError as uex:
            if "delaystr" in uex:
                delaystr = "m"
                response = requests.post(f"{self.qstashurl}{url}",
                headers={"Authorization": f"Bearer {self.token}","Upstash-Delay":f"{delay}{delaystr}","Content-Type":"application/json"},
                json=message
                )

        return response.json()
if __name__ == "__main__":
    caesarcron = CaesarCron()
    result = caesarcron.schedule("https://flyflasktest.fly.dev/sendemail",{"email":"amari.lawal@gmail.com","subject":"Caesar TEst Email Hello World","message":"Hello World"},everynight=True)
    print(result)

    #result = caesarcron.send_delay("https://flyflasktest.fly.dev/sendemail",{"email":"amari.lawal@gmail.com","subject":"Caesar TEst Email Hello World","message":"Hello World"},2,seconds=True)
    #print(result)