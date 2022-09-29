"""
字典的作用:
    更容易看的懂，key:value
    key不能重复，如果key重复，就会之前的key给覆盖掉
    list不能作为Key
    字典不能作为Key
    元组可以作为key，因为元组是不可变的
"""
info = {(1, 2): "val1"}
print(info)
