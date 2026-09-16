import json
import os

# 数据文件路径
DATA_FILE = "students.json"


def load_data():
    """
    从 JSON 文件加载数据，如果文件不存在或格式错误，返回空列表
    """
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("警告：数据文件损坏，已重置为空列表")
        return []
    except Exception as e:
        print(f"读取文件出错：{e}，已重置为空列表")
        return []


def save_data(data):
    """
    将数据保存回 JSON 文件
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("数据已保存。")
    except Exception as e:
        print(f"保存文件出错：{e}")


def show_students(data):
    """
    展示所有学生信息
    """
    if not data:
        print("当前没有学生数据。")
        return
    print("\n--- 学生成绩列表 ---")
    for idx, stu in enumerate(data, 1):
        print(f"{idx}. 姓名: {stu['name']}, 成绩: {stu['score']}")
    print("--------------------\n")


def add_student(data):
    """
    添加学生信息
    """
    name = input("请输入学生姓名：").strip()
    if not name:
        print("姓名不能为空。")
        return
    try:
        score = float(input("请输入学生成绩："))
    except ValueError:
        print("输入错误：成绩必须是数字。")
        return

    data.append({"name": name, "score": score})
    print(f"已添加：{name} - {score}")


def main():
    # 启动时先加载数据
    students = load_data()

    while True:
        print("\n=== 学生成绩管理系统 ===")
        print("1. 显示所有学生")
        print("2. 添加学生")
        print("3. 保存并退出")
        print("4. 直接退出（不保存）")

        choice = input("请输入选项 (1-4)：").strip()

        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            save_data(students)
            print("已退出。")
            break
        elif choice == "4":
            print("已退出（未保存）。")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()