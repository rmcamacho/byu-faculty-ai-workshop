# 1. Set Up Codex and the Plugin

Do this once. It prepares Learning Suite, Kuali and Workday together. You need your own BYU account, an institution-approved Codex account, Google Chrome and Node.js 22 or newer. Allow time for account approval before the workshop.

Run everything in a **local** terminal (Terminal, PowerShell, or VS Code's integrated terminal) so Chrome opens on your own computer. An SSH or remote terminal opens Chrome on the other machine.

## Download the Workshop

Open https://github.com/rmcamacho/byu-faculty-ai-workshop, choose **Code > Download ZIP**, and extract it. No GitHub account is needed. Or:

```sh
git clone https://github.com/rmcamacho/byu-faculty-ai-workshop.git
cd byu-faculty-ai-workshop
```

Open a terminal in this folder (the one containing `README.md`). In VS Code: **File > Open Folder**, then **Terminal > New Terminal**.

## Install Codex, Node.js and Chrome

Install Codex CLI using the [official instructions](https://learn.chatgpt.com/docs/codex/cli). On macOS/Linux:

```sh
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Install a current LTS release of [Node.js](https://nodejs.org/en/download) and Google Chrome if needed. Close and reopen the terminal, then check:

```text
codex --version
node --version
```

Node's major version must be at least 22.

Run `codex` and choose **Sign in with ChatGPT** with your institution-approved account. For BYU, see the [license page](https://ai.byu.edu/obtaining-a-chatgpt-edu-license) and confirm your CES workspace; don't buy a personal plan for this tutorial. Read the [BYU data guidance](https://ai.byu.edu/chatgpt-edu-data-restrictions-page) before using AI on real institutional records. Exit Codex (`/exit`) when signed in.

## Install the Plugin

In the terminal, still in this folder:

```text
codex plugin marketplace add .
codex plugin add byu-faculty-integrations@byu-faculty-ai-workshop
codex plugin list
```

The list should show `byu-faculty-integrations@byu-faculty-ai-workshop` as installed and enabled.

Start Codex again in this folder and check:

> Use $byu-learning-suite, $byu-kuali and $byu-workday. Without opening a browser, confirm all three skills loaded and summarize in one line each what they will and will not do. Stop if any is unavailable.

## Start the Dedicated Browser

The plugin controls a separate Chrome window with its own profile, never your everyday Chrome. You sign in there yourself; Codex never sees passwords, Duo codes or cookies.

> Use $byu-learning-suite in CLI browser mode. Check the dedicated-browser status and start it if needed. Do not inspect any page until I say it is ready.

A new Chrome window should open. Leave it open; the Learning Suite, Kuali and Workday tutorials all reuse it. At the end of a session:

> Stop the dedicated CLI Chrome session. Leave the profile on my computer.

Continue with [2. Learning Suite](2_LEARNING_SUITE.md).

## Troubleshooting

- **Skill unavailable:** run `codex plugin list`, then start a new Codex session. Use Codex CLI in the terminal; the Codex IDE sidebar does not load plugins.
- **Chrome opens on another machine:** you are in a remote terminal; use a local one.
- **Port already in use:** ask Codex to check the dedicated-browser status and reuse the running session. Never attach it to an unrelated browser.
- **CAPTCHA or BYU sign-in step:** complete it yourself in the dedicated window.
- **No browser connection at all:** you can still do every exercise that uses local files. Say so in your prompt; uploading files to an ordinary chat is not Learning Suite access.
