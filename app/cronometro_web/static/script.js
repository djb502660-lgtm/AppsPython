var segundos = 0;
var intervalo = null;
var corriendo = false;

var pantalla = document.getElementById("tiempo");
var btnIniciar = document.getElementById("btnIniciar");
var btnPausar = document.getElementById("btnPausar");
var btnReiniciar = document.getElementById("btnReiniciar");

function mostrarTiempo() {
    var h = Math.floor(segundos / 3600);
    var m = Math.floor((segundos % 3600) / 60);
    var s = segundos % 60;

    var textoH = h < 10 ? "0" + h : h;
    var textoM = m < 10 ? "0" + m : m;
    var textoS = s < 10 ? "0" + s : s;

    pantalla.textContent = textoH + ":" + textoM + ":" + textoS;
}

function iniciar() {
    if (corriendo) return;
    corriendo = true;
    btnIniciar.disabled = true;
    btnPausar.disabled = false;

    intervalo = setInterval(function () {
        segundos = segundos + 1;
        mostrarTiempo();
    }, 1000);
}

function pausar() {
    if (!corriendo) return;
    corriendo = false;
    clearInterval(intervalo);
    btnIniciar.disabled = false;
    btnPausar.disabled = true;
}

function reiniciar() {
    pausar();
    segundos = 0;
    mostrarTiempo();
}

btnIniciar.addEventListener("click", iniciar);
btnPausar.addEventListener("click", pausar);
btnReiniciar.addEventListener("click", reiniciar);

mostrarTiempo();
