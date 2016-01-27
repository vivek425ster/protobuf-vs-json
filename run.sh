#!/bin/sh

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

# Initialize our own variables:
input_file=""
serialize=0
deserialize=0
time=0

while getopts "cstdj:p:" opt; do
    case "$opt" in
    c)
	export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
	protoc --python_out=. Result.proto
        exit 0
        ;;
    s)  serialize=1
        ;;
    d)  deserialize=1
        ;;
    t)  time=1
	;;
    j)  input_file=$OPTARG
	if [ $serialize -eq 1 ] ; then
	  python serialize_json.py $input_file
	  serialize=0
	  exit
	fi
	if [ $deserialize -eq 1 ] ; then
	  python deserialize_json.py $input_file
          deserialize=0
	  exit
	fi
	if [ $time -eq 1 ] ; then
	  export TIME=1
	  python serialize_json.py $input_file
	  python deserialize_json.py result.json
	  file_size=`du -b result.json`
	  echo "Size in bytes" $file_size
          deserialize=0
	  exit
	fi
        ;;
    p)  input_file=$OPTARG
	if [ $serialize -eq 1 ] ; then
	  python serialize_proto.py $input_file
	  serialize=0
	  exit
	fi
	if [ $deserialize -eq 1 ] ; then
	  python deserialize_proto.py $input_file
	  deserialize=0
	  exit
	fi
	if [ $time -eq 1 ] ; then
	  export TIME=1
	  python serialize_proto.py $input_file
	  python deserialize_proto.py result_protobuf
	  file_size=`du -b result_protobuf`
	  echo "Size in bytes" $file_size
          deserialize=0
	  exit
	fi
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

echo "verbose=$verbose, output_file='$output_file', Leftovers: $@"
