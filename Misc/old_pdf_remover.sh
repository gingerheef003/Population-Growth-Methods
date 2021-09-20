now=$(date +%s)
ls | grep -E "*.pdf" | while read i
do
	t=$(date -r "$i" +%s)
	x=$(expr \( $now - $t \) / 259200)
	if [[ x -ge 1 ]]
	then
		rm "$i"		
	fi
done
