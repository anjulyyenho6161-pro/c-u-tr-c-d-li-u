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
    def themcuoi(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        p=self.head
        while p.next is not None:#last.next
            p=p.next
        p.next=new_node
    def chiahetcho2(self):
        if self.head is None:
            return
        print('danh sách các số chia hết cho 2: ')
        p=self.head
        tong=0
        while p:
            if p.data % 2==0:
                print(p.data, end="-")
                tong+=p.data
            p= p.next
        print("tong",tong)
    def timkiem(self,x):
        if self.head is None:
            return None
        p=self.head
        while p:#p is not None
            if p.data ==x:
                return p
            p=p.next
        return None

    def sapxep(self):
        if self.head is None:
            return None

        p = self.head
        while p:
            q = p.next
            while q:
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                q = q.next
            p = p.next
    def xoapt(self,y):# xóa 1 phần tử
        if self.head is None:
            return
        if self.head.data==y:
            self.head=self.head.next
            return
        p=self.head
        while p.next is not None:
            if p.next.data==y:
                p.next=p.next.next
                return
            p=p.next
        return False

    def Xoapt(self, x):#xoá nhiều phần tử
        # Xóa tất cả các node đứng đầu nếu chúng có giá trị bằng x
        while self.head is not None and self.head.data == x:
            self.head = self.head.next

        if self.head is None:
            return False

        # Duyệt qua các node tiếp theo để xóa các giá trị x còn lại
        p = self.head
        deleted = False
        while p.next is not None:
            if p.next.data == x:
                p.next = p.next.next  # Bỏ qua node có giá trị x
                deleted = True
            else:
                p = p.next  # Chỉ di chuyển tiếp khi không xóa (để tránh bỏ sót node liên tiếp)
        return deleted

    def xoatatcapt(self, x):
        # 1. Xóa các node đầu danh sách nếu bằng x
        while self.head is not None and self.head.data == x:
            self.head = self.head.next

        if self.head is None:
            return False

        # 2. Xóa các node ở giữa hoặc cuối danh sách
        p = self.head
        tim = False
        while p.next is not None:
            if p.next.data == x:
                p.next = p.next.next
                tim = True
            else:
                p = p.next
        return tim

    def themsau(self, x, y):
        # Tìm node có giá trị bằng x
        p = self.head
        while p is not None:
            #duyệt đến hết danh sách
            if p.data == x:
                # Tạo node mới chứa giá trị y
                new_node = Node(y)
                # Chèn node mới vào sau p
                new_node.next = p.next
                p.next = new_node
                return True  # Thêm thành công
            p = p.next

        print(f"Không tìm thấy giá trị {x} trong danh sách.")
        return False  # Không tìm thấy x




ds=DSLK()

ds.themdau(3)
ds.themdau(9)
ds.themdau(5)
ds.themdau(1)
ds.inds()
ds1=DSLK()
ds1.themdau(8)
ds1.themdau(6)
ds1.inds()
ds2=DSLK()
n=10
for i in range(1,n+1):#range(n)  ds2.themdau(i+1)
    ds2.themdau(i)
ds2.inds()
n=20
for i in range(1,n+1):
    if i%3==0:
        ds2.themcuoi(i)
ds2.inds()
# ds2.chiahetcho2()
# x=int(input("nhập vào giá trị x: "))
# kq=ds2.timkiem(x)
# if kq is not None:
#     print(f"tìm thấy {x} trong ds2")
# else:
#     print(f"không tim thấy {x} trong ds2 ")
# print('ds2 trước khi sắp xếp')
# ds2.inds()
# ds2.sapxep()
# print("ds2 sau khi sắp xếp")
# ds2.inds()
ds2.xoapt(10)
ds2.inds()
ds2.themsau(7,10)
ds2.inds()
ds2.xoatatcapt(6)
ds2.inds()













