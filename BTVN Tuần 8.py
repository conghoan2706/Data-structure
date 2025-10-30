# -------------------------------
#  CÀI ĐẶT CÂY AVL / BST
# -------------------------------

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Lấy chiều cao node
def height(root):
    if not root:
        return 0
    return root.height


# Tính hệ số cân bằng
def get_balance(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)


# Xoay phải
def rotate_right(y):
    x = y.left
    T2 = x.right

    # Thực hiện xoay
    x.right = y
    y.left = T2

    # Cập nhật chiều cao
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# Xoay trái
def rotate_left(x):
    y = x.right
    T2 = y.left

    # Thực hiện xoay
    y.left = x
    x.right = T2

    # Cập nhật chiều cao
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# -------------------------------
#  CHÈN NODE VÀO CÂY AVL
# -------------------------------
def insert(root, key):
    # Bước 1: Chèn như BST
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Tránh trùng lặp

    # Bước 2: Cập nhật chiều cao
    root.height = 1 + max(height(root.left), height(root.right))

    # Bước 3: Cân bằng lại
    balance = get_balance(root)

    # Trường hợp 1: Left Left
    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    # Trường hợp 2: Right Right
    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    # Trường hợp 3: Left Right
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Trường hợp 4: Right Left
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


# -------------------------------
#  DUYỆT IN-ORDER
# -------------------------------
def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []


# -------------------------------
#  TÌM NODE NHỎ NHẤT (successor)
# -------------------------------
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# -------------------------------
#  XÓA NODE KHỎI CÂY AVL
# -------------------------------
def delete(root, key):
    if not root:
        return root

    # Tìm node để xóa
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node có 1 hoặc 0 con
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node có 2 con → lấy successor
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    # Cập nhật chiều cao
    root.height = 1 + max(height(root.left), height(root.right))

    # Cân bằng lại
    balance = get_balance(root)

    # Các trường hợp mất cân bằng
    if balance > 1 and get_balance(root.left) >= 0:
        return rotate_right(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return rotate_left(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


# -------------------------------
#  CHƯƠNG TRÌNH CHÍNH
# -------------------------------
if __name__ == "__main__":
    arr = [50, 30, 70, 20, 40, 60, 80]

    root = None
    for val in arr:
        root = insert(root, val)

    print("In-order trước khi xóa:", inorder(root))

    root = delete(root, 30)

    print("In-order sau khi xóa 30:", inorder(root))
