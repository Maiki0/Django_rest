from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from apps.users.models import User
from apps.users.api.serializers import( 
    UserSerializer, UserListSerializer,UpdataUserSerializer,PasswordSerializer)

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    lis_serializer_class = UserListSerializer
    queryset = None
    
    def get_object(self, pk):
            return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects\
                .filter(is_active=True)\
                .values('id', 'username', 'email','name')
        return self.queryset
   
    @action(detail=True, methods=['post'], url_path='cambio_pass')
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data = request.data )
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message':'Contraseña actualizada corectamente'},
            status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay error en la infoemacion enviada',
            'Error':password_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)
    
    def list (self, request):
        users = self.get_queryset()
        users_serializer = self.lis_serializer_class(users, many=True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)
    
    def create (self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message':'Usuario regitrado correctamente'
            },status=status.HTTP_201_CREATED)
        return Response({
                        'message':'Hay un error en el registro',
                        'error': user_serializer.errors },
                        status=status.HTTP_400_BAD_REQUEST)
        
        
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdataUserSerializer(user,request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                            'message':'Usurio actualizado correctamente'},
                            status=status.HTTP_200_OK)
            
        return Response ({'message':'Error en la catualizacion',
                          'Error':user_serializer.errors},
                           status=status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active = False)
        if user_destroy == 1:
            return Response({
                'message':'Usuario se a eliminado correctament'
            },status=status.HTTP_200_OK)  
            
        return Response({
            'message':'No exixte el usuario que desea eliminar'
        },status=status.HTTP_404_NOT_FOUND)