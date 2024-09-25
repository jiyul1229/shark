# sort()
# 기존의 리스트를 정렬한다.
# 리스트 내에서 정의될 수 있다.

# sorted()
# 새로운 정렬된 리스트를 만든다.

list_num = [33, 2, 81, -77, 44, 1, 10, 99, 5, 0, -2]
list_str1 = ['b', 'l', 'o', 'c', 'k', 'd', 'm', 'a', 's', 'k']
list_str2 = ['B', 'L', 'o', 'C', 'k', 'D', 'M', 'a', 'k']

print("1. 숫자 리스트 정렬")
list_num.sort()
print(list_num)

print("\n2.소문자 문자열 리스트 정렬")
list_str1.sort()
print(list_str1)

print("\n3.대소문자 문자열 리스트 정렬")
list_str2.sort()
print(list_str2)

a = [3, 2, 8, 4, 1, 10, 99, 5]
b = [3, 2, 8, 4, 1, 10, 99, 5]
c = [3, 2, 8, 4, 1, 10, 99, 5]

a.sort()
print("a.sort()")
print(a)

b.sort(reverse=False)
print("\nb.sort(reverse=False)")
print(b)

c.sort(reverse=True)
print("\nc.sort(reverse=True)")
print(c)