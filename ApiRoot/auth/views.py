from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist


class LogoutView(APIView):
    permission_classes = (AllowAny,) # Any user can attempt to log out, with authentication or not
    authentication_classes = () # Set to empty tuple --- configured !use the default authentication methods for this specific request. This is important for our logout functionality, as it should be accessible without requiring a valid token for authentication.

    def post(self, request):
        try:
            refresh_token = request.data["refresh"] # Retrieve the refresh token
            token = RefreshToken(refresh_token) #  Create a "RefreshToken" Object--Essential for "blacklist" functionality

            token.blacklist() # Call the method so that token cannot be used to obtain new access token, thus logging out
            return Response(status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, TokenError):
            return Response(status=status.HTTP_400_BAD_REQUEST)