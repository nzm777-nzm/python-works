
def is_leap_year(year):
    
  if  year%100==0 or year%400==0 or year%4==0 or year%100!=0:
    
    return True

  else:
      
      return False

print(is_leap_year(2024))
    