# Interface_automation
**接口自动化**
使用requests库去请求csv中的接口，将测试报告重写到csv中。
`使用说明：`
1、启动web.py,进入http://ip:port页面
2、下载csv模板，将接口信息填入
3、将填写好的csv上传提交
4、在web页面将通用headers填写，json格式：{"authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVkZDI1NDM2ZmEzZmYyMGY1ZmE0MDhlMyIsInJvbGUiOiJzdHVkZW50IiwiaWF0IjoxNTc2NTU0MTc5LCJleHAiOjE1NzY2NDA1Nzl9.GAEqjh92lQH-JDjVXZD3OWjHjEsCOiF6dt7xIVjhy84"}
5、点击go开始执行csv中接口批量请求
6、执行完毕后，可进入测试报告页查看结果，也可下载csv查看。
7、已经接入并配置好钉钉机器人，会接收到通知
**本项目可通过定时请求http://ip:port/start接口监控生产环境接口状态**