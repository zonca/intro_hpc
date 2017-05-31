for count in $(seq -f "%04g" 0 999)
do
    touch files/data_$count.txt
done
