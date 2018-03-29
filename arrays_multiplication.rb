#arrays multiplication

first_array = [1, 2, 4, 7, 3, 9, 76, 12]
second_array = [10, 12, 78, 43, 9, 53, 27, 41]

def array_multiplication
    third_array = first_array.zip(second_array).map{|x, y| x * y }
end