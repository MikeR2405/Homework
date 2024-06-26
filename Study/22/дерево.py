class BinaryTree:
    def __init__(self, value):  # Исправлено на __init__
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value)
        if self.left_child is not None:
            self.left_child.pre_order()
        if self.right_child is not None:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child is not None:
            self.left_child.post_order()
        if self.right_child is not None:  # Исправлено на is not None
            self.right_child.post_order()
        print(self.value)  # Посещаем корневой узел после обхода поддеревьев

    def in_order(self):
        if self.left_child is not None:
            self.left_child.in_order()

        print(self.value)

        if self.right_child is not None:
            self.right_child.in_order()



# Создание дерева и использование цепочки вызовов для добавления узлов
node_root = BinaryTree(2).insert_left(7).insert_right(5)
node_7 = node_root.left_child.insert_left(2).insert_right(6)
node_6 = node_7.right_child.insert_left(5).insert_right(11)
node_5 = node_root.right_child.insert_right(9)
node_9 = node_5.right_child.insert_left(4)

# Вызов метода постфиксного обхода
# node_root.post_order()

# Вызов метода обхода в прямом порядке
# node_root.pre_order()
node_root.in_order()