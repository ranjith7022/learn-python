from main import BSTNode

def ref_implementation(bst_node, user):
    """Reference implementation for inserting a user into a BST."""
    if bst_node.val is None:
        bst_node.val = user
        return

    if user < bst_node.val:
        if bst_node.left is None:
            bst_node.left = BSTNode(user)
        else:
            ref_implementation(bst_node.left, user)
    else:
        if bst_node.right is None:
            bst_node.right = BSTNode(user)
        else:
            ref_implementation(bst_node.right, user)


def ref_inorder(bst_node, result):
    """Reference implementation for inorder traversal of a BST."""
    if bst_node is not None:
        ref_inorder(bst_node.left, result)
        result.append(bst_node.val)
        ref_inorder(bst_node.right, result)
    return result
