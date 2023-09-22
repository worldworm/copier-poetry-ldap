"""LDAP connection module."""
import os

from ldap3 import Connection, Server, ServerPool
from loguru import logger

from ..config import config


def cleanup():
    """Close and Cleanup ldap connection."""
    connection.unbind()
    logger.debug("ldap connection closed")


if not os.environ.get("PYTEST"):  # pragma: no cover
    if isinstance(config.LDAP_URL, list):
        server = ServerPool(None, "ROUND_ROBIN")
        for server_url in config.LDAP_URL:
            server.add(Server(server_url))
    else:
        server = Server(config.LDAP_URL)

    connection = Connection(server, auto_bind=True, user=config.LDAP_USER, password=config.LDAP_PASSWORD)
    logger.debug("ldap connection established with user {}", connection.extend.standard.who_am_i())
else:
    connection = None  # pylint: disable=invalid-name
