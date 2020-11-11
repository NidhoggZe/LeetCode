class Solution:
    def reorderSpaces(self, text: str) -> str:
        templist = []
        count = 0
        curstr = ""
        for i in range(0, text.__len__()):
            if text[i] == ' ':
                count += 1
                if curstr != "":
                    templist.append(curstr)
                curstr = ""
            else:
                curstr += text[i]
        if curstr != "":
                    templist.append(curstr)

        if templist.__len__() == 1:
            m = 0
            last = count
        else:
            m = count//(templist.__len__()-1)

            last = count - (templist.__len__()-1)*m
        res = ""
        for i in templist:
            res += i
            res += " "*m
        
        if m >= last:
            return res[0:res.__len__() - m + last]
        else:
            return res + count*" "