import csv


class abc():
    def __init__(self):
        self.id2 = ""
        self.idd = ""
        self.title = ""
        self.content = ""
        self.cate = ""
        write_txt_path = 'empty_fill_1.tsv'
        self.f2 = open(write_txt_path, 'w', encoding='utf-8', newline='')
        self.wr = csv.writer(self.f2, delimiter='\t')
    def abcd(self):
        with open("/home/msl/data/mrc/ko_mrc_ka/c74_e.tsv", "r") as f:
            for line in f:
                item = line.split("\t")
                if len(item) == 13 and item[0] != "":
                    self.id2 = item[0]
                    self.idd = item[1]
                    self.title = item[2]
                    self.content = item[3]
                    self.cate = item[11]
                    self.f2.write(line)
                else:
                    self.wr.writerow(
                        [self.id2, self.idd, self.title, self.content, item[0], item[1], item[2], item[3], item[4], item[5], item[6], self.cate,
                         item[7]])
                    print (self.id2)
        self.f2.write("\n")
        self.f2.close()

if __name__ == "__main__":
    a = abc()
    # b = a.ab()
    # c = a.abcd(b)  # b의 결과 값인 item 수를 c에 넣어준다.
    d = a.abcd()