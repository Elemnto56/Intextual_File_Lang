echo "What file to run?"
read input

echo "------ FROM $input.itx ------"
python3 og_parser.py $input.itx
