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

# 3

# def merge_unique_ids(active_users:list, new_users:list)->list:
#     new = []
#     for i in active_users + new_users:
#         if i not in new:
#             new.append(i)
#     return new

# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
# print(merge_unique_ids(active_users, new_users))

# 4

# def sorted_by_price(product:list)->list:
    
#     return sorted(product, key=lambda x: int(x[1]), reverse=True)

# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]

# print(sorted_by_price(products))
         
