function invertirNumero(n) {
    let acumulador = 0;
    while (n > 0) {
        let ultimoDigito = n % 10;
        acumulador = (acumulador * 10) + ultimoDigito;
        n = (n - ultimoDigito) / 10;
    }
    return acumulador;
}

//================================================================================================================

function binarioADecimal(binario) {
    let decimal = 0;
    let base = 1;
    while (binario > 0) {
        let bit = binario % 10;
        decimal += bit * base;
        base *= 2;
        binario = (binario - bit) / 10;
    }
    return decimal;
}

//================================================================================================================

function raizEntera(n) {
    if (n < 0) return -1;
    let i = 0;
    while (i * i <= n) {
        i++;
    }
    return i - 1;
}



//================================================================================================================


function factoresPrimos(n) {
    let divisor = 2;
    while (n > 1) {
        while (n % divisor === 0) {
            console.log(divisor);
            n = n / divisor;
        }
        divisor++;
    }
}

//================================================================================================================

function sumaDivisores(n) {
    let suma = 0;
    for (let i = 1; i < n; i++) {
        if (n % i === 0) suma += i;
    }
    return suma;
}

function sonAmigos(a, b) {
    return (sumaDivisores(a) === b && sumaDivisores(b) === a);
}


//================================================================================================================



function diamanteHueco(n) {
    let centro = (n + 1) / 2;
    for (let i = 1; i <= n; i++) {
        let fila = "";
        let espaciosExt = i <= centro ? centro - i : i - centro;
        let espaciosInt = i <= centro ? (i * 2) - 3 : (n - i) * 2 - 1;

       
        for (let j = 0; j < espaciosExt; j++) fila += " ";
        
        fila += "*";

        if (espaciosInt > 0) {
            for (let j = 0; j < espaciosInt; j++) fila += " ";
            fila += "*";
        }
        console.log(fila);
    }
}


//================================================================================================================


function relojArena(n) {

    for (let i = n; i >= 1; i--) {
        let fila = "";
        for (let s = 0; s < n - i; s++) fila += " ";
        for (let j = 0; j < (2 * i - 1); j++) fila += i;
        console.log(fila);
    }
    for (let i = 2; i <= n; i++) {
        let fila = "";
        for (let s = 0; s < n - i; s++) fila += " ";
        for (let j = 0; j < (2 * i - 1); j++) fila += i;
        console.log(fila);
    }
}

//================================================================================================================


function diaDelAño(d, m, a) {
    let totalDias = d;
    let esBisiesto = (a % 4 === 0 && a % 100 !== 0) || (a % 400 === 0);

    for (let mes = 1; mes < m; mes++) {
        if (mes === 2) {
            totalDias += esBisiesto ? 29 : 28;
        } else if (mes === 4 || mes === 6 || mes === 9 || mes === 11) {
            totalDias += 30;
        } else {
            totalDias += 31;
        }
    }
    return totalDias;
}


//================================================================================================================


function validarTarjeta(num) {
    let suma = 0;
    for (let i = 1; i <= 8; i++) {
        let digito = num % 10;
        if (i % 2 === 0) { 
            digito *= 2;
            if (digito > 9) digito -= 9;
        }
        suma += digito;
        num = (num - (num % 10)) / 10;
    }
    return suma % 10 === 0;
}

//================================================================================================================

function cajero(monto) {
    let b100 = 0, b50 = 0, b20 = 0, b10 = 0, b5 = 0, b1 = 0;

    while (monto >= 100) { monto -= 100; b100++; }
    if (b100 > 0) console.log("Billetes de 100: " + b100);

    while (monto >= 50) { monto -= 50; b50++; }
    if (b50 > 0) console.log("Billetes de 50: " + b50);

    while (monto >= 20) { monto -= 20; b20++; }
    if (b20 > 0) console.log("Billetes de 20: " + b20);

    while (monto >= 10) { monto -= 10; b10++; }
    if (b10 > 0) console.log("Billetes de 10: " + b10);

    while (monto >= 5) { monto -= 5; b5++; }
    if (b5 > 0) console.log("Billetes de 5: " + b5);

    while (monto >= 1) { monto -= 1; b1++; }
    if (b1 > 0) console.log("Billetes de 1: " + b1);
}


//================================================================================================================
















































