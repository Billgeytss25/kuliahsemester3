// membuat loop dengan for
for (let i = 10; i>= 1; i--){
    console.log('ini perulangan ke ${i + 1}');
    console.log("ini perulangan ke" + (i + 1));
    console.log("ini perulangan ke", i);
    console.log("ini perulangan ke", i);

}
// template 
console.log( 'ini perulangan ke ${i + 1}');
console.log("ini perulangan ke " + i);
console.log("ini perulangan ke", i);

// loops dengan while
let j = 1;
while (j < 10){
    console.warn('ini perulangan While ke ${j}');
    j++;
}

// contoh menampilkan data mhs
let mhs = ["Budi", "Andi", "Joko", "Joni"];
for (let i = 0; i < mhs.length; i++) {
    console.log(mhs[i]);
}
