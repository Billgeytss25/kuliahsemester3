function fetchData(callback){
    setTimeout(function() {
        const data = 'Fethced data';
        callback(data);
    }, 5000)
}
fetchData (function(data){
    console.log(data);
});
// membuat proses 2
console.log("ini proses 2 nya");