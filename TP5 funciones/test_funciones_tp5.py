import pytest

'''
#* PRUEBA PUNTO 1 *

from funciones import validation

def test_validation():
    assert validation(44437811) == True
    assert validation(4443781) == True
    assert validation(444378) == False
    assert validation(444378111) == False


    



#*PRUEBA PUNTO 2*

from funciones import last_word_lenght

def test_last_word_lenght():
    assert last_word_lenght("lista de palabras") == 8


    



#*PRUEBA PUNTO 3*

from funciones import id_obtaining

def test_id_obtaining():
    assert id_obtaining("matias nicolas salinas","44437811") == "matias7444"
    assert id_obtaining("laura romina claros","2347645")     == "laura6234"
    assert id_obtaining("alejandro alcacer","53426352")      == "alejandro7534"
    assert id_obtaining("santiago sosa","43265478")          == "santiago4432"


    



# PRUEBAS PUNTO 4

from funciones import is_mult, the_first_is_mult

def test_is_mult():
    assert is_mult(3,9) == True
    assert is_mult(9,9) == True
    assert is_mult(3,5) == False

def test_the_first_is_mult():
    assert the_first_is_mult(6,2) == True
    assert the_first_is_mult(5,2) == False
    assert the_first_is_mult(6,6) == False


    



# PRUEBAS PUNTO 5    

from funciones import temp_average

def test_temp_average():
    assert temp_average(20,10) == 15
    assert temp_average(3,12)  == 7.5
    assert temp_average(12,18) == 15
    assert temp_average(30,11) == 20.5
    assert temp_average(14,9)  == 11.5
    assert temp_average(1,6)   == 3.5
    assert temp_average(8,22)  == 15



    

    
# PRUEBAS PUNTO 6

from funciones import text_modifier

def test_text_modifier():
    assert text_modifier("que tal el paseo","")   == "q u e   t a l   e l   p a s e o "
    assert text_modifier("ojala ganemos","")      == "o j a l a   g a n e m o s "
    assert text_modifier("cuidado el escalon","") == "c u i d a d o   e l   e s c a l o n "
    assert text_modifier("buenas noches","")      == "b u e n a s   n o c h e s "
    assert text_modifier("lo encontramos","")     == "l o   e n c o n t r a m o s "



    


# PRUEBAS PUNTO 7
    
from funciones import obtain_max_and_min

def test_obtain_max_and_min():
    assert obtain_max_and_min([ 1 , 2 , 3 , 4 , 5 ])           == (1,5)
    assert obtain_max_and_min([ 4 , 232 , 53 , 47 , 5 ])       == (4,232)
    assert obtain_max_and_min([ 12 , 1453 , 10 , 844 , 21 ])   == (10,1453)
    assert obtain_max_and_min([ 3 , 3 , 6 , 9 , 15 ])          == (3,15)
    assert obtain_max_and_min([ 1000 , 20000 , 3 , 400 , 50 ]) == (3,20000)
    assert obtain_max_and_min([ 9 , 14 , 15 , 12 , 5 ])        == (5,15)


    

    

# PRUEBAS PUNTO 8

from funciones import obt_area_perimeter

def test_obt_area_perimeter():
    assert obt_area_perimeter(1) == (3.14, 6.28)
    assert obt_area_perimeter(2) == (12.56, 12.56)
    assert obt_area_perimeter(3) == (28.26, 18.84)
    assert obt_area_perimeter(4) == (50.24, 25.12)


    



# PRUEBAS PUNTO 9

from funciones import login

@pytest.mark.parametrize(
    "username,password,tries,expected1,expected2",
    [
        ("usuario1","asdasd",0,True,0),
        ("user1","asdasd",0,False,1),
        ("usuario","wasdwasd",2,False,3),
        ("usuario1","asdasd",2,True,2)
    ]
)
def test_login(username,password,tries,expected1,expected2):
    assert login(username,password,tries) == (expected1,expected2)


    

    

# PRUEBAS PUNTO 10

from funciones import apply_discount  

@pytest.mark.parametrize(
    "costs, expected_result", 
    [
        ({"cost1": 100, "cost2": 200, "cost3": 300, "discount1": 0, "discount2": 0, "discount3": 0       } , 600),
        ({"cost1": 100, "cost2": 200, "cost3": 300, "discount1": 0.2, "discount2": 0.1, "discount3": 0.3 } , 470),
        ({"cost1": 200, "cost2": 500, "cost3": 1000, "discount1": 0.2, "discount2": 0.1, "discount3": 0.3} , 160+450+700),
        ({"cost1": 400, "cost2": 200, "cost3": 600, "discount1": 0.2, "discount2": 0.1, "discount3": 0.3 } , 320+180+420),
        ({"cost1": 500, "cost2": 1500, "cost3": 1600, "discount1": 0.5, "discount2": 0.3, "discount3": 0.4 } , 2260),
    ]
)
def test_apply_discount(costs, expected_result):
    assert apply_discount(costs) == expected_result


    



# PRUEBAS PUNTO 11

from funciones import apply_absolute_value,get_absolute_value

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1,2,3,4,-5,-6,-7,-8]  , [1,2,3,4,5,6,7,8]),
        ([-3,-6,-9,-15,-24,-39] , [3,6,9,15,24,39]),
        ([-11,22,33,44,-55]     , [11,22,33,44,55]),
        ([1,2,3,4,-5,-6,-7,-8]  , [1,2,3,4,5,6,7,8]),
        ([3,-5,7,-9,11,-13,]    , [3,5,7,9,11,13]),
    ]
)
def test_apply_absolute_value(nums,expected):
    assert apply_absolute_value(nums) == expected

    

    


# PRUEBAS PUNTO 12

from funciones import text_to_dictionary

def test_text_to_dictionary():
    result = text_to_dictionary("se lo que es")
    assert result == ({'palabra 1':'se' , 'palabra 2':'lo' , 'palabra 3':'que' , 'palabra 4':'es'} , 4)
    result = text_to_dictionary("que buen servicio")
    assert result == ({'palabra 1':'que' , 'palabra 2':'buen' , 'palabra 3':'servicio'} , 3)
    result = text_to_dictionary("que elegancia la de francia")
    assert result == ({'palabra 1':'que' , 'palabra 2':'elegancia' , 'palabra 3':'la' , 'palabra 4':'de' , 'palabra 5':'francia'} , 5)


    

    

# PRUEBAS PUNTO 13    

from funciones import get_module

def test_get_module():
    assert get_module([2,3,4,5,6]) == [0,1,0,1,0]
    assert get_module([5,6,15,16,20]) == [1,0,1,0,0]
    assert get_module([20,19,40,39,60]) == [0,1,0,1,0]
    assert get_module([-7,-11,-13,-17,-19]) == [1,1,1,1,1]
    assert get_module([2,4,6,8,10]) == [0,0,0,0,0]


    

    

# PRUEBAS PUNTO 14

from funciones import prime_nums

def test_prime_nums():
    assert prime_nums(0) == False
    assert prime_nums(1) == False
    assert prime_nums(2) == True
    assert prime_nums(3) == True
    assert prime_nums(5) == True
    assert prime_nums(13) == True
    assert prime_nums(210) == False
    assert prime_nums(123) == True
    assert prime_nums(151) == True
    assert prime_nums(4230) == False






# PRUEBAS PUNTO 15
      
from funciones import get_factorial

def test_get_factorial():
    assert get_factorial(-1)== "No se puede calcular el factorial de un número negativo"
    assert get_factorial(0) ==   1
    assert get_factorial(3) ==   6
    assert get_factorial(5) == 120


    



# PRUEBAS PUNTO 16

from funciones import get_currencys

def test_get_currencys():
    assert get_currencys(37617,7)==2
    assert get_currencys(61523,6)==1
    assert get_currencys(111,1)==3
    assert get_currencys(543543,4)==2


    


    
# PRUEBAS PUNTO 17

from funciones import show_digits_sum

def test_show_digits_sum():
    assert show_digits_sum(4)==4
    assert show_digits_sum(12)==3
    assert show_digits_sum(653)==14
    assert show_digits_sum(1363)==13
    assert show_digits_sum(836)==17
    assert show_digits_sum(8643)==21
'''