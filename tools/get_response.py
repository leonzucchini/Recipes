import requests
from tools import get_user_agent

class HTMLresponse(object):
  """ Response from trying to get an HTML page, returning error and text """

  def __init__(self, url, user_agent=None):
    """ Try to get response from URL """

    self.error = 0
    self.error_message = ""
    self.text = ""

    # Try to get HTML response
    try:
      if user_agent == None:
        r = requests.get(url)
      else:
        r = requests.get(url, headers=user_agent)

      r.raise_for_status()
      self.text = r.text.encode('utf-8')

    # If error, return error message and flag
    except requests.exceptions.RequestException as err:
      self.error = 1
      self.response = str(err)
      self.error_message = "".join(["Get error: ", url])
