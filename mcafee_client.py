import json


try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class EPOError(Exception):
    """An error occured inside of the API."""


class McClient:
    """Communicate with an ePO server.
    Instances are callable, pass a command name and parameters to make API calls.
    """

    def __init__(self, server, port, username, password, verify=True):
        """Create a mcafee_client for the specified ePO server.

        :param server  : Host name or IP address of ePO server
        :param port    : Port Server is listening on
        :param username: username to authenticate
        :param password: password to authenticate

        .. todo::
            This still needs to be tested.  Not sure how it will handle bad password.
        """

        from requests import Session

        self._session = Session()

        self._verify = verify
        self._url = "https://{0}:{1}".format(server,port)

        # Gets a security token from the ePO server.
        self._token = self._request('core.getSecurityToken', auth=(username,password), verify=self._verify)

    def request(self, endpoint, **kwargs):
        """Method to initiate call to ePO server and return results.

        :param endpoint: ePO command to call
        :param kwargs: arguments passed to requests
        :return: deserialized JSON data

        .. todo::
            This function is still in development and needs to be tested.
            Need to implement code so it accepts other formats than just json
        """

        if self._verify:
            kwargs.setdefault('verify', True)

        params = kwargs.setdefault('params', {})
        params.setdefault(':output', 'json')
        params.setdefault('orion.user.security.token', self._token)

        url = urljoin(self._url, 'remote/{}'.format(endpoint))

        if kwargs.get('data') or kwargs.get('json') or kwargs.get('files'):
            # use post method if there is post data
            r = self._session.post(url, **kwargs)
        else:
            r = self._session.get(url, **kwargs)

        # Raises an error if a web error was received
        r.raise_for_status()
        text = r.text

        if not text.startswith('OK:'):
            # Raises an error if the API call was invalid
            raise EPOError(text)

        return json.loads(text[3:])


