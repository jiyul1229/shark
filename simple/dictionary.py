# dict = {
#     "name" : "이순신",
#     "age" : 55
# }

# print(dict["name"])

# dict = {
#     "data": ["홍길동", 55, True],
#     "number": 1
# }

# print(dict["data"][0])

name = "이름"

dict = {
    name : "홍길동"
}

print(dict)

dict[name] = "이순신"

dict["age"] = 50
del dict["이름"]

print(dict)