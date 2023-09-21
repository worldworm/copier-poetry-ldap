"""LDAP connection module."""
import os

from ldap3 import NTLM, Connection
from loguru import logger

from ..config import config


def cleanup():
    """Close and Cleanup ldap connection."""
    connection.unbind()
    logger.debug("ldap connection closed")


if not os.environ.get("PYTEST"):  # pragma: no cover
    connection = Connection(config.LDAP_URL, auto_bind=True, user=config.LDAP_USER, password=config.LDAP_PASSWORD, authentication=NTLM)
    logger.debug("ldap connection established with user {}", connection.extend.standard.who_am_i())
else:
    connection = None  # pylint: disable=invalid-name
