演示：[https://vulk.cssninja.io/](https://vulk.cssninja.io/)
文档：[https://docs.cssninja.io/vulk/guide/getting-started.html](https://docs.cssninja.io/vulk/guide/getting-started.html)
[购买链接](https://themeforest.net/item/vulk-multipurpose-vue-3-ssr-sass-landing-pages-ui-kit/36586175?utm_medium=demo&utm_source=buy_vulk&_gl=1*1dgqkng*_gcl_au*MjAwNjI2NDgzMi4xNzQyODEyNDQ3*FPAU*MjAwNjI2NDgzMi4xNzQyODEyNDQ3*_ga*MTUwMDcwOTIyNS4xNzQyODEyNDQ3*_ga_8YBG6FVEMD*MTc0MjgxNTY4Mi4yLjEuMTc0MjgxNzEyMS4wLjAuMA..*_fplc*R2xrJTJCJTJCMFV5cnkzVXlYMEY0WE9oSEY5ZlhoOFVWOEJ2TDhPMTgxNWsxMFYwTWp2ZG9weW5xeSUyRllxNXVzaU9JYVQ2WFlhU2lJQWZ2bVFNbWtsRXU2ZzVBeSUyRnM0VW9FemJUMU9lUmZHOGslMkZVaWNQT2g3a2lDQldWSyUyRm5Xa3JnJTNEJTNE)

SVG阅览(Window)：[https://github.com/tibold/svg-explorer-extension](https://github.com/tibold/svg-explorer-extension)
# 环境

#### Vulk v2.0.1 依赖
- [Nodejs LTS](https://nodejs.org/en/) _(> 16.x with npm >8)_ installed
- Knowledge with [Typescript](https://github.com/microsoft/typescript) _(> 4.x)_ (should not be installed globally)

#### 特性
- 基于 Vue 3 SSR/SSG 构建
- 由 Vite 驱动
- Bulma 框架(基于 Flexbox 的轻量级 CSS 框架。原生适合移动和平板)

```cmd
$env:HTTP_PROXY = "http://127.0.0.1:7897"
$env:HTTPS_PROXY = "http://127.0.0.1:7897"
```

```cmd
pnpm add typescript@4.x -D

# PowerShell 或 CMD
$env:HTTP_PROXY = "http://127.0.0.1:7897"
$env:HTTPS_PROXY = "http://127.0.0.1:7897"
pnpm dev
```