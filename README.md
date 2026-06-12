# 🖼️ Wallhaven 壁纸爬虫

一个基于 Python 的壁纸批量下载工具，从 [Wallhaven.cc](https://wallhaven.cc) 网站的 Toplist 热门榜单自动抓取并下载高清壁纸。

## ✨ 功能特性

- 🔥 自动抓取 Wallhaven Toplist 热门壁纸榜单
- 📄 支持批量爬取多页内容（默认 1-50 页）
- 📏 自动获取壁纸分辨率信息作为文件名
- 💾 高速下载原图质量壁纸
- ⏱️ 智能请求间隔，避免被网站封禁
- 🛡️ 异常处理机制，跳过无法获取的图片

## 📦 依赖安装

```bash
pip install requests lxml
```

## 🚀 使用方法

1. 克隆或下载本项目

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行爬虫：
   ```bash
   python main.py
   ```

4. 壁纸将自动下载到 `Wallhaven/` 文件夹中

## 📁 项目结构

```
reptile-wallpaper/
├── main.py            # 主程序
├── README.md          # 项目说明
└── Wallhaven/         # 下载的壁纸存放目录
```

## ⚙️ 配置说明

在 `main.py` 中可以修改以下参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `page_range` | 爬取的页码范围 | `range(2, 51)`（第2-50页） |
| `headers['user-agent']` | 浏览器标识 | Chrome 95 |

## 📝 工作流程

```
1. 获取列表页 HTML → 2. 提取图片详情页链接 → 3. 访问详情页 → 4. 解析原图地址 → 5. 下载保存
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
A: 修改 `main.py` 中的 `page_range` 参数，如 `range(5, 6)` 只下载第5页。

**Q: 下载速度慢？**
A: 可以删除或减少 `time.sleep()` 的时间，但可能增加被封禁风险。

## 📄 许可证

本项目仅供学习交流使用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---
# 参考内容
https://zhuanlan.zhihu.com/p/427584794