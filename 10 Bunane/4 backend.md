# 0 备忘录

**​“获得一次完整、可部署、可写进简历的企业级项目经验”​**​
**​“获得来自一线技术专家校友的1对1代码指导和架构评审”​**​
**​“掌握Git协作、敏捷开发、CI/CD等课堂上难以学到的工程化流程”​**

# 0 临时
| HTTP 方法 | 描述     | 幂等性 | 安全性 |
| ------- | ------ | --- | --- |
| GET     | 获取资源   | 是   | 是   |
| POST    | 创建新资源  | 否   | 否   |
| PUT     | 更新整个资源 | 是   | 否   |
| PATCH   | 部分更新资源 | 否   | 否   |
| DELETE  | 删除资源   | 是   | 否   |

# 1 常用
```shell
go mod init github.com/Bunane-Tech/backend

go get -u github.com/gofiber/fiber/v2
go get -u github.com/spf13/viper 			# 配置管理库
go get -u go.uber.org/zap					# 高性能日志库
go get -u entgo.io/ent/cmd/ent				# ORM框架
go get -u github.com/go-sql-driver/mysql	# mysql driver
```

```shell
go run -mod=mod entgo.io/ent/cmd/ent new User

# 重新初始化Ent生成配置
go run entgo.io/ent/cmd/ent new --target ./ent/schema 

# 生成代码
go generate ./ent
```

# 2 Zap语法

## 2.1 基本日志记录​
```go
// 记录不同级别的日志
zap.L().Debug("Debug message")   // 调试信息
zap.L().Info("Info message")      // 常规信息
zap.L().Warn("Warning message")   // 警告
zap.L().Error("Error message")    // 错误
zap.L().Fatal("Fatal message")    // 致命错误（会调用 os.Exit(1)）
```
## 2.2 结构化字段​
```go
zap.L().Info("User login",
    zap.String("username", "john_doe"),   // 字符串字段
    zap.Int("attempt", 3),                // 整数字段
    zap.Bool("success", true),            // 布尔字段
    zap.Error(errors.New("some error")),  // 错误字段（自动记录 error 内容）
)
```
输出示例(JSON格式)：
```json
{"level":"info","ts":1630000000,"msg":"User login","username":"john_doe","attempt":3,"success":true,"error":"some error"}
```
## 2.3 记录错误​
```go
if err := someFunction(); err != nil {
    zap.L().Error("Operation failed", zap.Error(err)) // 记录 error 对象
}
```
# 3 Ent语法
```go
edge.From("problem", Problem.Type).  // 定义关系起点
    Ref("submissions").              // 目标实体的反向引用名称
    Field("problem_id").             // 数据库中外键字段名
    Required().                      // 必须存在关联
    Immutable().                     // 创建后不可修改
    Unique()                         // 一对一关系
```
# 4 文档工具

**VS Code​**​: 安装名为 ​**​`Markdown All in One`​**​ 的强大插件。它提供了 `Ctrl+Shift+P` -> `Create Table of Contents` 命令，可以自动生成和更新目录。


# 5 前端数据交互
```vue3
const value = ref('')
async function getList(){
    const res = await axios({
        url: '/list',
        method: 'GET'
    })
    list.value = res.data
}

async function add(){
    const res = await axios({
        url: '/add',
        method: 'POST',
        data: {
            value: value.value
        }
    })
    getList
}
```
https://www.bilibili.com/video/BV1rM4m117Ry/?spm_id_from=333.337.search-card.all.click&vd_source=4f10315acd30a6491a3fb1f267a3a517