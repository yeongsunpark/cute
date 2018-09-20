economy = ["금융기타", "대출", "증권", "취업"]
science = ["IT기타", "게임", "과학기타", "날씨", "모바일", "비만성장", "생활가전", "성형외과", "소프트웨어", "수송기기", "영상음향가전", "의료기타", "자동차", "제약", "피부과" ,"하드웨어", "항공"]
society = ["결혼", "교육", "사회기타", "생활용품", "육아", "종교"]
sports = ["경마", "골프", "동계스포츠", "레저스포츠", "스포츠기타", "야구", "축구"]
normal = ["국방", "기호식품", "복권", "부동산", "쇼핑", "숙박", "식품기타", "애완", "여행기타", "연금보험", "인테리어", "재해", "정치", "탈모", "패션", "화장품", "공연", "영화", "예술"]
ent = ["연예"]

f2 = open("replace.txt", "w")

with open("/home/msl/data/mrc/ko_mrc_ka/r11_e.tsv", "r") as f:
    for line in f:
        item = line.strip().split("\t")
        if len(item) == 13:
            cate = item[11]
            if cate in economy:
                f2.write("경제\n")
            elif cate in science:
                f2.write("과학\n")
            elif cate in society:
                f2.write("사회\n")
            elif cate in sports:
                f2.write("스포츠\n")
            elif cate in normal:
                f2.write("일반\n")
            elif cate in ent:
                f2.write("연예\n")
            elif cate == "":
                f2.write("null\n")
            else:
                f2.write("error\n")
        elif len(item) == 9:
            cate = item[7]
            if cate in economy:
                f2.write("경제\n")
            elif cate in science:
                f2.write("과학\n")
            elif cate in society:
                f2.write("사회\n")
            elif cate in sports:
                f2.write("스포츠\n")
            elif cate in normal:
                f2.write("일반\n")
            elif cate in ent:
                f2.write("연예\n")
            elif cate == "":
                f2.write("null\n")
            else:
                f2.write("error\n")
        else:
            exit()


f2.close()