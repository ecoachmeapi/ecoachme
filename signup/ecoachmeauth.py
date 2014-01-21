from tastypie.authentication import Authentication


class ecoachmeauth(Authentication):
    def is_authenticated(self, request, **kwargs):
        if 'teste' in request.user.username:
          return True

        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username
