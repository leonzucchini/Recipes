import requests

class HMTLresponse(object):
    """ Response from trying to get an HTML page, returning error and text """

    def __init__(self, url):
      """ Try to get response from URL """

      self.error = 0
      self.error_message = ""
      self.text = ""

      # Try to get HTML response
      try:
        r = requests.get(url)
        r.raise_for_status()
        self.text = r.text.encode('utf-8')
    
      # If error, return error message and flag
      except requests.exceptions.RequestException as err:
        self.error = 1
        self.response = str(err)
        self.error_message = "".join(["Get error: ", url])
