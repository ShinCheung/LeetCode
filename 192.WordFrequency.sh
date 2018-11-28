#!/bin/sh

# 使用shell统计词频
# tr -s ' ' '\n' 是将所有连续的空格 空行删除并保证每一行只有一个字符串 
# sort | uniq -c 通常一起用来统计重复出现的次数

# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr -k 2 | awk '{print $2,$1}'