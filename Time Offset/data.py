with open('timing.txt', 'r') as file_in:
    with open('newtming.txt', 'w') as file_out:
        for line in file_in:
            ttime = line.split(",")
            new_t = str(int(ttime[0])+1786)
            ddata = ttime[1:]
            data = ','.join(ddata)
            line = '%s,%s' % (new_t, data)
            file_out.write(line)