class TestA:
    attr=1
obj_a=TestA()
obj_b=TestA()
obj_a.attr=42
print (obj_b.attr)
print (obj_a.attr)