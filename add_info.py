#!/usr/bin/env python3
#----------------------------------------------------------
#   Name: add_info.py
#   Author: xyy15926
#   Created at: 2019-08-31 13:14:40
#   Updated at: 2019-08-31 13:27:39
#   Description:
#----------------------------------------------------------

import sys
import os
import time
import argparse
from shutil import copy

def _add_info(file):

    print(file)

    cat_dict = {
        "cs_algorithm": "算法",
        "cs_cppc": "C/C++",
        "cs_java": "Java",
        "cs_program": "程序",
        "cs_python": "Python",
        "cs_rust": "Rust",
        "cs_web": "Web",
        "linux": "Linux",
        "math_algebra": "代数",
        "math_analysis": "分析",
        "math_probability": "概率论",
        "math_mixin": "最优化",
        "ml_models": "模型",
        "ml_techniques": "机器学习",
        "ml_specifications": "机器学习",
        "stat_rlang": "R语言",
        "stat_statistics": "统计",
        "tools": "工具",
        "zzdaily": "日常",
        "data_structure": "数据结构",
        "scala": "Scala",
        "db_optimization":"数据库优化",
        "character": "字符",
        "parallel": "并行",
        "program_design": "程序设计",
        "network": "网络",
        "keras": "Keras",
        "numpy": "Numpy",
        "pandas": "Pandas",
        "py3ref": "Py3Ref",
        "tensorflow": "Tensorflow",
        "bash_prog": "Bash编程",
        "shell":"Shell命令",
        "abstract_algebra": "抽象代数",
        "linear_algebra":"线性代数",
        "fourier_analysis":"傅里叶分析",
        "real_analysis": "实分析",
        "functional_analysis": "泛函分析",
        "constrained_optimization":"约束优化",
        "heuristics_algorithms": "启发式优化",
        "unconstrained_optimization": "无约束优化",
        "linear_models": "线性模型",
        "model_components": "模型组件",
        "model_enhancement": "增强模型",
        "nolinear_models": "非线性模型",
        "unsupervised_models": "无监督模型",
        "computer_vision": "CV",
        "graph_analysis": "社会网络",
        "natural_language_processing": "NLP",
        "rec_system": "推荐系统",
        "data_handling": "数据处理",
        "compiler_chain": "编译工具",
        "git": "Git",
        "hadoop": "Hadoop",
        "nosql_db": "NoSQLDB",
        "spark": "Spark",
        "sql_db": "SQLDB",
        "vim": "VIM"
    }

    path = os.path.dirname(file).strip("./\\").split("/")
    cats = []
    for p in path:
        if p in cat_dict:
            cats.append(cat_dict[p])
    created_at = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(os.path.getctime(file))
    )
    updated_at = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(os.path.getmtime(file))
    )

    tags = ""
    for i in cats:
        tags += f"  - {i}\n"
    tags = tags.strip("\n")

    f = open(file, "r+", encoding="utf8")
    title = f.readline()
    rtitle = title.strip("\t \n#")
    rtitle = rtitle.replace("*", "")
    # abt = []
    # for i in f:
    #     _tmp = f.readline().strip("\n")
    #     if _tmp.startswith("#"):
    #         break
    #     abt.append(_tmp)
    # abt_str = "\n".join(abt)

    header = rf"""---
title: {rtitle}
tags:
{tags}
categories:
{tags}
date: {created_at}
updated: {updated_at}
toc: true
mathjax: true
comments: true
description: {rtitle}
---
"""
    old = f.read()
    f.seek(0)
    f.write(header)
    f.write(old)

    f.close()

def add_info(source="source/_posts"):
    for d, _, fs in os.walk(source):
        for f in fs:
            if f.endswith("md"):
                _add_info(os.path.join(d, f))

def mv_imgs(source="source/_posts", dest="source/imgs"):
    imgl = os.listdir(dest)
    for d, _, fs in os.walk(source):
        for f in fs:
            if f[-3:] in ["png", "jpg", "epg", "svg"] and \
                    f not in imgl:
                print(f)
                copy(os.path.join(d, f), dest)


def replace_imgs(source="source/_posts"):
    for d, _, fs in os.walk(source):
        for f in fs:
            if f.endswith("md"):
                print(f)
                with open(os.path.join(d, f), "r+",
                          encoding="utf8") as fp:
                    buf = fp.read()
                    fp.seek(0)
                    fp.write(buf.replace("(imgs", "(/imgs"))

def recover_imgs(source="source/_posts"):
    for d, _, fs in os.walk(source):
        for f in fs:
            if f.endswith("md"):
                print(f)
                with open(os.path.join(d, f), "r+",
                          encoding="utf8") as fp:
                    buf = fp.read()
                    fp.seek(0)
                    fp.write(buf.replace("(/imgs", "(imgs"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--mv_imgs",
            action="store_const",
            const="mv_and_rep",
            default="rec",
            help="cp the images from source/_posts to"
                "source/imgs, and replace imgs link in"
                "markdown(default: recover imgs link)"
    )

    args, _ = parser.parse_known_args()
    if args.mv_imgs == "mv_and_rep":
        mv_imgs(source="source/_posts", dest="source/imgs")
        replace_imgs(source="source/_posts")
    else:
        recover_imgs(source="source/_posts")


