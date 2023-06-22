from django_auth-ldap.backend import LDAPBackend

class MyLDAPBackend(LDAPBackend):
    """ A custom LDAP authentication backend """

    def authenticate(self, username, password):
        """ Overrides LDAPBackend.authenticate to add custom login """

        user = LDAPBackend().authenticate(self, username, password)
        """ Add custom login here """
        return user
