# YouTube 视频下载器

这是一个简单的 Python 脚本，基于 `yt-dlp` 库，用于下载 YouTube 视频。

## 目录结构

- `download.py`: 下载脚本。
- `requirements.txt`: 依赖列表。

## 安装

1. 确保已安装 Python 3。
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

运行脚本并提供 YouTube 视频链接作为参数：

```bash
python download.py <视频链接>
```

示例：

```bash
python download.py https://www.youtube.com/watch?v=jNQXAC9IVRw
```

视频将下载到当前目录。
