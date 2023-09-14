""" Main module """
from .ldap.connection import connection


def main():
    """ Main function """
    try:
        pass
    finally:
        connection.unbind()


if __name__ == "__main__":
    main()
