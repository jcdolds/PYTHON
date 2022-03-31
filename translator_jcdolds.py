# -*- coding: utf-8 -*-
"""IBM_COURSERA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kYp1sybVhg4gIigpuO4BTXPwrvMOfKF_

### PROYECTO 1 - IBM COURSERA
"""

!pip install ibm_watson

apikey = 'e7_hpg1H6HoKwHtMGNTW4rqUcOzvp29CgcJ9-vmMwvbo'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/435eb4d8-d93e-4336-8a4d-844c512b2dd6'

# import deps
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup service
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

translation = lt.translate(text='Hi!, My name is Juan Daniel', model_id='en-fr').get_result()

translation

translation['translations'][0]['translation']

text = 'Bonjour, mon nom est Juan Daniel'

a = translation['translations'][0]['translation']

a == text