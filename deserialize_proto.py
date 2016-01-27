import Result_pb2
import sys
import os
import time

final_string = ""
result = Result_pb2.Result()

if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "INPUT_FILE"
  sys.exit(-1)


f = open(sys.argv[1], "rb")
start = time.clock()
result.ParseFromString(f.read())
end = time.clock()
 

f.close()

for student in result.student:
  final_string += student.name + "," + str(student.rollNum)
  for mark in student.marks:
      final_string += ":"
      final_string += mark.name + "," + str(mark.score)
  final_string += "\n"

text_file = open("output_protobuf.txt", "w")
text_file.write(final_string[:-1])
text_file.close()
size = os.stat("output_protobuf.txt").st_size
size1 = os.stat("result_protobuf").st_size
if "TIME" in os.environ:
  print "Deserialization Time ", end-start
  print "Size of output_protobuf.txt ", size
  print "Size of result_protobuf", size1
 
