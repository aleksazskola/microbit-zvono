function zvono () {
    music.playTone(262, music.beat(BeatFraction.Breve))
}
radio.onReceivedValue(function (name, value) {
    if (name == "p1s") {
        p1s = value
    } else if (name == "p1m") {
        p1m = value
    } else if (name == "k1s") {
        k1s = value
    } else if (name == "k1m") {
        k1m = value
    } else if (name == "p2s") {
        p2s = value
    } else if (name == "p2m") {
        p2m = value
    } else if (name == "k2s") {
        k2s = value
    } else if (name == "k2m") {
        k2m = value
    } else if (name == "p3s") {
        p3s = value
    } else if (name == "p3m") {
        p3m = value
    } else if (name == "k3s") {
        k3s = value
    } else if (name == "k3m") {
        k3m = value
    } else if (name == "p4s") {
        p4s = value
    } else if (name == "p4m") {
        p4m = value
    } else if (name == "k4s") {
        k4s = value
    } else if (name == "k4m") {
        k4m = value
    } else if (name == "p5s") {
        p5s = value
    } else if (name == "p5m") {
        p5m = value
    } else if (name == "k5s") {
        k5s = value
    } else if (name == "k5m") {
        k5m = value
    } else if (name == "p6s") {
        p6s = value
    } else if (name == "p6m") {
        p6m = value
    } else if (name == "k6s") {
        k6s = value
    } else if (name == "k6m") {
        k6m = value
    } else if (name == "p7s") {
        p7s = value
    } else if (name == "p7m") {
        p7m = value
    } else if (name == "k7s") {
        k7s = value
    } else if (name == "k7m") {
        k7m = value
    } else if (name == "sati") {
        sati = value
    } else if (name == "minuti") {
        minuti = value
    } else if (name == "dan") {
        dan = value
    }
})
let sedmiKraj = ""
let sedmi = ""
let sestiKraj = ""
let sesti = ""
let petiKraj = ""
let peti = ""
let cetvrtiKraj = ""
let cetvrti = ""
let treciKraj = ""
let treci = ""
let drugiKraj = ""
let drugi = ""
let prviKraj = ""
let prvi = ""
let vreme = ""
let minuti = 0
let sati = 0
let k7m = 0
let k7s = 0
let p7m = 0
let p7s = 0
let k6m = 0
let k6s = 0
let p6m = 0
let p6s = 0
let k5m = 0
let k5s = 0
let p5m = 0
let p5s = 0
let k4m = 0
let k4s = 0
let p4m = 0
let p4s = 0
let k3m = 0
let k3s = 0
let p3m = 0
let p3s = 0
let k2m = 0
let k2s = 0
let p2m = 0
let p2s = 0
let k1m = 0
let k1s = 0
let p1m = 0
let p1s = 0
let dan = 0
radio.setGroup(220)
dan = 1
loops.everyInterval(60000, function () {
    minuti += 1
    if (minuti > 60) {
        sati += 1
        minuti = 0
        if (sati > 24) {
            sati = 0
            dan += 1
            if (dan > 7) {
                dan = 1
            }
        }
    }
    vreme = "" + sati + ":" + minuti
})
basic.forever(function () {
    prvi = "" + p1s + ":" + p1m
    prviKraj = "" + k1s + ":" + k1m
    drugi = "" + p2s + ":" + p2m
    drugiKraj = "" + k2s + ":" + k2m
    treci = "" + p3s + ":" + p3m
    treciKraj = "" + k3s + ":" + k3m
    cetvrti = "" + p4s + ":" + p4m
    cetvrtiKraj = "" + k4s + ":" + k4m
    peti = "" + p5s + ":" + p5m
    petiKraj = "" + k5s + ":" + k5m
    sesti = "" + p6s + ":" + p6m
    sestiKraj = "" + k6s + ":" + k6m
    sedmi = "" + p7s + ":" + p7m
    sedmiKraj = "" + k7s + ":" + k7m
    if (dan <= 5 && dan > 0) {
        if (vreme == (prvi || (prviKraj || (drugi || (drugiKraj || (treci || (treciKraj || (cetvrti || (cetvrtiKraj || (peti || (petiKraj || (sesti || (sestiKraj || (sedmi || sedmiKraj)))))))))))))) {
            zvono()
        }
    }
})
