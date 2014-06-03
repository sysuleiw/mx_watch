#mx监控server端程序

###监控文件配置
1. 监控文件更新在common.py文件下,更改watch_file_path数组内容即可,需要注意的是livereload本身无法监控新增文件,只能监控文件的删除和修改

2. 建议所有被监控文件以相对路径存放,方便大家使用

###本程序使用
1. 首先保证服务器开放此服务相关端口或关闭防火墙

2. 首先在server安装livereload插件,详细可了解这里[https://github.com/lepture/python-livereload]

3. 执行`` python mx_watch.py ``

4. 在被刷新的网页中插入``<script src='服务器ip:port/livereload.js'></script>``

5. 只要被监控的文件有改动,那么客户端浏览器中引用到livereload.js的页面均会自动刷新


###服务器重启自执行
1. 可以在服务器启动过程中加入相关的重启命令
