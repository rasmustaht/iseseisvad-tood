nested_lists = [[1,2,3], [4,5,6]]
print(nested_lists[0][1])
ret = []
for el_v in nested_lists:
    print(el_v)
    for el_s in el_v:
        ret.append(el_s)
        
print(ret)