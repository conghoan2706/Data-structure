def tower_of_hanoi(n, source_peg, target_peg, aux_peg):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ cột {source_peg} sang cột {target_peg}")
        return

    tower_of_hanoi(n - 1, source_peg, aux_peg, target_peg)

    print(f"Di chuyển đĩa {n} từ cột {source_peg} sang cột {target_peg}")

    tower_of_hanoi(n - 1, aux_peg, target_peg, source_peg)


if __name__ == "__main__":
    try:
        num_disks = int(input("Nhập số đĩa bạn muốn giải: "))

        if num_disks <= 0:
            print("Vui lòng nhập một số nguyên dương.")
        else:
            print("\nCác bước để giải Tháp Hà Nội là:")
            tower_of_hanoi(num_disks, 'A', 'C', 'B')

            total_moves = 2**num_disks - 1
            print(f"\n✨ Tổng số bước di chuyển tối thiểu là: {total_moves}")

    except ValueError:
        print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")