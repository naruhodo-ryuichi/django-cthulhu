/**
 * Created with PyCharm.
 * User: peter
 * Date: 30/08/13
 * Time: 17:54
 * To change this template use File | Settings | File Templates.
 */
app.controller('fichaCtrl', function ($scope) {
    $scope.ficha = reseteaficha();
    $scope.tirarand = function(){tirarand($scope)};
    $scope.actualizaINT = function(){actualizaINT($scope)};
    $scope.actualizaPOD = function(){actualizaPOD($scope)};
    $scope.actualizaEDU = function(){actualizaEDU($scope)};
    $scope.actualizaTAM = function () {
        calculapv($scope);
        calculabd($scope);
        calculacom($scope);
    };
    $scope.actualizaFUE = function () {
        calculabd($scope);
        calculacom($scope);
    };
    $scope.actualizaCON = function () {
        calculapv($scope);
    };
});

function calculapv($scope) {
    $scope.ficha.pv = Math.ceil((Number($scope.ficha.TAM) + Number($scope.ficha.CON)) / 20);
}

function calculabd($scope) {
    var ret = "-";
    var val = Number($scope.ficha.TAM) + Number($scope.ficha.FUE);
    if (val <= 64) {
        ret = "-2";
    } else if (val <= 85) {
        ret = "-1";
    } else if (val <= 124) {
        ret = "0";
    } else if (val <= 164) {
        ret = "+1d4";
    } else if (val <= 204) {
        ret = "+1d6";
    } else if (val > 204){
        ret = "Masivo (" + val + ")";
    }
    $scope.ficha.bd = ret;
}
function calculacom($scope) {
    var ret = "-";
    var val = Number($scope.ficha.TAM) + Number($scope.ficha.FUE);
    if (val <= 64) {
        ret = "-2";
    } else if (val <= 85) {
        ret = "-1";
    } else if (val <= 124) {
        ret = "0";
    } else if (val <= 164) {
        ret = "+1";
    } else if (val <= 204) {
        ret = "+2";
    } else if (val > 204){
        ret = "Masivo (" + val + ")";
    }
    $scope.ficha.com = ret;
}
function tirada(dados) {
    var m = dados.split("+");
    var n = m[0].split("D");
    var total = 0;
    for (var i = 0; i <= n[0]-1; i++)
        total += Math.floor(Math.random() * n[1] + 1);
    if (m[1]!=null)
        total +=Number(m[1]);
    total *= 5;
    return total;
}

function tirarand($scope) {
    $scope.ficha = {
        FUE: tirada('3D6'),
        DES: tirada('3D6'),
        INT: tirada('2D6+6'),
        CON: tirada('3D6'),
        APA: tirada('3D6'),
        POD: tirada('3D6'),
        TAM: tirada('2D6+6'),
        EDU: Math.min(99, tirada('3D6+3')),
        antropologia : 1,
        fusilescopeta : 20,
        armacorta : 25,
        arqueologia : 1,
        arteoficio : 5,
        buscarlibros : 20,
        cerrajeria : 1,
        charlataneria : 5,
        ciencia : 1,
        cienciasocultas : 5,
        conducirautomovil : 20,
        conducirmaquinaria : 1,
        contabilidad : 5,
        credito : 0,
        derecho : 5,
        descubrir : 25,
        discrecion : 20,
        disfrazar : 5,
        electricidad : 10,
        encanto : 15,
        equitacion : 5,
        escuchar : 20,
        historia : 5,
        historianatural : 10,
        intimidar : 15,
        lanzar : 20,
        lenguaotra : 1,
        lucha : 25,
        mecanica : 10,
        medicina : 1,
        mitosdecthulhu : 0,
        nadar : 20,
        orientacion : 10,
        persuasion : 10,
        pilotar : 1,
        prestidigitacion : 10,
        primerosauxilios : 30,
        psicoanalisis : 1,
        psicologia : 10,
        saltar : 20,
        seguirrastros : 10,
        supervivencia : 10,
        tasar : 5,
        trepar : 20,
        armasdefuego : 1
    };
        $scope.ficha.lenguaprop = "Inglés";
        $scope.ficha.lenguapropval = Math.round($scope.ficha.EDU);
        $scope.ficha.esquivar = Math.round($scope.ficha.DES/2);
        $scope.ficha.sonar = Math.round($scope.ficha.POD/5);
        $scope.ficha.saberonirico = Math.round($scope.ficha.mitosdecthulhu*2);

    actualizaEDU($scope);
    actualizaINT($scope);
    actualizaPOD($scope);
    calculapv($scope);
    calculabd($scope);
    calculacom($scope);
}

function actualizaINT($scope) {
    $scope.ficha.pi = $scope.ficha.INT*2;
}
function actualizaPOD($scope) {
    $scope.ficha.suerte = Math.min(99, $scope.ficha.POD);
    $scope.ficha.cordura = Math.min(99, $scope.ficha.POD);
    $scope.ficha.pm = $scope.ficha.POD/5;
}

function actualizaEDU($scope) {
    $scope.ficha.ph = $scope.ficha.EDU * 4;
    $scope.ficha.edad = Math.round(Number($scope.ficha.EDU)/5 + 6);
}

function reseteaficha(){
    return {
        FUE: 0,
        DES: 0,
        INT: 0,
        CON: 0,
        APA: 0,
        POD: 0,
        TAM: 0,
        EDU: 0,
        bd: 0,
        pv: 0,
        pm: 0,
        ph: 0,
        pi: 0,
        edad: 0,
        cordura: 0,
        suerte: 0,
        com: 0,
        antropologia : 1,
        fusilescopeta : 20,
        armacorta : 25,
        arqueologia : 1,
        arteoficio : 5,
        buscarlibros : 20,
        cerrajeria : 1,
        charlataneria : 5,
        ciencia : 1,
        cienciasocultas : 5,
        conducirautomovil : 20,
        conducirmaquinaria : 1,
        contabilidad : 5,
        credito : 0,
        derecho : 5,
        descubrir : 25,
        discrecion : 20,
        disfrazar : 5,
        electricidad : 10,
        encanto : 15,
        equitacion : 5,
        escuchar : 20,
        esquivar : 0,
        historia : 5,
        historianatural : 10,
        intimidar : 15,
        lanzar : 20,
        lenguaotra : 1,
        lenguaprop : "",
        lenguapropval : 0,
        lucha : 25,
        mecanica : 10,
        medicina : 1,
        mitosdecthulhu : 0,
        nadar : 20,
        orientacion : 10,
        persuasion : 10,
        pilotar : 1,
        prestidigitacion : 10,
        primerosauxilios : 30,
        psicoanalisis : 1,
        psicologia : 10,
        saltar : 20,
        seguirrastros : 10,
        supervivencia : 10,
        tasar : 5,
        trepar : 20,
        dormir : 0,
        sonar : 0,
        saberonirico:0,
        armasdefuego : 1
    };
}

