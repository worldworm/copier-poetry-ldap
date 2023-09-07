""" LDAP connection module """
from ldap3 import NTLM, Connection
from loguru import logger

from ..config import config

connection = Connection(config.LDAP_URL, auto_bind=True, user=config.LDAP_USER, password=config.LDAP_PASSWORD, authentication=NTLM)
logger.debug("connection established with user {}", connection.extend.standard.who_am_i())
