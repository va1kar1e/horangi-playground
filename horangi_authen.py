# coding: utf-8
# Author: Siwanont Sittinam

import os
from dotenv import load_dotenv
load_dotenv()


class HorangiAuthentication:
    def getHostname(self):
        HOSTNAME = os.getenv("HORANGI_HOSTNAME")

        return HOSTNAME

    def getRequestHeader(self):
        HORANGI_API_KEY = os.getenv("HORANGI_API_KEY")

        return {
            'x-api-key': str(HORANGI_API_KEY)
        }
