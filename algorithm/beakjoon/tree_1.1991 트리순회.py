import sys

def preorder(index):
    print(chr(index+64), end="")
    if tree[index][1] != '.':
        preorder(ord(tree[index][1]) - 64)
    if tree[index][2] != '.':
        preorder(ord(tree[index][2]) - 64)


def inorder(index):
    if tree[index][1] != '.':
        inorder(ord(tree[index][1]) - 64)
    print(chr(index + 64), end="")
    if tree[index][2] != '.':
        inorder(ord(tree[index][2]) - 64)

def postorder(index):
    if tree[index][1] != '.':
        postorder(ord(tree[index][1]) - 64)
    if tree[index][2] != '.':
        postorder(ord(tree[index][2]) - 64)
    print(chr(index + 64), end="")


N = int(sys.stdin.readline())
# 트리의 인덱스 : 자신의 위치
# 인덱스의 1번재 위치 : 부모, 2번재 : 왼쪽자식, 3번재 : 오른쪽자식
tree = [[0]*3 for _ in range(N+1)]
# print(ord('A'))
# print(chr(65))
for _ in range(N):
    parrent, left, right = map(str, sys.stdin.readline().split())
    tree[ord(parrent) - 64][1] = left
    tree[ord(parrent) - 64][2] = right
    if left != '.':
        tree[ord(left) - 64][0] = parrent
    if right != '.':
        tree[ord(right) - 64][0] = parrent

preorder(1)
print()
inorder(1)
print()
postorder(1)