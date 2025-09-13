# ChessApp
## Overview
ChessApp is a full-stack web application that lets users play chess in the browser. It features:
- A Python/Flask backend that handles game logic, move validation, and API endpoints.
- A modern Vue.js frontend for an interactive user experience with a clean UI.

The app supports standard chess rules, including legal move validation, game state management, and user interaction through a responsive interface.

## Running the Backend Server
Perform these steps if running for the first time
- Make sure you have python3 and Pipenv installed
- Create a virtual enviornment (alternatively you can use homebrew to install system-wide)
  - ```python3 -m venv venv```
- Activate the virtual enviornment
  - Macbook: ```source venv/bin/activate```
  - Windows: ```venv\Scripts\activate```
- This installs Flask and Flask-CORS using the requirments.txt file included in the repo.
  - ```pip install -r backend/requirements.txt```

To run the Backend Server
- ```pipenv shell```
- ```python3 src/main.py```



## Running the Frontend Server
Install nvm if you don't have it already
- ```curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash```
- add the following to your ~/.zshrc or ~/.bash or equivalent depending on the shell you are using
- ```export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```
- Restart your terminal
- ```nvm install --lts```
- ```nvm use --lts```
- ```npm init -y```

To run the Server
- ```npm run install```
- ```npm run serve```
