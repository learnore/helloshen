### [若依 / RuoYi-Vue 拓展功能](https://gitee.com/y_project/RuoYi-Vue)
* security_code.py
  - [x] 支持获取验证码 base64（可通过在线转换成图片） + uuid
  - [ ] 待使用Python自动识别 base64 并解出验证码
* main.py
  - [x] 支持 “uuid+验证码” 登录获取 token
  - [x] 支持使用 token 进入系统获取其他数据（这里用“获取任务数据”作为例子）
