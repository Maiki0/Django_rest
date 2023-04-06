from datetime import datetime

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
  
def format_date(date):
  date = datetime.strptime(date, '%d/%m/%y')
  date = f"{date.year}-{date.month}-{date.day}"
  return date