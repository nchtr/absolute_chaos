#1
with open("in.txt", "r") as ifs, open("out.txt", "w") as ofs:
    if ifs and ofs:
        sstr = ""
        for line in ifs:
            for c in line:
                if c.isalpha():
                    sstr += c
                else:
                    sstr += " "
        for word in sstr.split():
            if len(word) >= 7:
                ofs.write(word + "\n")
        ifs.close()
        ofs.close()
    else:
        print("Unable to open file(s)")
        
        
#2
with open("in.txt", "r") as ifs, open("out.txt", "w") as ofs:
    if ifs and ofs:
        sstr = ""
        for line in ifs:
            for c in line:
                if c.isalpha():
                    sstr += c
                else:
                    sstr += " "
        for i in sstr.split():
            ofs.write(i+" ")
        ifs.close()
        ofs.close()
    else:
        print("Unable to open file(s)")


#3
with open("111.txt","r") as fi:
      fcont=fi.read().split("\n")
      with open("222.txt","w") as fo:
            for stri in fcont[-1::-1]:
                stri=stri[-1::-1]+"\n"
                fo.write(stri)
                
#4
with open("input_file.txt", "r") as input:
    lines = input.readlines()

nocomma = None
for i in range(len(lines) - 1, -1, -1):
    if "," not in lines[i]:
        nocomma = i
        break

nl = "************\n"

if nocomma is not None:
    lines.insert(nocomma + 1, nl)
else:
    lines.append(nl)
with open("output_file.txt", "w") as output:
    output.writelines(lines)

