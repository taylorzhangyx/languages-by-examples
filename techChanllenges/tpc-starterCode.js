var fs = require('fs');
var buf = '';

process.stdin.on('readable', function() {
  var chunk = process.stdin.read();
  if (chunk) buf += chunk.toString();
});

process.stdin.on('end', function() {
    var lines = buf.split('\n');
    var count = parseInt(lines[0]);
    for(var loopi = 1; loopi <= count; loopi++){
        var tokens = parseInt(lines[loopi])
        console.log(f(tokens))
    }
});

function f(n){
    if(n > 0){
        return "You are the future of Tencent!"
    }
    else{
        return "Good luck and Enjoy TPC!"
    }
}
