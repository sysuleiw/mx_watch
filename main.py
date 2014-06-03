# coding:utf8
from livereload import Server
from common import Config

# 启动livereload监控
if __name__ == "__main__":
    server = Server()
    for file in Config.watch_file_path:
        server.watch(file)
    server.serve()
