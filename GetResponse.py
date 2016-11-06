import requests

class HTMLResponse(object):
  """Response from a get request to a server with a specific URL.
  Error handling for get requests."""
  
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
