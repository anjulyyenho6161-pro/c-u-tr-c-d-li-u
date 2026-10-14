class Node:#một nút
    def __init__(self,data):
        self.data=data#truyền dữ liệu vào dta cuối
        self.next=None#con trỏ tới vị trí kế tiếp
class DSLK:#một danh sách
    def __init__(self):
        self.head=None
    def themdau(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def inds(self):
        p=self.head
        while p is not None:
            print(p.data,end="-")
            p=p.next
        print("None")


ds=DSLK()
ds.themdau(3)
ds.themdau(9)
ds.themdau(5)
ds.themdau(1)
ds.inds()



