
def check_number(number):

    if number>0:

        return "+ve"
    
    elif number<0:

        return "-ve"
    
    elif number==0:

        return "zero"

def test_num_chk():

    assert check_number(10)=="+ve","+ve number check failed"

    assert check_number(-10)=="-ve","-ve number chk failed"

    assert check_number(0)=="zero","zero number chk failed"

try:

    test_num_chk()     

    print("ran test passed")

except Exception as e:

    print("test failed",e)       
