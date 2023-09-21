"""Main module."""
from .ldap.connection import cleanup, connection


def main():
    """Main function."""
    try:
        pass
    finally:
        cleanup()
