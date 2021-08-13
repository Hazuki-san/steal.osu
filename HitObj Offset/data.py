with open('hitobj.txt', 'r') as file_in:
    with open('newhtobj.txt', 'w') as file_out:
        for line in file_in:
            ttime = line.split(",")
            new_t = str(int(ttime[2])+1786)
            ddddata = ttime[:2]
            dddata = ','.join(ddddata)
            ddata = ttime[3:]
            data = ','.join(ddata)
            line = '%s,%s,%s' % (dddata, new_t, data)
            file_out.write(line)