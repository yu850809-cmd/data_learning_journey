def analyze_even_numbers():
    while True:
        start=int(input("請輸入第一個數字"))
        end=int(input("請輸入第二個數字"))

        if start == end:
            print("輸入的數字無法運作,請重新輸入")
            continue
        elif start > end:
            start,end=end,start

        total=0
        count=0
        for n in range(start,end+1):
            if n % 2==0:
                total+=n
                count+=1
        average=total/count if count != 0 else  0
        return total, count ,average

data=analyze_even_numbers()
print(data[0])
print(data[1])
print(data[2])