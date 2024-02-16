# Blue
DotNet Blazor WASM with Tailwind CSS

> [!NOTE]
> Pre-installed software: DotNet 8.x, Npm 9.2.0, Node 18.19.0

### Commands
(1) Create project with DotNet CLI
```shell
dotnet new blazorwasm -o Blue.App --pwa
```

(2) Initialize new project with package.json file
```shell
npm init
```

(3) Install tailwindcss locally
```shell
npm i -D tailwindcss
npx tailwindcss init
```

(4) Modify tailwind.config.js with the following:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.razor", "**/*.cshtml", "**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

(5) Create new Styles/app.css file
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

(6) Remove wwwroot/css/bootstrap directory

(7) Remove wwwroot/css/app.css file



npx tailwindcss -i Styles/app.css -o wwwroot/app.css --watch

### Add the following to the launchSettings.json file
```json
"Watch": {
  "commandName": "Executable",
  "workingDirectory": "$(ProjectDir)",
  "executablePath": "dotnet",
  "commandLineArgs": "watch run debug --launch-profile http"
}
```
