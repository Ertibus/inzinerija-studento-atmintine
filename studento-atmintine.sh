python -m venv venv;
case "$OSTYPE" in
	linux*) source ./venv/bin/activate;;
	msys*) ./venv/Scripts/activate;;
	*)		echo "unknown: $OSTYPE";;
esac
yes | pip install -r requirements.txt --quiet;
python3 run.py
