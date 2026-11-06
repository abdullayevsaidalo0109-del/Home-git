# uyga vazifa
# 1
 
# def majority_element(numbers: list) ->int:
#     dct ={}
#     for i in numbers:
#         if i not in dct:
#             dct[i] = 1
#         else:
#             dct[i] +=1
#     return max(dct, key=dct.get)
        
# numbers =  [2, 2, 1, 1, 1, 2, 2]
# print(majority_element(numbers))

 # 2

# def search_by_genre(cinema:list, genre:str)->list:
#     result = []
#     for i in cinema:
#         if i['genre'] == genre:
#             result.append(i)
#     return result

# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

# print(search_by_genre(cinema, "Fantastika"))