python -m venv venv;
case "$OSTYPE" in
	linux*) source ./venv/bin/activate;;
	msys*) ./venv/Scripts/activate;;
	*)		echo "unknown: $OSTYPE";;
esac
pip install -r requirements.txt;
python3 run.py
