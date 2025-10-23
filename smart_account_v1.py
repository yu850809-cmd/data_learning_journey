import json
from pathlib import Path

DATA=Path("account.json")

def load_records():
    if not DATA.exists():
        DATA.write_text("[]",encoding="utf-8")
    with DATA.open("r",encoding="utf-8")as f:
        return json.load(f)
    
def save_records(records):
    with DATA.open("w",encoding="utf-8")as f:
        json.dump(records,f,ensure_ascii=False,indent=2)
    print("已儲存到 account.json")

def add_record(records):
    item=input("輸入項目名稱")
    amount=int(input("輸入金額"))
    record={"項目":item,"金額":amount}
    records.append(record)
    print("已新增",record)

def show_records(records):
    print("\n---所有紀錄---")
    total =0
    for r in records:
        print(f"{r['項目']}:{r['金額']}元")
        total += r["金額"]
    print("-----------")    
    print("總支出",total,"元")

def run_menu():
    records = load_records()
    while True:
        print("\n======記帳系統======")
        print("1. 新增支出")
        print("2. 顯示所有紀錄")
        print("3. 儲存並離開")
        choice=input("請輸入選項")
        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            save_records(records)
            break
        else:
            print("請輸入正確選項")

if __name__=="__main__":
    run_menu()