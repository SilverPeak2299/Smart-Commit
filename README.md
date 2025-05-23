# Smart Commit
A simple CLI tool for generting commit messages with Google Gemini


## General
there are two primary commands as part of smart-commit:
- `smart-commit`: generates a commit msg from the git diff, presents it to the user then gives some options for just commiting, editing the msg, reloading the message and exiting without doing anything.

- `smart-commit-config`: takes a Google Gemeni API key as an arguemnt and stores in in your OS's keychain for later use.

## Setup
 1. Generate a Google Gemeni API key, a free tier should be available. 
 2. Run `smart-commit-config` to set up with the generated API keychain
 3. Good to go, use `smart-commit` to generate a commit for files in your staging area