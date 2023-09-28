class NoArvore:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def criar_arvore():
    
    A = NoArvore('A')
    B = NoArvore('B')
    C = NoArvore('C')
    D = NoArvore('D')
    E = NoArvore('E')
    F = NoArvore('F')
    G = NoArvore('G')
    H = NoArvore('H')
    I = NoArvore('I')
    
  
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    E.left = H
    F.left = I

    return A  

def postorder(node):
    if node is None:
        return {}

    left = postorder(node.left)
    right = postorder(node.right)

    result = {**left, **right}
    result[id(node)] = node.value

    return result

def reverse_postorder(node):
    if node is None:
        return {}

    left = reverse_postorder(node.left)
    right = reverse_postorder(node.right)

    result = {id(node): node.value}
    result.update(left)
    result.update(right)

    return result

def max_altura(node):
    if node is None:
        return -1

    left_height = max_altura(node.left)
    right_height = max_altura(node.right)

    return 1 + max(left_height, right_height)

def min_altura(node):
    return max_altura(node) - 3

if __name__ == "__main__":
    root = criar_arvore()
    
    print("Resultado da pesquisa em pós-ordem:")
    post_order_result = postorder(root)
    print(post_order_result)
    
    print("\nResultado da pesquisa em pós-ordem reversa:")
    reverse_post_order_result = reverse_postorder(root)
    print(reverse_post_order_result)
    
    print("\nAltura mínima da árvore:", min_altura(root))