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

```go
edge.From("problem", Problem.Type).  // 定义关系起点
    Ref("submissions").              // 目标实体的反向引用名称
    Field("problem_id").             // 数据库中外键字段名
    Required().                      // 必须存在关联
    Immutable().                     // 创建后不可修改
    Unique()                         // 一对一关系
```

**VS Code​**​: 安装名为 ​**​`Markdown All in One`​**​ 的强大插件。它提供了 `Ctrl+Shift+P` -> `Create Table of Contents` 命令，可以自动生成和更新目录。

备忘录：
- Prefork 可以通过利用多个 CPU 核心来提高性能。
- Dockerfile  Judge镜像压缩

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