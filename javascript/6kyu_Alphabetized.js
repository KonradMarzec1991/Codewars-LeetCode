function alphabetized(s) {
    s = s.replace(/[^a-zA-Z]/g,"");
    arr = s.split("");
    
    arr.sort(function (a,b) {
       let insensitive = a.toLowerCase().charCodeAt() - b.toLowerCase().charCodeAt();
       let sensitive = s.indexOf(a) - s.indexOf(b);
       return insensitive === 0 ? sensitive : insensitive;
    });

    return arr.join("")
}