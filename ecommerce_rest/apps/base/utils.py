def validate_files(request, field, upadte = False):
    '''
    :params
    :request: request.data
    :field: key of field
    
    '''
    
    request = request.copy()
    if upadte:
      if type(request[field]) == str: request.__delitem__(field)
      
    else:
       if type(request[field]) == str:request.__setitem__(field, None)  
    return request