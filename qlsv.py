#khởi tạo 1 danh sách trống để in thông tin học sinh
students = []
# tạo vòng lặp while để in menu với điều kiện chọn 0 thì kết thúc chương trình
while True: 
    print("Chào mừng thầy cô đến với phần mềm quản lí học sinh - sinh viên")
    print("--------------------------Menu-------------------------")
    print("\t|1. Thêm học sinh vào danh sách     |")
    print("\t|2. Hiện thị danh sách học sinh     |")
    print("\t|3. Tìm kiếm học sinh từ danh sách  |")
    print("\t|4. Xóa học sinh từ danh sách       |")
    print("\t|0. Thoát chương trình              |")
    print("-------------------------------------------------------")
    chucNang = int(input("Mời bạn chọn chức năng"))
    # nếu chọn chức năng 0 vòng lặp while sẽ dừng lại
    if chucNang == 0: 
        print("Thoát chương trình hoàn tất")
        break
    #thêm học sinh vào danh sách
    elif chucNang == 1:
        print("Thêm học sinh vào danh sách")
        ten = str(input("Mời bạn nhập tên học sinh"))
        lop = str(input("Mời bạn nhập tên lớp"))
        diem = float(input("Mời bạn nhập điểm trung bình"))
        # add các tiêu đề trong danh sách nhập thông tin học sinh
        students.append({"Tên": ten, "Lớp":lop,"Điểm":diem})
        print("Học sinh đã được thêm vào danh sách")
        #Hiển thị danh sách học sinh
    elif chucNang == 2:
        print(students)
        #tìm kiếm học sinh từ danh sách
    elif chucNang == 3 :
        print("Tìm kiếm học sinh từ danh sách")
        nhaphs = str(input("Mời bạn nhập tên học sinh cần tìm"))
        #Biến này được sử dụng để kiểm tra xem học sinh có tồn tại trong danh sách hay không.
        timThay = False
        for timhs in students : 
            if timhs["Tên"]==nhaphs:
                print("Học sinh có tên",nhaphs,"đã tìm thấy trong danh sách")
                print("Lớp",timhs["Lớp"])
                print("Điểm",timhs["Điểm"])
                timThay= True
                break
            else: 
                print("Học sinh",nhaphs,"không có tên trong danh sách !")
                #Xóa học sinh khỏi danh sách
    elif chucNang ==4 :
        print("Xóa học sinh ra khỏi danh sách")
        xoaTen = str(input("Mời bạn nhập tên hoc sinh muốn xóa"))
        for hsinh in students:
            if hsinh["Tên"] == xoaTen:
                students.remove(hsinh)
                print(f"Đã xóa {xoaTen} ra khỏi danh sách.")
                break
    else:
        print("Không tìm thấy học sinh có tên {xoaTen} trong danh sách.")
 