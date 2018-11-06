<코드 설명>
prepare: law_parser.json: 필요한 파일의 경로를 적음.
step1: doc2text_2.py : input_dir 에 있는 텍스트 파일을 모두 가져와서 장-절-조 이런 식으로 적힌 텍스트 파일을 만듦.
step2: txt_all_save.py : 완성 된 장-절-조 텍스트 파일을 하나의 파일로 합친다. 
step3: law_pre.py : 정규식을 통해 다듬는 작업 등을 함. 



<사용 안 하는 코드>
law_rex.py: law_pre.py 연습 하던 코드
doc2txt.py: doc2text_2.py 연습 하던 코드
doc_text.py : law_parser.json 연습하던 코드
