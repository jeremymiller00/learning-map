#!/bin/zsh
# run this script from the root of the project, such as
# sh src/check_data.sh
# NB: last line of csv files must have '\n' or last line will not be evaluated

cd data
datadir="."
# global variable
noerrors=true
for file in "$datadir"/*
do
  first=true
  nofileerrors=true
  echo "File Being Read: $file"
  while IFS= read -r line
  do
    # strip line of all characters except comma
    res="${line//[^,]}"
    if [ "$first" = true ]
    then
      # store comma count for first line - header
      firstcount=`echo "${#res}"`
      first=false
    else
      # store comma count for subsequent line
      nextcount=`echo "${#res}"`
      if [ "$firstcount" != "$nextcount" ]
      then
        noerrors=false
        nofileerrors=false
        echo "Error in file $file"
        echo "On line: $line"
        echo "Should have $firstcount commas but has $nextcount"
      fi
    fi
  done < $file
  if [ "$nofileerrors" = true ]
  then
    echo "No errors found in file $file"
  fi
done
if [ "$noerrors" = true ]
then
  echo "No errors found in any files."
fi
exit 0