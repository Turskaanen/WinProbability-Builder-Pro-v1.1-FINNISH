def voiton_todennakoisyys_rakentaja():
    print("\n🎯 VOITON TODENNÄKÖISYYSRAKENTAJA – PRO v1.1\n")

    try:
        xg_koti = float(input("⚽ Kotijoukkueen xG: "))
        xg_vieras = float(input("⚽ Vierasjoukkueen xG: "))
        voitot_koti = int(input("✅ Kotijoukkueen voitot (viimeiset 5): "))
        tasapelit_koti = int(input("➖ Kotijoukkueen tasapelit (viimeiset 5): "))
        tappiot_koti = int(input("❌ Kotijoukkueen tappiot (viimeiset 5): "))
        voitot_vieras = int(input("✅ Vierasjoukkueen voitot (viimeiset 5): "))
        tasapelit_vieras = int(input("➖ Vierasjoukkueen tasapelit (viimeiset 5): "))
        tappiot_vieras = int(input("❌ Vierasjoukkueen tappiot (viimeiset 5): "))
        loukkaantumiset_koti = int(input("🤕 Kotijoukkueen loukkaantumiset (määrä): "))
        loukkaantumiset_vieras = int(input("🤕 Vierasjoukkueen loukkaantumiset (määrä): "))
        kerroin_koti = float(input("💰 Kotivoiton kerroin: "))
        panos = float(input("💸 Panos (€): "))
    except ValueError:
        print("⚠️ Syötä vain numeroita.")
        return

    # xG-ero
    xg_ero = xg_koti - xg_vieras
    xg_pisteet = min(max((xg_ero + 1) / 2, 0), 1)

    # Formilaskenta
    formi_koti = (voitot_koti * 3 + tasapelit_koti * 1) / 15
    formi_vieras = (voitot_vieras * 3 + tasapelit_vieras * 1) / 15
    formi_pisteet = min(max((formi_koti - formi_vieras + 1) / 2, 0), 1)

    # Loukkaantumispenaltti
    penaltti = max((loukkaantumiset_koti - loukkaantumiset_vieras) * 0.02, -0.2)
    loukkaantumis_pisteet = max(0, 1 + penaltti)

    # Yhdistetty todennäköisyys
    raakap = (xg_pisteet * 0.4) + (formi_pisteet * 0.4) + (loukkaantumis_pisteet * 0.2)
    todennakoisyys = min(max(raakap, 0.01), 0.99)

    # Rajakerroin
    rajakerroin = 1 / todennakoisyys
    value_bet = kerroin_koti > rajakerroin

    # EV & Kelly
    voitto = (panos * kerroin_koti) - panos
    tappio = -panos
    ev = (todennakoisyys * voitto) + ((1 - todennakoisyys) * tappio)
    kelly = ((kerroin_koti * todennakoisyys) - (1 - todennakoisyys)) / kerroin_koti
    kelly_panos = panos * kelly if kelly > 0 else 0

    # Luotettavuusindeksi
    luotettavuus = round((xg_pisteet + formi_pisteet + loukkaantumis_pisteet) / 3 * 100, 1)

    print("\n📊 TULOKSET:")
    print(f"- Arvioitu voittotodennäköisyys: {todennakoisyys*100:.2f} %")
    print(f"- Rajakerroin: {rajakerroin:.2f}")
    print(f"- Value bet: {'KYLLÄ ✅' if value_bet else 'EI ❌'}")
    print(f"- EV (odotusarvo): {ev:.2f} €")
    print(f"- Kelly-panos: {kelly_panos:.2f} €")
    print(f"- Luotettavuusindeksi: {luotettavuus}/100")

    print("\n💡 SUOSITUS:")
    if value_bet and ev > 0:
        print("✅ PANOSTA – value bet löydetty.")
    else:
        print("❌ ÄLÄ PANOSTA – ei kannattava.")

voiton_todennakoisyys_rakentaja()
