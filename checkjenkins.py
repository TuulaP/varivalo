

import json
import requests
import time

from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime

# Original from https://stackoverflow.com/a/53800802/364931

job_name = "master-tests"  #Give your job name here


load_dotenv()  # take environment variables from .env.

## if auth needed
usr = os.getenv('USRN')
sal = os.getenv('SAL')
auth = HTTPBasicAuth(usr, sal)
JENKINSPATH = os.getenv('JENKINSPATH')


def jenkins_job_status(job_name):

    try:

        url  = JENKINSPATH + "/job/%s/lastBuild/api/json" % job_name  
        print(url)

        while True:
            data = requests.get(url, auth=auth)
            print(data.status_code)

            if (data.status_code == 200):
                #print("!!!", data)
                data = data.json()
            if data['building']:
                time.sleep(60)
            else:
                if data['result'] == "SUCCESS":
                    id = data['fullDisplayName']
                    print(id)
                    lastrun = data['timestamp']
                
                    print("Job {0} is success, last run at {1}".format(id, lastrun))
                    return True
                else:
                    print("Job status failed")
                    return False

    except Exception as e:
        print(str(e))
        return False




jenkins_job_status("master-tests")

