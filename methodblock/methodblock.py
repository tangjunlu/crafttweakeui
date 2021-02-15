#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：青竹红颜
@Date    ：2021/2/10 23:12 
"""


def show_window():
    pass


# 删除配方
def recipe_remove(data):
    recipe_name = data
    remove_recipe = f"""
recipes.remove({recipe_name});
"""
    file_path = 'recipes/remove.zs'
    save_recipe(file_path, remove_recipe)


def recipe_remove_shaped(data):
    pass


# 添加无序配方
def shapeless_recipe(data):

    recipe = f"""
    recipes.addShapeless(data[],[]
    );
    """
    pass


# 添加有序配方
def shaped_recipe(data):
    num = 0
    while True:
        if data[num] == '':
            data[num] = 'null'
        num += 1
        if num == len(data):
            break
    recipe = f'''
recipes.addShaped("recipe_name", {data[0]},[
  [{data[1]},{data[2]},{data[3]}],
  [{data[4]},{data[5]},{data[6]}],
  [{data[7]},{data[8]},{data[9]}]
]);'''
    file_path = 'recipes/recipe.zs'
    save_recipe(file_path, recipe)


# 保存文件
def save_recipe(file_path, recipe):
    with open(file_path, 'a+', encoding='utf-8')as f:
        f.write(recipe)
