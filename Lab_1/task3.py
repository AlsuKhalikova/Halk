# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
count_of_pages = 100
count_of_strings = 50
count_of_symbols = 25
volume_of_symbol = 4
volume_in_bytes = volume * 1024 ** 2
volume_of_one_book = count_of_pages * count_of_strings * count_of_symbols * volume_of_symbol

print("Количество книг, помещающихся на дискету:", round(volume_in_bytes // volume_of_one_book, ))
