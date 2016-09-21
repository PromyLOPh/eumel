#!/bin/sh

root=`dirname "$0"`
root=`realpath "$root"`

while read -r F; do
	base=`basename "$F"`
	linear=`mktemp`
	destdir="${base}.extracted"
	echo "Extracting $F to $destdir"
	$root/linearizeDisk.py "$F" "$linear"
	$root/extractArchive.py -n -o "$destdir" "$linear"
	pushd "$destdir" || continue
	for G in ./*; do
		echo "Converting $G to ${G}.txt"
		$root/convertFileDs.py "$G" > "${G}.txt" || rm "${G}.txt"
	done
	popd
	rm "$linear"
done

