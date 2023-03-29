def validate_files(request, field, upadte = False):
    '''
    :params
    :request: request.data
    :field: key of field
    
    '''
    
    request._mutable = True
    if upadte:
      if type(request[field]) == str: 
          del request[field]
    else:
        request[field] = None if type(request[field]) == str else request [field] 
    request._mutable = False 
    return request