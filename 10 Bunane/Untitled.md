
1、测试一下编程题，超大数据判题。于涛；
2、测试一下编程题，C/Java/Python，至少一道。卞振伟；

前端UI建议反馈
3、创建题目页面
4、创建题集
5、编辑题集
-  http://123.56.117.129:10010/admin/problem/create/singlechoice
-  http://123.56.117.129:10010/admin/problem-sets/create
- http://123.56.117.129:10010/admin/problem-sets/editor


基于 Vue3 + Naive UI，实现个人中心页面，左侧是菜单栏，包含：
- 个人信息(UserProfile.vue)
    - 显示用户头像、昵称、ID、邮箱、手机号等基本信息
    - 头像上传
        - 支持点击头像打开编辑模态框。
        - 模态框中可选择预设头像或上传自定义图片。
    - 昵称编辑
        - 点击“编辑”图标进入昵称编辑状态。
        - 输入新昵称后点击“确认”图标保存。
        - 昵称更新成功后给出提示。
- 购买套餐(Purchase.vue)
    - 每条记录展示：
        - 套餐名称
        - 套餐价格
        - 套餐描述
        - 支付金额
        - 支付二维码
- 购买记录(PurchaseRecords.vue)
    - 表格展示历史订单信息
    - 包含订单号、产品名称、金额、支付时间
- 历史作品(HistoricalWorks.vue)
    - 显示作品(图片)封面和创建时间
    - 作品按照日期(天)分组展示，可以筛选日期
    - 应式设计适配不同屏幕尺寸
- 设置密码(ChangePassword.vue)
    - 表单验证旧密码、新密码和确认密码
    - 密码复杂度验证（长度6-20位）
    - 提交前验证两次输入一致性


分别由五组Vue3组件组成，集成调用。
请给出个人信息(UserProfile.vue)和购买套餐(Purchase.vue)的代码

import { UserProfile, PurchaseRecords, HistoricalWorks, ChangePassword } from "./components";




基于 Vue3 + Naive UI，实现后台管理页面，左侧是菜单栏，包含：
一、用户管理(UserMgmt.vue)
​1. ​用户列表
    - 展示所有注册用户信息（ID、昵称、邮箱、手机号、注册时间、积分）
    - 支持按邮箱/手机号搜索用户
​2. ​用户详情与操作​​
    - 查看/编辑用户基本信息（强制重置手机号/邮箱）
    - 强制密码重置​​（无需验证旧密码，适用于用户忘记密码的客服场景）
二、套餐管理(Purchase.vue)
​1. ​套餐配置​​
    - 创建/编辑套餐（套餐名称、套餐价格(原价/活动价)、套餐积分、套餐描述、支付二维码）
    - 上下架控制（控制用户端是否可购买）
三、订单管理(Order.vue)
​1. ​订单审计​​
    - 完整订单列表：订单号、关联用户、套餐名称、实付金额、支付渠道、创建/支付时间、状态（待支付/已完成/未完成）
2. 按时间范围（精确到小时）筛选
四、系统设置(System.vue)
​1. SMTP配置(SMTP 服务器地址、端口等相关配置)

分别由四组Vue3组件组成，集成调用。给出vue3组件代码和集成界面Vue3组件代码。


import { UserMgmt, Purchase, Order, System } from "./components";
