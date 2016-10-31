import requests

class GetResponse:
  """Response from a get request to a server with a specific URL.
  Error handling for get requests."""

  timeout = 1

  def __init__(self):
    """Init"""
    self.get_error = 0
    self.response = ''

  def tryRequest(self, url):
    """Tries to get the HTML text for a URL and handles connection and
    HTML errors from the response. Returns a text or passes."""

    try:
      r = requests.get(url)
      r.raise_for_status()
      self.response = r.text

    except requests.ConnectionError as err:
      self.get_error = 1
      self.response = str(err)

    except requests.exceptions.HTTPError as err:
      self.get_error = 1
      self.response = str(err)

    except requests.exceptions.Timeout as err:
      self.get_error = 1
      self.response = str(err)

    return self
