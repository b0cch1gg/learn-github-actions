# check_system.py

def kiem_tra_ket_noi(dia_chi_ip):
    # Giả lập một hàm kiểm tra kết nối mạng đơn giản
    print(f"Đang kiểm tra kết nối đến {dia_chi_ip}...")
    return True

print("--- BẮT ĐẦU CHẠY KIỂM THỬ TỰ ĐỘNG ---")

# Dùng lệnh assert để ép bài test. Nếu kết quả là False, chương trình sẽ báo lỗi và dừng lại.
assert kiem_tra_ket_noi("192.168.1.1") == True, "LỖI: Không thể kết nối đến hệ thống!"

print("--- KIỂM THỬ THÀNH CÔNG! HỆ THỐNG HOẠT ĐỘNG TỐT ---")
