def dem_so_cach_doi_tien(S, coins):
    # 1. Khởi tạo mảng dp với S+1 phần tử
    # dp[i] sẽ lưu số cách để tạo ra tổng i
    dp = [0] * (S + 1)
    
    # 2. Quy tắc cơ sở: Có 1 cách để tạo ra tổng 0 (không dùng đồng nào)
    dp[0] = 1
    
    # 3. Lặp qua từng mệnh giá tiền
    for coin in coins:
        # 4. Cập nhật mảng dp cho các số tiền từ 'coin' đến 'S'
        for j in range(coin, S + 1):
            # Số cách mới = Số cách cũ + Số cách tạo ra (j - coin)
            dp[j] = dp[j] + dp[j - coin]
            
    # 5. Kết quả nằm ở dp[S]
    return dp[S]

# Ví dụ
S = 5
coins = [1, 2, 5]
so_cach = dem_so_cach_doi_tien(S, coins)
print(f"Số cách khác nhau để đổi {S} đồng là: {so_cach}") 
# Output: Số cách khác nhau để đổi 5 đồng là: 4