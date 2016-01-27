import json
import sys
import time
import os
if len(sys.argv) != 2:
  print len(sys.argv)
  print "Usage:", sys.argv[0], "INPUT_FILE"
  sys.exit(-1)

with open(sys.argv[1]) as data_file:
  data = data_file.readlines()

final_list = []
for record in data:
  list_record = record.split(":")
  dict_record = {}
  dict_record["Name"] = list_record[0].split(",")[0]
  list_marks = []
  for i in range(1,len(list_record)):
    dict_marks = {}
    course_name = list_record[i].split(",")[0]
    if i == len(list_record):
      course_marks = int(list_record[i].split(",")[1][:-1])
    else:
      course_marks = int(list_record[i].split(",")[1])
    dict_marks["CourseName"] = course_name
    dict_marks["CourseScore"] = course_marks
    list_marks.append(dict_marks)
  dict_record["CourseMarks"] = list_marks
  dict_record["RollNo"] = int(list_record[0].split(",")[1])
  final_list.append(dict_record)

with open('result.json', 'w') as outfile:
    start = time.clock()
    json.dump(final_list, outfile, separators=(',', ':'),
        ensure_ascii=False)
    end = time.clock()


if "TIME" in os.environ:
  print "Serialization time", end - start
