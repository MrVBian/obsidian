## Action请求接口
**请求方式：Socket**
**Topic：IP:10011**
**指令说明：请求Action**
```json
{
  "task_id": 30 
}
```
## Action响应接口
```json
{
  "type": "feedback",
  "message": "task running",
}

{
  "type": "result",
  "success": false,
  "task_id": 30,
  "result": "movement stopped",
}

{
  "type": "error",
  "message": "XXX中间件错误",
}
```

| 参数         | 参数类型    | 说明                | 实例值                    |
| ---------- | ------- | ----------------- | ---------------------- |
| type       | 消息类型    | result 或 feedback |                        |
