class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self, head):
        # head 생성 
        self.head = head


    def insert_node(self, value):
        # head를 base_node에 저장 
        self.base_node = self.head

        # 무한 반복 
        while True : 
            #  value가 기준 노드보다 작은 경우 
            if value < self.base_node.value:
                # 기준 노드의 왼쪽 노드가 있는 경우 
                if self.base_node.left != None:
                    # 기준 노드의 왼쪽 노드가 새로운 기준 노드가 됨 
                    self.base_node = self.base_node.left

                # 기준 노드의 왼쪽 노드가 없는 경우 
                else:
                    # 기준 노드의 왼쪽 노드에 value 노드 추가 
                    self.base_node.left = node(value)
                    break

            # value가 기준 노드보다 큰 경우 
            else:
                # 기준 노드의 오른쪽 노드가 있는 경우 
                if self.base_node.right != None:
                    # 기준 노드의 오른쪽 노드가 새로운 기준 노드가 됨 
                    self.base_node = self.base_node.right

                # 기준 노드의 오른쪽 노드가 없는 경우 
                else:
                    # 기준 노드의 오른쪽 노드에 value 노드 추가 
                    self.base_node.right = node(value)
                    break
        

    def search_node(self, value):
        """
        bst 내부에 value값이 있는지 True / False값을 반환하는 메소드를 작성
        """
        # head를 기준 노드 변수로 저장 
        self.base_node = self.head

        # 기준 노드가 있는경우에 계속 반복 
        while self.base_node:
            # 기준 노드의 값이 value 일 경우 
            if self.base_node.value == value:
                # True 반환 
                return True
            
            # 기준 노드의 값이 value보다 큰 경우 
            elif self.base_node.value > value : 
                # 기준 노드의 왼쪽 노드가 새로운 기준 노드가 됨 
                self.base_node = self.base_node.left
            
            # 기준 노드의 값이 value보다 작은 경우 
            else : 
                # 기준 노드의 오른쪽 노드가 새로운 기준 노드가 됨 
                self.base_node = self.base_node.right
        return False


if __name__ == "__main__":
    """
    예상 입출력 확인    
                        16
                    /       \
                12              19
               /  \             /  \
            11      13         18   20
          /
        9
      /  \
    8     10
    """

    head = node(16)  
    bt = binary_search_tree(head)

    bt.insert_node(12)
    bt.insert_node(19)
    bt.insert_node(11)
    bt.insert_node(13)
    bt.insert_node(18)
    bt.insert_node(20)
    bt.insert_node(9)
    bt.insert_node(8)
    bt.insert_node(10)

    print(bt.search_node(5))    #False
    print(bt.search_node(-2))   #False
    print(bt.search_node(18))   #True