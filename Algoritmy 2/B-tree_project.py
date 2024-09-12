t = 2

def make_list(length: int):
    lst = [None]
    for i in range(0, length):
        lst += [None]
    return lst


class Node:
    keys = make_list(t * 2 - 1)
    children = make_list(2 * t)
    parent = None
    n = 0
    leaf = False


def b_tree_search(x, k):
    i = 0
    while i < x.n and k > x.keys[i]:
        i += 1
    if i < x.n and k == x.keys[i]:
        return k
    elif x.leaf:
        return False
    else:
        b_tree_search(x.children[i], k)


def split_child(x, i):
    z = Node()
    y = x.children[i]
    z.leaf = y.leaf
    z.n = t - 1
    y.n = t - 1

    for j in range(0, t - 1):
        z.keys[j] = y.keys[j + t]

    if not y.leaf:
        for j in range(0, t):
            z.children[j] = y.children[j + t]

    for j in range(x.n - 1, i + 1, -1):
        x.keys[j + 1] = x.keys[j]
        z.children[j] = y.children[j + t]

    for j in range(x.n, i + 2, -1):
        x.children[j + 1] = x.children[j]

    z.leaf = True
    x.children[i + 1] = z
    x.keys[i] = y.keys[t - 1]
    x.n = x.n + 1


def tree_insert(x, k):
    r = x
    if r.n == 2 * t - 1:
        s = Node()
        x = s
        s.leaf = False
        s.n = 0
        s.children[0] = r
        split_child(s, 0)
        tree_insert_nonfull(s, k)
    else:
        tree_insert_nonfull(r, k)


def tree_insert_nonfull(x, k):
    i = x.n - 1
    if x.leaf:
        while i >= 0 and k < x.keys[i]:
            x.keys[i + 1] = x.keys[i]
            i = i - 1
        x.keys[i + 1] = k
        x.n = x.n + 1
    else:
        while i >= 0 and k < x.keys[i]:
            i = i - 1
        i = i + 1
        if x.children[i].n == 2 * t - 1:
            split_child(x, i)
            if k > x.keys[i]:
                i = i + 1
        tree_insert_nonfull(x.children[i], k)


def return_empty_tree():
    x = Node()
    x.leaf = True
    x.n = 0
    return x


b_tree = return_empty_tree()

tree_insert(b_tree, 2)
tree_insert(b_tree, 1)
tree_insert(b_tree, 4)
tree_insert(b_tree, 3)
tree_insert(b_tree, 6)
tree_insert(b_tree, 8)
tree_insert(b_tree, 7)
tree_insert(b_tree, 12)
tree_insert(b_tree, 15)
tree_insert(b_tree, 13)
tree_insert(b_tree, 16)
tree_insert(b_tree, 19)
print(b_tree_search(b_tree, 5))
print(b_tree_search(b_tree, 12))