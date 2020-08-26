#!/bin/python3
import os
import re


class Color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


pattern = re.compile(r"\\*.*\\*/\n", re.MULTILINE)
old_header = """/* ************************************************************************** */
/*                                                                            */
/*   Project: minishell                                   ::::::::            */
/*   Members: dvoort, prmerku                           :+:    :+:            */
/*   Copyright: 2020                                   +:+                    */
/*                                                    +#+                     */
/*                                                   +#+                      */
/*                                                  #+#    #+#                */
/*   while (!(succeed = try()));                   ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */
"""
new_header = """/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   minishell                                          :+:    :+:            */
/*                                                     +:+                    */
/*   By: anonymous <anonymous@student.codam.nl>       +#+                     */
/*                                                   +#+                      */
/*   Created: 2020/08/26 00:00:00 by anonymous     #+#    #+#                 */
/*   Updated: 2020/08/26 00:00:00 by anonymous     ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */
"""


def replace_header(file_path):
    header = open(file_path).read()
    if re.search(pattern, header):
        header = header.replace(old_header, new_header)
        file_name = open(file_path, 'w')
        file_name.write(header)
        file_name.close()
        print(Color.RED + "Header replaced in file: " + Color.END + file_path)
    return


def search_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            if name.endswith(".c") or name.endswith(".h"):
                file_path = os.path.join(root, name)
                print(Color.YELLOW + "Replacing header in file: " + Color.END + file_path)
                replace_header(file_path)
    return


path = input(Color.GREEN + "Enter path: " + Color.END)
search_files(path)
print(Color.GREEN + "\nFINISHED\n" + Color.END)
