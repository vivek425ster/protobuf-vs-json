import json
import sys
import time
import os

def byteify(input_str):
    if isinstance(input_str, dict):
        return {byteify(key): byteify(value)
                for key, value in input_str.iteritems()}
    elif isinstance(input_str, list):
        return [byteify(element) for element in input_str]
    elif isinstance(input_str, unicode):
        return input_str.encode('utf-8')
    else:
        return input_str

if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "INPUT_FILE"
  sys.exit(-1)

with open(sys.argv[1]) as data_file:
  start = time.clock()
  records = json.load(data_file)

records = byteify(records)
final_result = ""
for record in records:
  final_result += record["Name"] + "," + str(record["RollNo"])
  courses = record["CourseMarks"]
  for i in range(0,len(courses)):
    dict_record = courses[i]
    final_result += ":"
    final_result += dict_record["CourseName"] + "," + str(dict_record["CourseScore"])
  final_result += "\n"
text_file = open("output_json.txt", "w")
text_file.write(final_result[:-1])
text_file.close()
size = os.stat("output_json.txt").st_size
size1 = os.stat("result.json").st_size
end = time.clock()
if "TIME" in os.environ:
    print "Deserializartion time ", (end - start)
    print "Size of output_json.txt ", size
    print "Size of result.json ", size1
