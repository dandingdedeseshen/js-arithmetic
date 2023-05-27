import jieba

seg_str = "好好学习，天天向上。"

print("/".join(jieba.lcut(seg_str)))