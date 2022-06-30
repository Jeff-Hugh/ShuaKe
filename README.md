# 刷视频
网站：广西专业技术人员继续教育信息管理系统

专业技术人员评职称时需要刷供需科目的学时，系统会强制看视频，并且视频播放时无法加速，即使通过js代码可以加速视频，但是系统不会进行学时记录。

此程序登录后可以代替所有鼠标点击操作，无需值守在电脑旁。

## 环境

1. Python 3.10，其他版本没试过。

2. Windows系统运行，其他平台没有试过。

## 安装依赖

```
pip install selenium==4.3.0
```

### 1. 如果使用 Chrome 浏览器

安装依赖

```
pip install webdriver-manager==3.7.1
```
### 2. 如果使用 Edge 浏览器

从 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ 下载安装 msedgedriver ，将 msedgedriver.exe 添加到 Path 环境变量中。


## 配置文件
建一个名为 _config.json_ 的配置文件，文件内容如下：

```json
{
    "Username":"身份证号",
    "Password":"密码",
    "video_time":15,
    "Browser":"Edge",
    "Years":"2022,2021,2020,2019"

}
```
一般视频的播放时间不会超过15分钟，所以可以保持 _video_time_ 为 15 分钟。

Browser 可以填 Edge 或者 Chrome ，Firefox 暂时没有测试成功。

Years 填还没有刷的年份，用逗号隔开。可以只填一个。

## 运行程序
输入命令
```
python Shua.py
```
然后在打开的浏览器中输入验证码，回到命令窗口，按下 Enter 键，此后程序自动运行无需操作。

程序运行后浏览器和命令控制窗口都可以最小化，保持后台运行即可。每过 _video_time_ 分钟就会打开一个新的视频窗口并最小化。

如果验证码输入错误，关闭所有浏览器，结束命令窗口程序，重新执行以上步骤。