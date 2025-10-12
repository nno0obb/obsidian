---
created_at: 2025/08/10 16:47:15
updated_at: 2025/08/11 00:35:46
---
```
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

sudo dnf update -y
sudo dnf upgrade -y
sudo dnf install -y python3.12
python3.12
ls -al python3
which python3
which python3.12
sudo dnf install -y python3-pip

pip install --user pipx
pipx ensurepath
pipx install poetry

sudo dnf install -y git

git clone https://github.com/nno0obb/ai-auto-trader.git
cd ai-auto-trader

poetry config virtualenvs.in-project true
poetry env use /usr/bin/python3.12
poetry install
eval $(poetry env activate)

# direnv
deactivate
curl -sfL https://direnv.net/install.sh | bash
sudo chmod +x $(which direnv)

@~/.bashrc
# direnv
eval "$(direnv hook bash)"
show_virtual_env() {
  if [[ -n "$VIRTUAL_ENV" && -n "$DIRENV_DIR" ]]; then
    echo "($(basename $VIRTUAL_ENV)) "
  fi
}
export -f show_virtual_env
PS1='$(show_virtual_env)'$PS1

@.envrc
source .venv/bin/activate

direnv allow

---

sudo dnf install -y redis6
sudo systemctl status redis6
sudo systemctl start redis6
redis6-cli

sudo systemctl status main_order
sudo systemctl status main_check
```