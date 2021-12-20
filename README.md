# CLI_Tweet

Tweet using the command line interface. (You'll need a Twitter Developer Account)

When prompoted enter your keys which you recieve at the Twitter Dev portal

### To run the script:
```sh
chmod +x tweetPy.py
cd
mkdir bin
mv tweetPy.py ~/bin
export PATH="$HOME/bin:$PATH"
source ~/.zshrc -- or .bashrc
```

### To run the tests:
```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
```
