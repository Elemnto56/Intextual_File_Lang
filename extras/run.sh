echo "What file to run?"
read input

echo "------ FROM $input.itx ------"
python3 parser.py $input.itx
