# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制依赖清单并安装依赖
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 复制当前目录下的所有文件到工作目录
COPY . .

# 运行应用
CMD ["python", "app.py"]
