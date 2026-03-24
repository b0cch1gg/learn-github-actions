# Sử dụng môi trường gốc là Python 3.10
FROM python:3.10-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy file mã nguồn vào trong container
COPY check_system.py .

# Khi container khởi chạy, nó sẽ tự động chạy file này
CMD ["python", "check_system.py"]
