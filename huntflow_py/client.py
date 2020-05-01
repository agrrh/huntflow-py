import collections
import logging
import requests
import urllib.parse

from email_validator import validate_email, EmailNotValidError

__version__ = '0.1.0'


class Client(object):
    """Client handler, responsible for fetching data from various APIs."""

    VERSION = __version__
    USER_AGENT = f'huntflow-py/{VERSION}'
    BASE_URL = ''

    REQUEST_METHODS = collections.defaultdict(requests.get, {
        'GET': requests.get,
        'POST': requests.post,
        'PUT': requests.put,
    })

    def __init__(self, token=None, email=''):
        """
        Client used to simplify API calls, share some parameters, ease logging, etc.

            >>> from client import Client

        Ensure empty emails not allowed:

            >>> c = Client(token='test')
            Traceback (most recent call last):
            ...
            email_validator.EmailSyntaxError: The email address is not valid. It must have exactly one @-sign.

        Ensure invalid email not allowed:

            >>> c = Client(token='test', email='foo@bar.zorg')
            Traceback (most recent call last):
            ...
            email_validator.EmailUndeliverableError: The domain name bar.zorg does not exist.
        """
        self.token = token

        # NOTE HuntFlow requires User-Agent header, we also require valid email for emergency contact.
        valid = validate_email(email)
        if not email or not valid:
            raise EmailNotValidError

        self.email = valid.email

    def _request(self, url, method='GET', params={}, headers={}, json={}, files={}):
        headers_default = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': f'{self.USER_AGENT} ({self.email})',
        }

        try:
            resp = self.REQUEST_METHODS.get(method.upper())(
                urllib.parse.urljoin(self.BASE_URL, url),
                params=params,
                headers={
                    **headers_default,
                    **headers,
                },
                json=json,
                files=files,
            )
        except Exception as e:
            logging.error(f'Error requesting {url}: {e}')
            return False

        if resp.status_code not in (200,):
            logging.warning(f'Possible error, status code {resp.status_code} not in desired range')
            logging.debug(f'{resp.json()}')

        # TODO Retry on 429 Too Many Requests?

        # TODO Check result for being valid JSON

        return {
            'code': resp.status_code,
            'json': resp.json()
        }
