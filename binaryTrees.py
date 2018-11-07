class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print (self.value)

        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print (self.value)
        
        if self.right_child:
            self.right_child.in_order()
    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print (self.value)

''' 
    a_root = BinaryTree('a')
    a_root.insert_left('b')
    a_root.insert_right('c')

    b_node = a_root.left_child
    b_node.insert_right('d')

    c_node = a_root.right_child
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right_child
    e_node = c_node.left_child
    f_node = c_node.right_child

    print(a_root.value) # a
    print(b_node.value) # b
    print(c_node.value) # c
    print(d_node.value) # d
    print(e_node.value) # e
    print(f_node.value) # f
'''
one_node = BinaryTree('1')
one_node.insert_left('2')
one_node.insert_right('5')

two_node = one_node.left_child
five_node = one_node.right_child

two_node.insert_left('3')
two_node.insert_right('4')

three_node = two_node.left_child
four_node = two_node.right_child

five_node.insert_left('6')
five_node.insert_right('7')

six_node = five_node.left_child
seven_node = five_node.right_child






print("\n\n\n\n")
one_node.post_order()
