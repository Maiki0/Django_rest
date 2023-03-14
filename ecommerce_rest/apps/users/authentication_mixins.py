from rest_framework import status,authentication,exceptions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    user = None
    
    def get_user(self, request):
        '''
        Return:
            * user    : User Instace or 
            *message  : Error message or
            *None     : Corrup Token
        '''
        token = get_authorization_header(request).split()
        if token:
            try: 
                token = token[1].decode()
                
            except:
                return None
    
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            
            if user != None:
                self.user = user 
                return user   
        return None
    
    def authentication( self,request):
        if self.user is None:
            self.get_user(request   )
            raise exceptions.AuthenticationFailed('No se han envidado las credenciales.')
        
        return (self.user, 1)
    
    '''def dispatch(self ,request , *args, **kwargs):
        user = self.get_user(request)
        #fopund token in request
        
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
        
        response = Response(
            {'Error':'No se han enviado las credenciales.'},status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response'''