check_marker.py: 마커 | 를 마커 $ 로 바꿈

check_wh.py: q_id 와 wh 만 있는 파일을 만듦

compare.py: 두 파일을 비교해 만약 일치하면 적음.

count_wh_file.py: for i in range(1, 11): /n {}.format(i) 해서 파일들의 육하원칙 개수 모두 셈

count_wh.py: 육하원칙 개수 셈

empty_fill.py: 본문 제목 등이 없는 행에 위의 내용을 적어서 다 채워진 하나의 파일을 만듦.

inser_str.py: def insert(str (string, str_to_insert, s_index, e_index): 받아서 정답 앞 뒤로 마커 붙임. 

replace_cate.py: 세분화된 카테고리가 적혀있으면 대분류 카테고리를 적음.

rex.py: 마커 바로 앞이나 뒤에 마커가 있으면 없애는 정규식.

why.py: json 을 tsv 로 바꿔주는 코드인데 이렇게하면 안 됨. 

이렇게 `r = csv.writer(f2, delimiter = '\t', quoting=csv.QUOTE_NONE, quotechar='')` quoting 옵션 지정해 줘야함. 

안 그러면 json 파일에 붙는 \" 이런 게 다 인식 돼고 암튼 이상해져서 

``` context			"를
context			로  #1634

"\n		context_en를
\n		context_en로  # 1634

text	"를
text	로  #306

"\n				text_en를
\n				text_en로  #306


""를 "로  #8104
```

이렇게 다 바꿔주는 작업해야됨
