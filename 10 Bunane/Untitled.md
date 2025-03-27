# CodeIt page

### Prerequisites

1. A recent web browser (Chrome, Edge, Firefox, ...)
2. [Nodejs LTS](https://nodejs.org/en/) _(> 16.x with npm >8)_ installed
3. Knowledge with [Typescript](https://github.com/microsoft/typescript) _(> 4.x)_ (should not be installed globally)

#### Install nodejs

1. Check if you already have Node.js installed. Run this command in your terminal:
```bash
node -v
```
If node is not installed on your machine, you can go to the official nodejs.org website, and choose the version depending on your operating system:
- <a href="https://nodejs.org/en/download/" target="_blank">Install node.js and npm on Windows, Linux or Mac OSX</a>
2. Enable pnpm with corepack
```powershell
corepack enable
corepack prepare pnpm@latest --activate
```
> _corepack is installed with node from **v16.13.x**, if your version is below, install it with: `npm install -g corepack`_

To setup the template and start installing project dependencies, run one of the following commands:
```bash
pnpm install
```
## 🔃 Run a development server
To start the development server, run the following commands:
```bash
pnpm dev
```