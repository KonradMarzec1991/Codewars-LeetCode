function uniqueSort(arr) {
	const uniq = [...new Set(arr)];
    uniq.sort((a, b) => a - b);
    return uniq
}
