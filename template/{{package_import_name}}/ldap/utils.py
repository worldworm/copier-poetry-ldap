"""LDAP helper functions."""
from ldap3 import Connection
from loguru import logger


@logger.catch(reraise=True)
def get_group_members(connection: Connection, group_dn: str) -> list[str]:
    """Recursively get all members of a group."""
    connection.search(search_base=group_dn, search_filter="(objectClass=group)", search_scope="BASE", attributes=["member"])

    if len(connection.entries) != 1:
        raise LookupError(f"A unique assignment was not possible for {group_dn} ({len(connection.entries)} results found)")

    members = []
    for member in connection.entries[0].member.values:
        if "ou=users" in member.lower():
            members.append(member)
        else:
            members.extend(get_group_members(connection, member))

    return members
