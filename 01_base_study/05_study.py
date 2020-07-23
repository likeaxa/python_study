# mac 安装jieba wordcloud 需要换源 不然太慢了 参考链接
# 安装命令
# pip3 install jieba
# pip3 install wordcloud
# https://blog.csdn.net/zichen_ziqi/article/details/104449324?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# 安装过程遇见权限问题 可以用sudo 安装 eg sudo pip3 install jieba
import jieba
from wordcloud import WordCloud


s = '昨晚晚上我去干嘛了，我在家学习呢'
list = jieba.lcut(s)
print(list)
new_str = ''.join(list)
word_cloud = WordCloud().generate(s)
word_cloud.to_file('test.png')
