# 简介
获取PDF文件的书签toml配置文件。
# 安装依赖
## 安装 Python3
## 安装依赖
```bash
pip3 install -r requirements.txt
```

# 使用命令
```bash
./get_bookmarks.py <pdf_file> <out_toml_file>
```

+ pdf_file：pdf 文件路径
+ out_toml_file：pdf 的书签配置，toml文件输出位置

# 书签配置
toml格式配置

+ name：书签名称
+ page：书签页码，页码从 1 开始
+ children：嵌套书签列表

例如：

```toml
[[bookmarks]]
  name = "目录"
  page = 8

[[bookmarks]]
  name = "第一章"
  page = 12
  [[bookmarks.children]]
    name = "第一节"
    page = 12
  [[bookmarks.children]]
    name = "第二节"
    page = 34

[[bookmarks]]
  name = "第二章"
  page = 88
  [[bookmarks.children]]
    name = "第一节"
    page = 88

[[bookmarks]]
  name = "附录I"
  page = 366

[[bookmarks]]
  name = "附录II"
  page = 370

[[bookmarks]]
  name = "习题答案与提示"
  page = 383
  [[bookmarks.children]]
    name = "第一章"
    page = 383
  [[bookmarks.children]]
    name = "第二章"
    page = 389
```
