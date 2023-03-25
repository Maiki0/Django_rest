def validate_files(request, feild):
    '''
    :params
    :request: request.data
    :field: key of field
    
    '''
    
    request._mutable = True
    request[feild] = None if type(request[feild]) == str else request [feild] 
    request._mutable = False 
    return request