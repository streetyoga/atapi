from setuptools_scm import get_version
import requests


class API:
    """API base class"""

    def __init__(self, timeout=None, show_limit_usage=False, show_header=False):
        self.timeout = timeout
        self.show_limit_usage = show_limit_usage
        self.show_header = show_header
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json;charset=utf-8",
                                     "User-Agent": "atapi/" + get_version(),
                                     })

    def query(self, url, payload=None):
        """get request"""
        params = {"url": url,
                  "params": payload,
                  "timeout": self.timeout}
        response = self.session.get(**params)
        data = response.json()
        result = {}
        if self.show_limit_usage:
            result["limit_usage"] = {key: response.headers[key] for key
                                     in response.headers.keys()
                                     if key.startswith("x-mbx-used-weight")
                                     or key.startswith('x-mbx-order-count')
                                     or key.startswith('x-sapi-used')}
        if self.show_header:
            result["header"] = response.headers
        if len(result) != 0:
            result["data"] = data
            return result
        return data
