# 1. Set Up Codex and the Plugin

Do this once. It prepares Learning Suite, Kuali and Workday together. You need your own BYU account and an institution-approved ChatGPT/Codex account. Allow time for account approval before the workshop.

## Choose How You'll Run Codex

| | **ChatGPT desktop app** (recommended for most faculty) | **Codex CLI** (Terminal, PowerShell or VS Code) |
| --- | --- | --- |
| You type prompts in | the app's Codex chat | a terminal |
| Browser it controls | a browser built into the app | a separate, dedicated Chrome window |
| Also needs | nothing else | Node.js 22 or newer and Google Chrome |

Both use the same plugin, skills and prompts. Pick one; you can switch later.

## Download the Workshop and Sign In

1. Open https://github.com/rmcamacho/byu-faculty-ai-workshop, choose **Code > Download ZIP**, and extract it. No GitHub account is needed. (Git users can `git clone https://github.com/rmcamacho/byu-faculty-ai-workshop.git` instead.)
2. Use your institution-approved account everywhere below. For BYU, see the [license page](https://ai.byu.edu/obtaining-a-chatgpt-edu-license) and confirm your CES workspace is selected; don't buy a personal plan for this tutorial. Read the [BYU data guidance](https://ai.byu.edu/chatgpt-edu-data-restrictions-page) before using AI on real institutional records.

Then follow **A** or **B**.

## A. ChatGPT Desktop App

### Install and open the workshop folder

1. Install the app from the [official instructions](https://learn.chatgpt.com/docs/app) (macOS, Windows or Linux) and sign in with your approved account.
2. Start a **Codex** chat and **open the workshop folder** you extracted (the one containing `README.md`) as its folder or project.

### Install the plugin

1. Open **Plugins** in the app. The **Faculty AI Workshop** marketplace appears because the workshop folder is open. Install **BYU Learning Suite, Kuali and Workday**.
2. Quit and reopen the app, then start a **new** Codex chat in the workshop folder.

### Check it

In a new Codex chat in the workshop folder:

> Use $byu-learning-suite, $byu-kuali and $byu-workday. Without opening a browser, confirm all three skills loaded and summarize in one line each what they will and will not do. Stop if any is unavailable.

### Open the built-in browser

Codex works in a browser built into the app, not your everyday Chrome. If it tries to connect to an external Chrome instead, tell it to use the built-in browser.

> Use $byu-learning-suite. Open or reuse the app's built-in browser and go to https://learningsuite.byu.edu. Wait while I sign in and tell you I am ready. Then open the Development course list and identify my practice copy by its visible title; ask me which one only if there are multiple plausible copies. Do not open the source demo or a live course, roster or gradebook. If I have no copy yet, guide me through Copy the Demo Course in tutorial/2_LEARNING_SUITE.md. Once my copy is open, confirm its title and Development status, check the eight assignment titles and point values (283 total), and locate Start Here without changing anything.

Sign in yourself in that browser panel, including Duo. Reuse this browser for later exercises; another service may require sign-in. Never paste a password, Duo code or cookie into a prompt.

Continue with [2. Learning Suite](2_LEARNING_SUITE.md). If your copy is already verified, start Exercise 1; otherwise follow Copy the Demo Course.

## B. Codex CLI (Terminal, PowerShell or VS Code)

Run everything in a **local** terminal so Chrome opens on your own computer; an SSH or remote terminal opens Chrome on the other machine. In VS Code use **Terminal > New Terminal**: the Codex sidebar does not load plugins.

### Install Codex and Node.js

Install Codex CLI from the [official instructions](https://learn.chatgpt.com/docs/codex/cli). On macOS/Linux:

```sh
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Install a current LTS release of [Node.js](https://nodejs.org/en/download) and Google Chrome if needed. Close and reopen the terminal, then check that both work (Node's major version must be at least 22):

```text
codex --version
node --version
```

Run `codex`, choose **Sign in with ChatGPT** with your approved account, then exit (`/exit`).

### Install the plugin

Open a terminal in the workshop folder (the one containing `README.md`) and run:

```text
codex plugin marketplace add .
codex plugin add byu-faculty-integrations@byu-faculty-ai-workshop
codex plugin list
```

The list should show `byu-faculty-integrations@byu-faculty-ai-workshop` as installed and enabled. Start `codex` again in this folder and check:

> Use $byu-learning-suite, $byu-kuali and $byu-workday. Without opening a browser, confirm all three skills loaded and summarize in one line each what they will and will not do. Stop if any is unavailable.

### Start the dedicated browser

The plugin controls a separate Chrome window with its own profile, never your everyday Chrome. You sign in there yourself; Codex never sees passwords, Duo codes or cookies.

> Use $byu-learning-suite in CLI browser mode. Check the dedicated-browser status and start it if needed. Do not inspect any page until I say it is ready.

Leave it open; the Learning Suite, Kuali and Workday tutorials all reuse it. At the end of a session:

> Stop the dedicated CLI Chrome session. Leave the profile on my computer.

Continue with [2. Learning Suite](2_LEARNING_SUITE.md).

## Troubleshooting

- **Skill unavailable:** start a **new** chat or session after installing; skills load only then. In the CLI, check `codex plugin list`. In VS Code, use the integrated terminal, not the Codex sidebar.
- **Workshop marketplace not in the desktop app's Plugins:** make sure the chat has the workshop folder open. Otherwise install the [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), run the two commands under [Install the plugin](#install-the-plugin-1) in B, and reopen the app; the app and the CLI share plugin settings.
- **Desktop app reaches for your external Chrome:** tell it to use the app's built-in browser instead.
- **CLI Chrome opens on another machine:** you are in a remote terminal; use a local one.
- **CLI port already in use:** ask Codex to check the dedicated-browser status and reuse the running session. Never attach it to an unrelated browser.
- **CAPTCHA or BYU sign-in step:** complete it yourself in the browser Codex is using.
- **No browser connection at all:** you can still do every exercise that uses local files. Say so in your prompt; uploading files to an ordinary chat is not Learning Suite access.
