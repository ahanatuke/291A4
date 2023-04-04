for i in 1 2 3 4;
do
    for type in "Embed" "Norm";
    do
        python3 A4Q$i$type.py $1 | sed "s/\ObjectId('.*')/ObjectId('')/" | sort > A4Q$i$type.out
    done
    if ! cmp A4Q${i}Embed.out A4Q${i}Norm.out; then
        echo "differs for $i"
        exit
    fi
done
echo "all good :)"