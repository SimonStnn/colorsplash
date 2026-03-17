#!/bin/bash

# Minimal setup: install Python dependencies defined in pyproject.toml.
# Also install the Bruno CLI for local development.
# Ensure SSH config has safe permissions to allow git pushes from this container.
set -e

# Ensure SSH directory permissions are correct (fixes "Bad owner or permissions" errors).
if [ -d "$HOME/.ssh" ]; then
  chmod 700 "$HOME/.ssh" || true
  if [ -f "$HOME/.ssh/config" ]; then
    chmod 600 "$HOME/.ssh/config" || true
  fi
fi

uv sync
npm install -g @usebruno/cli --no-fund --no-audit