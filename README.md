# ScriptSDK

[![License](https://img.shields.io/badge/License-GPL--2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](package.json)

Use certain Endstone features directly in your Bedrock add-ons through a JavaScript API. ScriptSDK bridges the gap between Minecraft Bedrock add-ons and Endstone plugin capabilities.

⚠️ **Plugin currently under development.**

## 📋 Overview

ScriptSDK is a dual-component system:
- **JavaScript/TypeScript SDK**: Import and use in your Bedrock add-ons
- **Endstone Plugin**: Python-based server plugin that enables the SDK functionality

## ✨ Features

*Coming soon - This section will list all available features*

<!-- Features will be documented here as they are implemented -->

## 📦 Installation

### For Add-on Developers (JavaScript/TypeScript)

1. Download the latest release from [GitHub Releases](https://github.com/Bedrock-Developpeur-Francophone/ScriptSDK/releases)
2. Copy the following files to your add-on project in a `lib` folder:
   - `ScriptSDK.ts`
   - `ScriptSDK.js`
   - `type.d.ts`

Your add-on structure should look like:
```
your-addon/
├── lib/
│   ├── ScriptSDK.ts
│   ├── ScriptSDK.js
│   └── type.d.ts
└── scripts/
    └── your-script.js
```

### For Server Administrators (Endstone Plugin)

1. Download the latest plugin wheel (`.whl`) from [GitHub Releases](https://github.com/Bedrock-Developpeur-Francophone/ScriptSDK/releases)
2. Place the `.whl` file in your Endstone server's `plugins` folder
3. Restart your server

## 🚀 Quick Start

### In your Bedrock Add-on

After copying the SDK files to your `lib` folder, import it in your scripts:

```javascript
import ScriptSDK from './lib/ScriptSDK.js';

// Example usage
const result = ScriptSDK.test();
console.log(result); // { value: 'test' }
```

### TypeScript Support

Full TypeScript support with type definitions included:

```typescript
import ScriptSDK from './lib/ScriptSDK.js';
import type { test } from './lib/type.js';

const result: test = ScriptSDK.test();
```

## 📝 License

This project is licensed under the GPL-2.0 License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [GitHub Repository](https://github.com/Bedrock-Developpeur-Francophone/ScriptSDK)
- [Issue Tracker](https://github.com/Bedrock-Developpeur-Francophone/ScriptSDK/issues)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Bedrock-Developpeur-Francophone/ScriptSDK/issues) on GitHub.