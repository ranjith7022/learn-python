# ref.py

# Reference implementation functions for Red-Black Tree operations.
# These functions OPERATE ON RBNode and RBTree objects IMPORTED FROM main.py.
# Based on CLRS (Introduction to Algorithms)

# Import the necessary classes from the user's implementation
try:
    from main import RBNode, RBTree
except ImportError:
    print("Error: Could not import RBNode and RBTree from main.py.")
    print("Ensure main.py exists and defines these classes.")
    # Define dummy classes to prevent further NameErrors during parsing,
    # but the functions will likely fail at runtime if import failed.
    class RBNode: pass
    class RBTree: pass


def left_rotate(tree, x):
    """
    Performs a left rotation on node x.
    Assumes tree is an RBTree instance from main.py
    Assumes x is an RBNode instance from main.py
    Assumes nodes have .right, .left, .parent attributes.
    Assumes tree has .nil and .root attributes.
    """
    # Check if right child exists and is not nil
    if x.right == tree.nil:
        # print("Warning: Cannot left_rotate node with nil right child.")
        return # Or raise an error, depending on desired behavior

    y = x.right
    x.right = y.left  # Turn y's left subtree into x's right subtree
    if y.left != tree.nil:
        y.left.parent = x

    y.parent = x.parent  # Link y's parent to x's parent
    if x.parent == tree.nil:
        tree.root = y  # x was root, now y is root
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x  # Put x on y's left
    x.parent = y


def right_rotate(tree, y):
    """
    Performs a right rotation on node y.
    Assumes tree is an RBTree instance from main.py
    Assumes y is an RBNode instance from main.py
    Assumes nodes have .right, .left, .parent attributes.
    Assumes tree has .nil and .root attributes.
    """
     # Check if left child exists and is not nil
    if y.left == tree.nil:
        # print("Warning: Cannot right_rotate node with nil left child.")
        return # Or raise an error

    x = y.left
    y.left = x.right  # Turn x's right subtree into y's left subtree
    if x.right != tree.nil:
        x.right.parent = y

    x.parent = y.parent  # Link x's parent to y's parent
    if y.parent == tree.nil:
        tree.root = x  # y was root, now x is root
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y  # Put y on x's right
    y.parent = x


def insert_fixup(tree, z):
    """
    Restores Red-Black properties after insertion of node z.
    Assumes tree is an RBTree instance from main.py
    Assumes z is an RBNode instance from main.py
    Assumes nodes have .parent and .red attributes.
    """
    # Check if z and its parent/grandparent exist and are not nil before accessing .red
    while z.parent != tree.nil and z.parent.red:
        # Ensure grandparent exists before proceeding
        if z.parent.parent == tree.nil:
            break # Parent is root, loop condition should have handled this? Safety check.

        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right  # Uncle node
            if y != tree.nil and y.red: # Check if uncle is nil
                # Case 1: Uncle is red -> Recolor and move up
                z.parent.red = False
                y.red = False
                z.parent.parent.red = True
                z = z.parent.parent  # Move z up to grandparent
            else: # Uncle is black (or nil, which is black)
                # Case 2: Uncle is black, z is a right child (triangle)
                if z == z.parent.right:
                    z = z.parent  # Move z up to parent
                    left_rotate(tree, z)
                    # After rotation, z points to the original parent,
                    # which is now the left child. Fall through to Case 3.
                    # z's parent and grandparent references are updated by rotate

                # Case 3: Uncle is black, z is a left child (line)
                # This check handles both original Case 3 and Case 2 after rotation
                if z.parent != tree.nil: # Check parent after potential rotation
                    z.parent.red = False
                if z.parent.parent != tree.nil: # Check grandparent after potential rotation
                    z.parent.parent.red = True
                    right_rotate(tree, z.parent.parent)
                # Need to break here? CLRS doesn't explicitly break, relies on loop condition
                # but after Case 3, the red-red violation at z is resolved locally.
                # The loop continues from the original grandparent (which became z).
                # Let's stick to CLRS structure.

        else:  # Symmetric case: z.parent is the right child
            y = z.parent.parent.left  # Uncle node
            if y != tree.nil and y.red: # Check if uncle is nil
                # Case 1: Uncle is red -> Recolor and move up
                z.parent.red = False
                y.red = False
                z.parent.parent.red = True
                z = z.parent.parent
            else: # Uncle is black (or nil)
                # Case 2: Uncle is black, z is a left child (triangle)
                if z == z.parent.left:
                    z = z.parent
                    right_rotate(tree, z)
                    # Fall through to Case 3

                # Case 3: Uncle is black, z is a right child (line)
                if z.parent != tree.nil:
                    z.parent.red = False
                if z.parent.parent != tree.nil:
                    z.parent.parent.red = True
                    left_rotate(tree, z.parent.parent)
                # Break? See comment in the symmetric case above.

        # Safety check: If z moved up to root, stop
        if z == tree.root:
            break

    # Ensure Property 2: Root is always black
    if tree.root != tree.nil:
        tree.root.red = False


def ref_implementation(tree, val):
    """
    Reference implementation logic for inserting a value into the RBTree.
    OPERATES ON the RBTree object 'tree' passed from main_test.py,
    which should be an instance of the RBTree class from main.py.
    CREATES new nodes using the RBNode class imported from main.py.
    """
    # Create the new node z using the RBNode class from main.py
    try:
        z = RBNode(val)
    except NameError:
         print("Error: RBNode class not available (likely import failed).")
         return # Cannot proceed

    z.left = tree.nil   # Use the tree's nil sentinel
    z.right = tree.nil
    z.red = True        # New node is initially red
    z.parent = tree.nil # Initialize parent to nil

    # Standard BST insertion logic
    y = tree.nil
    x = tree.root

    while x != tree.nil:
        y = x
        # Comparison assumes val has appropriate __lt__, __gt__, __eq__
        if z.val < x.val:
            x = x.left
        elif z.val > x.val:
            x = x.right
        else:
            # Handle duplicate values - ignore in this reference
            # print(f"Duplicate value {val} ignored.")
            return # Do not insert duplicate

    # Link z with its parent y
    z.parent = y
    if y == tree.nil:
        tree.root = z  # Tree was empty
    elif z.val < y.val:
        y.left = z
    else:
        y.right = z

    # If z is the root, just make it black and we're done.
    # Check parent *after* linking it.
    if z.parent == tree.nil:
        z.red = False
        return

    # If z's parent is the root (which must be black), no red-red violation.
    if z.parent.parent == tree.nil:
        return

    # Call fixup to restore Red-Black properties
    insert_fixup(tree, z)


def ref_inorder(node, result_list, nil_node = RBNode(None)):
    """
    Performs an inorder traversal on nodes (assumed to be RBNode from main.py).
    Uses the 'val' attribute and stops recursion at nil_node.
    Assumes result_list is initialized as an empty list by the caller.
    """
    # Check if the current node is the sentinel nil node
    if node is not nil_node and node is not None:
        ref_inorder(node.left, result_list, nil_node)
        # Append the value if it's not None (safety check)
        if node.val is not None:
             result_list.append(node.val)
        ref_inorder(node.right, result_list, nil_node)
    return result_list # Return the list being built
