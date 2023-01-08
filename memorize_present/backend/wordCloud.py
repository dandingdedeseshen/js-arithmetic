import re
import jieba
import jieba.analyse
from wordcloud import WordCloud
import cv2

content = open(u'asset/sadf.txt','r').read()
# 处理文本数据，获得所有文字
str = ""
res = re.findall('[\u4e00-\u9fa5]+', content)
str = str.join(res)
# 去掉频率太高的词汇
stop_words = ['你', '我', '的', '了', '们', '嗯', '吧', '吗', '呀', '呢']
for word in stop_words:
  str = str.replace(word, '')
# jieba分词
seg_list = [list(jieba.cut(str,cut_all=False))][0]
seg_list = ' '.join(seg_list)
# 分析权重
tag = jieba.analyse.extract_tags(sentence=str, topK=20, withWeight=True)
# 词云背景
im = cv2.imread(u'asset/123.png')
# 设置参数，创建WordCloud对象
wc = WordCloud(
  font_path='msyh.ttc',
  background_color='white',    # 设置背景颜色为白色
  stopwords=stop_words,        # 设置禁用词，在生成的词云中不会出现set集合中的词
  mask=im
)
# 生成词云
wc.generate(seg_list)
# 保存词云文件
wc.to_file('img.jpg')