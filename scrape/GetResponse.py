import requests

class HTMLResponse(object):
  """ Get HTML text including error handling """
  
  def __init__(self, url):
    """Tries to get the HTML text for a URL and handles connection and
    HTML errors from the response. Returns a text or passes."""
    
    self.get_error = 0

    try:
      r = requests.get(url)
      r.raise_for_status()
      self.response = r.text.encode('utf-8')
    
    except requests.exceptions.RequestException as err:
      self.get_error = 1
      self.response = str(err)
      print "HTML Error: " + url

  def write_error(self):
    """ For HTML error write to error log """