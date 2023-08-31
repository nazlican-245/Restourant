let toplam=0;
let alan=document.getElementById("toplam_fatura");
let hamburger=document.getElementById("adet_1");
let pizza=document.getElementById("adet_2");
let tost=document.getElementById("adet_3");

let kazandibi=document.getElementById("adet_4");
let sutlac=document.getElementById("adet_5");
let baklava = document.getElementById("adet_6");

let su=document.getElementById("adet_7");
let kola=document.getElementById("adet_8");
let soda=document.getElementById("adet_9");
let toplama_butonu=document.getElementById("topla_buton");
let temizleme=document.getElementById("temizle_buton");

let hamburger_fiyat=45;
let pizza_fiyat=55;
let tost_fiyat=23;

let kazandibi_fiyat=24;
let sutlac_fiyat=14;
let baklava_fiyat=34;

let su_fiyat=3;
let kola_fiyat=13;
let soda_fiyat=7;
toplama_butonu.addEventListener("click",topla);
temizleme.addEventListener("click",temizle);

function topla(){
    let toplam=(hamburger_fiyat * hamburger.value) + (pizza_fiyat * pizza.value) + (tost_fiyat * tost.value) + (kazandibi_fiyat * kazandibi.value) + (sutlac_fiyat * sutlac.value) + (baklava_fiyat * baklava.value) + (su_fiyat * su.value) + (soda_fiyat*soda.value) + (kola_fiyat*kola.value);
    alan.innerHTML=toplam;
    console.log(toplam)
}

function temizle(){
    hamburger.value=0;
    pizza.value=0;
    tost.value=0;
    
    kazandibi.value=0;
    sutlac.value=0;
    baklava.value=0;

    su.value=0;
    kola.value=0;
    soda.value=0;
    toplam=0;

    hamburger.value.innerHTML=hamburger.value;
    pizza.value.innerHTML=pizza.value;
    tost.value.innerHTML=tost.value;

    kazandibi.value.innerHTML=kazandibi.value;
    sutlac.value.innerHTML=sutlac.value;
    baklava.value.innerHTML=baklava.value;

    su.value.innerHTML=su.value;
    kola.value.innerHTML=kola.value;
    soda.value.innerHTML=soda.value;
    alan.innerHTML=toplam;
}