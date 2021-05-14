
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

    def __repr__(self, shift=''):
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

    def __eq__(self, other):
        if self.empty and other.empty:
            return True
        elif not self.empty and not other.empty:
            return (
                    self.data == other.data and self.left == other.left and self.right == other.right)
        else:
            return False

    def __hash__(self):
        if self.empty:
            return hash(())
        else:
            return hash((self.data, self.left, self.right))
