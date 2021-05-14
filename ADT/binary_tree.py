
class BinaryTree:
    """
    Class representing a binary tree.
    """
    def __init__(self, *args, **kwargs):
        if args:
            assert len(args) == 1
            self.empty = False
            self.data = args[0]
            # If parameter doesn't exists save as empty tree
            self.left = kwargs.pop("left", None) or BinaryTree()
            self.right = kwargs.pop("right", None) or BinaryTree()
        else:
            self.empty = True
        assert not kwargs  # Can't accept other arguments

    def __repr__(self, shift='') -> str:
        """
        Representation fucntion for binary tree
        :param shift: str
        :return: str
        """
        if self.empty:
            return "BinaryTree()".format(shift)
        elif self.left.empty and self.right.empty:
            return 'BinaryTree({1})'.format(shift, self.data)
        else:
            return 'BinaryTree({1},\n{0}      left = {2},\n{0}      right = {3})'. \
                format(shift,
                       self.data,
                       self.left.__repr__(shift + '             '),
                       self.right.__repr__(shift + '              ')
                       )

    def __eq__(self, other) -> bool:
        """
        Equality method for two binary trees.
        :param other: BinaryTree
        :return: bool
        """
        if self.empty and other.empty:
            return True
        elif not self.empty and not other.empty:
            return (
                    self.data == other.data and self.left == other.left and self.right == other.right)
        else:
            return False

    def __hash__(self) -> hash:
        """
        Hash method for binary tree
        :return: hash
        """
        if self.empty:
            return hash(())
        else:
            return hash((self.data, self.left, self.right))

    def cut(self, level) -> None:
        """
        Method removes all the subtrees from given level.
        :param level: int
        :return: None
        """
        if level == 0:
            self.empty = True
            self.left = None
            self.right = None
            self.data = None
        elif self.empty:
            pass
        else:
            self.left.cut(level-1)
            self.right.cut(level-1)

    def mirror(self):
        """
        Method mirrors all the branches in the tree(and subtrees).
        :return: None
        """
        if not self.empty:
            self.left, self.right = self.right, self.left
            self.left.mirror()
            self.right.mirror()


def inorder(tree: BinaryTree) -> list:
    """
    Function performs a inorder search of the given tree, returning the list of elements of each node.
    :param tree: BinaryTree
    :return: list
    """
    if tree.empty:
        return []
    data = []
    data += inorder(tree.left)
    data += tree.data
    data += inorder(tree.right)
    return data


def preorder(tree: BinaryTree) -> list:
    """
    Function performs a preorder search of the given tree, returning the list of elements of each node.
    :param tree: BinaryTree
    :return: list
    """
    if tree.empty:
        return []
    data = []
    data += tree.data
    data += preorder(tree.left)
    data += preorder(tree.right)
    return data


def postorder(tree: BinaryTree) -> list:
    """
    Function performs a postorder search of the given tree, returning the list of elements of each node.
    :param tree: BinaryTree
    :return: list
    """
    if tree.empty:
        return []
    data = []
    data += postorder(tree.left)
    data += postorder(tree.right)
    data += tree.data
    return data


def height(tree: BinaryTree) -> int:
    """
    Function calculates the height of the given tree, where height = num. of levels
    :param tree: BinaryTree
    :return: int
    """
    if tree.empty:
        return 0
    else:
        if tree.left.empty:
            left_height = 0
        else:
            left_height = height(tree.left)
        if tree.right.empty:
            right_height = 0
        else:
            right_height = height(tree.right)
        return max(left_height, right_height)


def is_leaf(tree: BinaryTree) -> bool:
    """
    Function determines if the given binary tree is a leaf(Does not have child's)
    :param tree: BinaryTree
    :return: bool
    """
    return (not tree.empty) and tree.right.empty and tree.left.empty


def number_of_leafs(tree: BinaryTree) -> int:
    """
    Function calculates the number of leafs of given tree
    :param tree: BinaryTree
    :return: int
    """
    if tree.empty:
        return 0
    elif is_leaf(tree):
        return 1
    return number_of_leafs(tree.left) + number_of_leafs(tree.right)

