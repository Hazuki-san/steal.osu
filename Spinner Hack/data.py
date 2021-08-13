starttime = 245351

beat = 47
offset = 47

line = "256,192," + str(starttime + beat) + ",12,0," + str((starttime+beat) + int(offset/2)) + ",0:0:0:0:\n"
dupe = 200

with open('newdata.txt', 'w') as file_out:
    file_out.write("256,192," + str(starttime) + ",12,0," + str((starttime) + int(offset/2)) + ",0:0:0:0:\n")
    file_out.write("256,192," + str(starttime + beat) + ",12,0," + str((starttime + beat) + int(offset/2)) + ",0:0:0:0:\n")
    for time in range(1, dupe-2):
        spinner = line.split(",")
        start = str(int(spinner[2])+beat)
        ddddddata = spinner[:2]
        dddddata = ','.join(ddddddata)
        ddddata = spinner[3:5]
        dddata = ','.join(ddddata)
        end = str(int(spinner[5])+beat)
        ddata = spinner[6:7]
        data = ','.join(ddata)
        line = '%s,%s,%s,%s,%s' % (dddddata, start, dddata, end, data)
        file_out.write(line)