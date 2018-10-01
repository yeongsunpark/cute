#!/usr/bin/env bash

# Define a timestamp function
timestamp() {
  date +"%T"
}
echo "$(timestamp): Start.."

python3 doc2text_2.py
echo "$(timestamp): Step 1: doc2text_2"

python3 txt_all_save.py
echo "$(timestamp): Step 2: txt_all_save"

python3 law_pre.py
echo "$(timestamp): Step 3: law_pre"

