def zvono():
    music.play_tone(262, music.beat(BeatFraction.BREVE))

def on_received_value(name, value):
    global p1s, p1m, k1s, k1m, p2s, p2m, k2s, k2m, p3s, p3m, k3s, k3m, p4s, p4m, k4s, k4m, p5s, p5m, k5s, k5m, p6s, p6m, k6s, k6m, p7s, p7m, k7s, k7m, sati, minuti, dan
    if name == "p1s":
        p1s = value
    elif name == "p1m":
        p1m = value
    elif name == "k1s":
        k1s = value
    elif name == "k1m":
        k1m = value
    elif name == "p2s":
        p2s = value
    elif name == "p2m":
        p2m = value
    elif name == "k2s":
        k2s = value
    elif name == "k2m":
        k2m = value
    elif name == "p3s":
        p3s = value
    elif name == "p3m":
        p3m = value
    elif name == "k3s":
        k3s = value
    elif name == "k3m":
        k3m = value
    elif name == "p4s":
        p4s = value
    elif name == "p4m":
        p4m = value
    elif name == "k4s":
        k4s = value
    elif name == "k4m":
        k4m = value
    elif name == "p5s":
        p5s = value
    elif name == "p5m":
        p5m = value
    elif name == "k5s":
        k5s = value
    elif name == "k5m":
        k5m = value
    elif name == "p6s":
        p6s = value
    elif name == "p6m":
        p6m = value
    elif name == "k6s":
        k6s = value
    elif name == "k6m":
        k6m = value
    elif name == "p7s":
        p7s = value
    elif name == "p7m":
        p7m = value
    elif name == "k7s":
        k7s = value
    elif name == "k7m":
        k7m = value
    elif name == "sati":
        sati = value
    elif name == "minuti":
        minuti = value
    elif name == "dan":
        dan = value
radio.on_received_value(on_received_value)

sedmiKraj = ""
sedmi = ""
sestiKraj = ""
sesti = ""
petiKraj = ""
peti = ""
cetvrtiKraj = ""
cetvrti = ""
treciKraj = ""
treci = ""
drugiKraj = ""
drugi = ""
prviKraj = ""
prvi = ""
vreme = ""
dan = 0
minuti = 0
sati = 0
k7m = 0
k7s = 0
p7m = 0
p7s = 0
k6m = 0
k6s = 0
p6m = 0
p6s = 0
k5m = 0
k5s = 0
p5m = 0
p5s = 0
k4m = 0
k4s = 0
p4m = 0
p4s = 0
k3m = 0
k3s = 0
p3m = 0
p3s = 0
k2m = 0
k2s = 0
p2m = 0
p2s = 0
k1m = 0
k1s = 0
p1m = 0
p1s = 0
radio.set_group(220)

def on_every_interval():
    global minuti, sati, dan, vreme
    minuti += 1
    if minuti > 60:
        sati += 1
        minuti = 0
        if sati > 24:
            sati = 0
            dan += 1
            if dan > 7:
                dan = 1
    vreme = "" + str(sati) + ":" + str(minuti)
loops.every_interval(60000, on_every_interval)

def on_forever():
    global prvi, prviKraj, drugi, drugiKraj, treci, treciKraj, cetvrti, cetvrtiKraj, peti, petiKraj, sesti, sestiKraj, sedmi, sedmiKraj
    prvi = "" + str(p1s) + ":" + str(p1m)
    prviKraj = "" + str(k1s) + ":" + str(k1m)
    drugi = "" + str(p2s) + ":" + str(p2m)
    drugiKraj = "" + str(k2s) + ":" + str(k2m)
    treci = "" + str(p3s) + ":" + str(p3m)
    treciKraj = "" + str(k3s) + ":" + str(k3m)
    cetvrti = "" + str(p4s) + ":" + str(p4m)
    cetvrtiKraj = "" + str(k4s) + ":" + str(k4m)
    peti = "" + str(p5s) + ":" + str(p5m)
    petiKraj = "" + str(k5s) + ":" + str(k5m)
    sesti = "" + str(p6s) + ":" + str(p6m)
    sestiKraj = "" + str(k6s) + ":" + str(k6m)
    sedmi = "" + str(p7s) + ":" + str(p7m)
    sedmiKraj = "" + str(k7s) + ":" + str(k7m)
    if dan <= 5 and dan > 0:
        if vreme == (prvi or (prviKraj or (drugi or (drugiKraj or (treci or (treciKraj or (cetvrti or (cetvrtiKraj or (peti or (petiKraj or (sesti or (sestiKraj or (sedmi or sedmiKraj))))))))))))):
            pass
basic.forever(on_forever)
