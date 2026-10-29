   from average import average


   def test_average_of_numbers():
       assert average([2, 4, 6]) == 4


   def test_average_of_empty_list_is_zero():
       assert average([]) == 0
