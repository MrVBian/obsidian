
```go
# 初始化工程
go mod init aichimili.com/demo

# 增加依赖
go get github.com/gofiber/fiber/v2
# 更新依赖
go get -u github.com/gofiber/fiber/v2

# 清理无效下载需要依赖
go mod tidy

go run server.go
```
