# 🖼️ Wallhaven 壁纸爬虫

一个基于 Python 的壁纸批量下载工具，从 [Wallhaven.cc](https://wallhaven.cc) 自动抓取并下载高清壁纸，支持热榜、热门、搜索三种模式。

## ✨ 功能特性

- 🔥 支持三种运行模式：**Toplist 热榜** / **Hot 热门** / **Search 搜索**
- 🔍 搜索模式支持自定义关键词
- 📄 支持批量爬取多页内容
- 📏 自动获取壁纸分辨率信息作为文件名
- 💾 高速下载原图质量壁纸
- ⏱️ 智能请求间隔，避免被网站封禁
- 🛡️ 异常处理机制，跳过无法获取的图片
- 📁 支持按日期/关键词自动创建子文件夹
- 📝 自动生成下载日志

## 📦 依赖安装

```bash
pip install requests lxml pyyaml
```

## 🚀 使用方法

1. 克隆或下载本项目

2. 安装依赖：
   ```bash
   pip install requests lxml pyyaml
   ```

3. 编辑 `config.yaml` 配置文件（见下方配置说明）

4. 运行爬虫：
   ```bash
   python main.py
   ```

5. 壁纸将自动下载到配置的保存目录中

## 📁 项目结构

```
reptile-wallpaper/
├── main.py            # 主程序
├── config.yaml        # 配置文件
├── README.md          # 项目说明
├── logs/              # 下载日志目录
└── Wallhaven/         # 下载的壁纸存放目录
```

## ⚙️ 配置说明

所有配置项均在 `config.yaml` 中修改：

| 参数 | 说明 | 可选值/示例 |
|------|------|-------------|
| `mode` | 运行模式 | `toplist`（热榜）、`hot`（热门）、`search`（搜索） |
| `search_keyword` | 搜索关键词（仅 search 模式） | `"girl"`、`"nature"` 等 |
| `page_start` | 起始页码 | `1` |
| `page_end` | 结束页码 | `50` |
| `save_dir` | 壁纸保存目录 | `Wallhaven` 或 `D:/Wallpapers` |
| `create_date_subfolder` | 按日期创建子文件夹 | `true` / `false` |
| `create_keyword_subfolder` | 按关键词创建子文件夹（仅 search 模式） | `true` / `false` |
| `log_dir` | 日志保存目录 | `logs` |
| `request_delay_min` | 最小请求间隔（秒） | `0.5` |
| `request_delay_max` | 最大请求间隔（秒） | `2` |

### 配置示例

```yaml
# 热门模式 - 下载 Hot 热门壁纸
mode: hot
page_start: 1
page_end: 10

# 搜索模式 - 按关键词搜索
mode: search
search_keyword: "nature"
create_keyword_subfolder: true
```

## 📝 工作流程

```
1. 读取配置 → 2. 获取列表页 HTML → 3. 提取详情页链接 → 4. 解析原图地址 → 5. 下载保存 → 6. 记录日志
```

## ⚠️ 注意事项

- 请合理使用，避免过于频繁的请求对服务器造成压力
- 仅供学习交流使用，请勿用于商业用途
- 下载的壁纸版权归原作者所有
- 建议遵守网站的 robots.txt 规则

## 🐛 常见问题

**Q: 下载中断怎么办？**
A: 程序支持异常跳过，重新运行会继续下载，但已下载的文件不会重复下载。

**Q: 如何只下载特定页？**
A: 修改 `config.yaml` 中的 `page_start` 和 `page_end` 参数。

**Q: 下载速度慢？**
A: 可以减小 `request_delay_min` 和 `request_delay_max` 的值，但可能增加被封禁风险。

## 📄 许可证

本项目仅供学习交流使用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---
# 参考内容
https://zhuanlan.zhihu.com/p/427584794