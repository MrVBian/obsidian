# WorkBuddy
```json
{
  "models": [
    {
      "id": "gpt-6-astra",
      "name": "gpt-6-astra",
      "vendor": "OpenAI",
      "apiKey": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d",
      "url": "https://tks.air-class.com/v1/chat/completions",
      "maxInputTokens": 200000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "supportsReasoning": true
    },
    {
      "id": "gpt-5.6-sol",
      "name": "gpt-5.6-sol",
      "vendor": "OpenAI",
      "apiKey": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d",
      "url": "https://tks.air-class.com/v1/chat/completions",
      "maxInputTokens": 200000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "supportsReasoning": true
    },
    {
      "id": "gpt-5.6-terra",
      "name": "gpt-5.6-terra",
      "vendor": "OpenAI",
      "apiKey": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d",
      "url": "https://tks.air-class.com/v1/chat/completions",
      "maxInputTokens": 200000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "supportsReasoning": true
    },
    {
      "id": "gpt-5.6-luna",
      "name": "gpt-5.6-luna",
      "vendor": "OpenAI",
      "apiKey": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d",
      "url": "https://tks.air-class.com/v1/chat/completions",
      "maxInputTokens": 200000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "supportsReasoning": true
    },
    {
      "id": "gpt-5.5",
      "name": "gpt-5.5",
      "vendor": "OpenAI",
      "apiKey": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d",
      "url": "https://tks.air-class.com/v1/chat/completions",
      "maxInputTokens": 200000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "supportsReasoning": true
    }
  ]
}
```
# GPT DeskTop
## 1 codex model provider
| 系统            | 路径                                          |
| ------------- | ------------------------------------------- |
| macOS / Linux | `~/.codex/config.toml`                      |
| Windows       | `C:\Users\%USERPROFILE%\.codex\config.toml` |
请确保以下内容位于 config.toml 文件的开头部分
```tolm
model_provider = "OpenAI"
model = "gpt-5.6-sol"
review_model = "gpt-5.6-sol"
model_reasoning_effort = "xhigh"
disable_response_storage = true
network_access = "enabled"
windows_wsl_setup_acknowledged = true

[model_providers.OpenAI]
name = "OpenAI"
base_url = "https://tks.air-class.com"
wire_api = "responses"
supports_websockets = true
requires_openai_auth = true

[features]
responses_websockets_v2 = true
goals = true
```
## 2 配置 auth api key
| 系统            | 路径                                        |
| ------------- | ----------------------------------------- |
| macOS / Linux | `~/.codex/auth.json`                      |
| Windows       | `C:\Users\%USERPROFILE%\.codex\auth.json` |
加入apikey
```json
{
  "OPENAI_API_KEY": "sk-3ac37a18695ffd3a9b240f4cd90c0916b8a5511ee48e090bf747e981a825542d"
}
```

