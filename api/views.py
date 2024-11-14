from django.shortcuts import render 
from rest_framework import viewsets, permissions
from api.models import Cliente, Producto
from api.serializers import ClienteSerializer, ProductoSerializer, UserSerializer
from rest_framework import status, views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from rest_framework.authtoken.models import Token

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]
    # Uncomment the following lines if you want to restrict access to authenticated users
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username is None or password is None:
            return response.Response({'message': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return response.Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key}, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        # Verificamos si el usuario está autenticado
        if not request.user.is_authenticated:
            return response.Response(
                {'message': 'No estás autenticado. No se puede cerrar sesión.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Borramos el token de la solicitud
        request.user.auth_token.delete()
        # Cerramos sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return response.Response(
            {'message': 'Sesión cerrada y token eliminado.'},
            status=status.HTTP_200_OK
        )

# Create your views here.
