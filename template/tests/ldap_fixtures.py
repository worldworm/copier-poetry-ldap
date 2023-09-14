""" LDAP fixtures for testing """
import pytest
from ldap3 import MOCK_SYNC, Connection, Server


@pytest.fixture()
def ldap_connection() -> Connection:
    """ Returns a connection to a fake LDAP server with some entries for testing """
    connection = Connection(Server("fake_server"), user="cn=user0,ou=users,dc=example,dc=com", password="test", client_strategy=MOCK_SYNC)
    # Users
    connection.strategy.add_entry("cn=user0,ou=users,dc=example,dc=com", {"objectClass": "user", "userPassword": "test"})
    connection.strategy.add_entry("cn=user1,ou=users,dc=example,dc=com", {"objectClass": "user"})
    connection.strategy.add_entry("cn=user2,ou=users,dc=example,dc=com", {"objectClass": "user"})
    connection.strategy.add_entry("cn=user3,ou=users,dc=example,dc=com", {"objectClass": "user"})

    # Groups
    connection.strategy.add_entry("cn=group0,ou=groups,dc=example,dc=com", {"objectClass": "group", "member": []})
    connection.strategy.add_entry("cn=group1,ou=groups,dc=example,dc=com", {
                                  "objectClass": "group", "member": ["cn=user1,ou=users,dc=example,dc=com"]})
    connection.strategy.add_entry("cn=group2,ou=groups,dc=example,dc=com", {
                                  "objectClass": "group", "member": ["cn=user2,ou=users,dc=example,dc=com"]})
    connection.strategy.add_entry("cn=group3,ou=groups,dc=example,dc=com", {"objectClass": "group", "member": [
                                  "cn=user1,ou=users,dc=example,dc=com", "cn=user2,ou=users,dc=example,dc=com"]})
    connection.strategy.add_entry("cn=group4,ou=groups,dc=example,dc=com", {"objectClass": "group", "member": [
                                  "cn=group1,ou=groups,dc=example,dc=com", "cn=user3,ou=users,dc=example,dc=com"]})

    connection.bind()
    return connection
