import random
import time

# Basit bir UFO sınıfı oluşturuyoruz
class UFO:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ufo_tespiti_veri_hizi():
    while True:
        # Rastgele bir veri akışı oluşturun (örneğin, x ve y koordinatları)
        x_koordinati = random.uniform(0, 100)
        y_koordinati = random.uniform(0, 100)

        # Algılanan UFO hakkında bilgiyi yazdırın
        print(f"Algılanan UFO: X={x_koordinati}, Y={y_koordinati}")

        # UFO nesnesini oluşturun
        ufo = UFO(x_koordinati, y_koordinati)

        # UFO'ya mesaj gönder
        mesaj_gonder(ufo)

        # Belirli bir süre aralığıyla veri akışını güncellemek için bekleyin
        time.sleep(1)  # 1 saniye bekleyin (bu süreyi ihtiyaca göre ayarlayabilirsiniz)

def mesaj_gonder(ufo):
    # Bu işlev, algılanan UFO'ya bir mesaj göndermek için kullanılabilir
    # Burada, uygulamanıza uygun bir iletişim mekanizması uygulamalısınız
    # Örneğin, bir veritabanına kaydedebilir veya bir ağ üzerinden iletişim kurabilirsiniz.
    print(f"UFO'ya mesaj gönderildi: X={ufo.x}, Y={ufo.y}")

def main():
    # Kullanıcıdan onay al
    izin = input("UFO tespiti veri hızıyla gerçekleştirilsin mi? (E/H) ").strip().lower()

    if izin == "e":
        ufo_tespiti_veri_hizi()

    else:
        print("UFO tespiti veri hızıyla gerçekleştirilmedi. Program sonlandırılıyor.")

if __name__ == "__main__":
    main()
