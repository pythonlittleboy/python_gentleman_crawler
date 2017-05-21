#str = "/uploads/1704/snis909pl-lp.jpg"
#print(str.replace("-lp", ""))

title = "STAR-668古川いおり タイトスカートの誘惑 先輩OLのパッツパツのヒップラインとパンチラ、太もも美脚、エロ尻に興奮させられて…"
token = title
token = token.strip('\'".,?:-')
stopwords = "、 -=1234567890"

def isEnglish(char):
    return (char >= 'a' and char <= 'z') or (char >= "A" and char <= "Z")

def getChars(content):
    appendChar = ""
    results = []

    for char in token:
       if not char in stopwords:
           if isEnglish(char):
               appendChar = appendChar + char
           else:
               if appendChar != "":
                    results.append(appendChar)
                    appendChar = ""
               results.append(char)

    return results

print(getChars(title))