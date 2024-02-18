#!/usr/bin/python3

import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '+255756270855',
  'message': 'You owe me 8,430,000 its high time you paid up. This is a malware messagegiving me access to your phone data.
 Elisha nilipe pesa zangu!',
  'key': 'textbelt',
})
print(resp.json())
