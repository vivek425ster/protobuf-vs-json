import Result_pb2
import sys
import time
import os

if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "INPUT_FILE"
  sys.exit(-1)

with open(sys.argv[1]) as data_file:
  data = data_file.readlines()

res = Result_pb2.Result()
students = []
for record in data:
  list_record = record.split(":")
  student = Result_pb2.Student()
  student.name = list_record[0].split(",")[0]
  list_marks = []
  for i in range(1,len(list_record)):
    mark = Result_pb2.CourseMarks()
    course_name = list_record[i].split(",")[0]
    if i == len(list_record):
      course_marks = int(list_record[i].split(",")[1][:-1])
    else:
      course_marks = int(list_record[i].split(",")[1])
    mark.name = course_name
    mark.score = course_marks
    list_marks.append(mark)
  student.marks.extend(list_marks)
  student.rollNum = int(list_record[0].split(",")[1])
  students.append(student)
res.student.extend(students)

f = open("result_protobuf", "wb")
start = time.clock()
f.write(res.SerializeToString())
end = time.clock()
f.close()
if "TIME" in os.environ:
  print "Serialization time ", end - start

#with open('result_protobuf', 'w') as outfile:
#  outfile.write(res.SerializeToString())

