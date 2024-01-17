# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : rename_files
  Description : 一次性更改整个文件夹中的文件名称（ChatGPT）
  Author      : chenyushencc@gmail.com
  date        : 2024/1/10 11:03
-------------------------------------------------
"""

import os


def rename_files_in_folder(folder_path, new_prefix):
    """
    自定义前缀
    :param folder_path: 需要修改的文件路径
    :param new_prefix: 添加前缀
    """
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历文件并修改名称
    for old_name in files:
        # 构建新的文件名
        file_extension = os.path.splitext(old_name)[1]  # 获取文件扩展名
        new_name = f"{new_prefix}_{old_name}"

        # 构建文件的完整路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)


def rename_files_in_folder(folder_path):
    """
    每个文件加前缀  "{number}_xxxxxxx"
    :param folder_path: 需要修改的文件路径
    """
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历文件并修改名称
    count = 39
    for old_name in files:
        # 构建新的文件名
        file_extension = os.path.splitext(old_name)[1]  # 获取文件扩展名
        new_name = f"{count}_{old_name}"
        count += 1

        # 构建文件的完整路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)


if __name__ == "__main__":
    # 输入文件夹路径和新的文件名前缀
    folder_path = input("请输入文件夹路径：")
    # new_prefix = input("请输入新的文件名前缀：")

    # 调用函数进行文件重命名
    # rename_files_in_folder(folder_path, new_prefix)
    rename_files_in_folder(folder_path)

    print("文件重命名完成！")