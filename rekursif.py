def bagi_kartu(cards, players, distribusi, current_card=0):
    if current_card >= len(cards):
        return distribusi

    current_player = current_card % players
    distribusi[current_player].append(cards[current_card])

    return bagi_kartu(cards, players, distribusi, current_card + 1)

def main():
    banyak_pemain = int(input("Masukkan banyak pemain: "))
    kartu = list(range(1, 53))
    
    distribusi = [[] for _ in range(banyak_pemain)]
    distribusi = bagi_kartu(kartu, banyak_pemain, distribusi)

    for i, cards in enumerate(distribusi):
        print(f"Pemain {i + 1}: {cards}")

if __name__ == "__main__":
    main()