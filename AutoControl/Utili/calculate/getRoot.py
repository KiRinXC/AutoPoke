import os
import sys

def get_root():
    # 获取当前文件的目录
    if getattr(sys, 'frozen', False):
        # 如果是打包后的目录，则直接选择当前目录
        root_dir ="./"
    else:
        # 否则当前目录为函数所在的位置
        current_dir = os.path.abspath(__file__)
        root_dir = current_dir
        for _ in range(4):
            root_dir = os.path.dirname(root_dir)
        root_dir = os.path.join(root_dir, 'scripts')

    if os.path.exists(root_dir):
        # print(f"目录 '{root_dir}' 存在。")
        return root_dir
    else:
        print(f"目录 '{root_dir}' 不存在。")
        return None

