// membuat function
function salamPembuka(name){
    console.log("Halo, selamat datangs " + name);    
}
salamPembuka("Luhut");

//membuat function express
let salamPenutup = function (name) {
    console.log("halo, sampai jumpa mattane" + name);
};
salamPenutup("Andin");

// mmebuat arrow function
let salamPenutup2 = (name) => {
    console.log("halo, sampai jumpa" + name);
};

salamPenutup2("joko anwar");

// scope variabel local & global
let shapeArea = (panjang, lebar) =>{
    let varlocal = "ini variabel Local"
    let varglobal = "ini variabel global"
    console.log('luas untuk persegi dengan panjang ${panjang} dan lebar ${lebar}adalah ${panjang * lebar}');
    console.log(varlocal);
    console.log(varglobal);
};
shapeArea(5, 10);
console.log(varlocal);
console.log(varglobal);




