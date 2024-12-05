

def is_leap_year(year):

    if year<0:

        return False

    if year%4==0 and year%100!=0 or year%400==0 and year%100==0:

        return True
    
    else:

        return False
    
def test_is_year_chk():   

    assert  is_leap_year(2024)==True,"non centuary year chk failed"

    assert is_leap_year(2025)==False,"invalid non centuary year chk failed" 

    assert  is_leap_year(2000)==True,"centuary leap  year chk failed"

    assert is_leap_year(1900)==False,"invalid centuary year chk failed"

    assert is_leap_year(-2024)==False,"invalid year chk failed"

try:
    test_is_year_chk()
    print("test case pass")

except Exception  as e:
    print("test failed",e)