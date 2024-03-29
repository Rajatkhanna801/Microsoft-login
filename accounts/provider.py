from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.contrib.auth.models import User


class MicrosoftAccount(ProviderAccount):

    def to_str(self):
        dflt = super(MicrosoftAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class MicrosoftProvider(OAuth2Provider):
    id = 'microsoft'
    name = 'Microsoft'
    account_class = MicrosoftAccount

    def get_scope(self, request):
        scope = set(super(MicrosoftProvider, self).get_scope(request))
        scope.add('openid')
        return list(scope)

    def get_default_scope(self):
        return ['openid', 'User.read']

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        response = dict(
            username=data.get('mail'),
            email=data.get('mail'),
            last_name=data.get('surname'),
            first_name=data.get('givenName')
        )
        # if user := User.objects.filter(email=data.get('mail')).last():
        #     response['user_permissions'] = list(
        #         user.groups.last().permissions.values_list('codename', flat=True)
        #     )
        return response

provider_classes = [MicrosoftProvider]
