# PPTParse

[English](#pptparse) | [中文](#中文)

PPTParse is a Python library for parsing and building PowerPoint presentations (.pptx files).

### Features

- Parse PowerPoint files into structured data
- Support converting structured data back to PowerPoint files
- Support various shapes including images, text boxes, groups, placeholders, etc.
- Rich HTML export interface (extensible)
- Compatible with python-pptx, supports custom shape processing

### Installation

Python 3.10 or higher is recommended.

```bash
git clone https://github.com/Force1ess/PPTParse.git
cd PPTParse
pip install -e .
```

### Usage Example

```python
from pptparse import Presentation, Config
from copy import deepcopy
from dataclasses import asdict
from dacite import from_dict

# Load presentation
config = Config("/tmp")
prs = Presentation.from_file("test.pptx", config)

# Parse to dict
prs_attrs = asdict(deepcopy(prs))
print(prs_attrs)

# Convert dict back to Presentation object and save
prs = from_dict(data_class=Presentation, data=prs_attrs)
prs.save("test_output.pptx")

# Export as pseudo-HTML code
print(prs.to_html())
```

---


## 中文

PPTParse 是一个用于解析和构建 PowerPoint 演示文稿（.pptx 文件）的 Python 工具库。

### 特性

- 解析 PowerPoint 文件为结构化数据
- 支持将结构化数据还原为 PowerPoint 文件
- 支持图片、文本框、分组、占位符等多种形状
- 丰富的 HTML 导出接口（可扩展）
- 兼容 python-pptx，支持自定义 shape 处理

### 安装

建议使用 Python 3.10 及以上版本。

```bash
git clone https://github.com/Force1ess/PPTParse.git
cd PPTParse
pip install -e .
```

### 使用示例

```python
from pptparse import Presentation, Config
from copy import deepcopy
from dataclasses import asdict
from dacite import from_dict

# 加载演示文稿
config = Config("/tmp")
prs = Presentation.from_file("test.pptx", config)

# 解析为 dict
prs_attrs = asdict(deepcopy(prs))
print(prs_attrs)

# dict 转回 Presentation 对象并保存
prs = from_dict(data_class=Presentation, data=prs_attrs)
prs.save("test_output.pptx")

# 导出为 伪HTML代码
print(prs.to_html())
```
