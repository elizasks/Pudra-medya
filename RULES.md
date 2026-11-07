# Pudra — Otomatik Üretim Kuralları

Bu depo @pudradergi (Instagram) + "Pudra Dergi" (Facebook) için hazırlanan medyayı barındırır.
Metricool markası: blogId 7937594, saat dilimi Europe/Istanbul.

## Yayın akışı
1. Tasarımı `tools/` içindeki koddan üret (Python + Pillow + ffmpeg). `tools/pudra.py` renkler/logo, `tools/anim.py` animasyon motoru (render(), sticker, waving_flag, text_a, F fontları), `tools/illus.py` illüstrasyon örnekleri. `stories.py`, `flags_anim.py`, `bf_anim.py`, `manifesto2.py` örnek sayfa/story üretimleri.
2. Dosyayı ay klasörüne koy (ör. `2026-11/`), anlamlı adla (ör. `2026-11/g_1112_1.mp4`), commit + push.
3. Metricool'a ver: `https://raw.githubusercontent.com/elizasks/pudra-medya/main/<klasör>/<dosya>`
4. Postlar: providers instagram + facebook. Story: yalnızca instagram, type STORY, metin yok. Tek 4:5 video → IG REEL / FB REEL. Video carousel → IG POST / FB POST.
5. Tamamen otomatik yayın (draft: false, autoPublish: true). Kullanıcı onay beklemez.

## Hedef
- Para kazandırma + etkileşim odaklı. Her içerik kaydetme / paylaşma ("arkadaşına gönder") / yorum (numara/seçim sorusu) / takip hedefli.
- Özgünlük: İçeriğin çoğu Pudra'nın kendi tasarımı olmalı (Instagram 2026 aggregator kuralı). Başkasının görselini (film karesi, ünlü fotoğrafı, başka markanın posteri, filigranlı görsel) olduğu gibi KULLANMA.
- Konumlanma: "dürüst güzellik". Hedef kitle 20–60 yaş kadınlar. Konular: moda, güzellik, cilt bakımı, ilişkiler. Samimi ton.
- Seslendirme yok. Video sahipleri etiketlenmez / collab yapılmaz.
- "Bu hafta neler var" gibi haftayı listeleyen story YAPMA.

## Tempo
- Haftada 5 post + her gün 3 story (10:30 / 13:00 / 19:00).
- İki Reels arka arkaya gelmez; carousel ↔ Reels dönüşümlü.
- Saat: getBestTimeToPostByNetwork (genelde 10:00, ikinci tepe 18:00).
- Plana bakmadan önce getScheduledPosts ile mevcut planı kontrol et; dolu slotlara ekleme yapma, çakıştırma.

## Görsel stil
- RENKLİ ve HAREKETLİ: renkli zeminler (Berry #8E1048, Pembe #F4C6D4, Mürdüm #2A1520, Kırmızı #D62839, Krem #FBF6F7, Black Friday için Siyah #160E12) dönüşümlü; büyük daireler (nefes alan), parıltılar, nokta grid, dalga çizgisi, eğik sticker etiketler.
- Her carousel sayfası ve story 5–7 sn mp4. Öğeler sırayla kayarak/zıplayarak gelir. Her maddeye konusunu anlatan küçük illüstrasyon animasyonu.
- Font: Poppins Bold başlık, Poppins Regular/Medium metin, Lora Bold Italic tek vurgu kelime. (Instrument Serif KULLANMA — "okunmuyor".) Ok/emoji glifleri fontlarda yok, "›" kullan.
- Logo: assets/logo_A_klasik.png veya logo_B_berry.png; her zaman SOL ÜSTTE (post x56 y56 92px; story x56 y210).
- Post 1080×1350, story 1080×1920. Story'de metin alt 270px'e girmez.
- Carousel en fazla 6 sayfa.
- Gerçek fotoğraf tercih edilir: Fotoğraf arşivi bu depoda `photos/` altında (ayakkabi, canta, kombin, tirnak, varsa kisisel = Eliz'in kendi kombin fotoğrafları → "Editörün Stili"). Kullanılan fotoğrafları `photos/KULLANILANLAR.md` dosyasına tarih + dosya adıyla ekle ve mümkünse kullanılmamışları seç. Filigranlı/başkasına ait görseller arşive alınmadı.

## Strateji (7 Kasım 2026, "Pudra Büyüme ve Gelir Stratejisi" dokümanı)
- Vaat: "Filtresiz güzellik, akıllı stil, gerçek ilişkiler." Ses tonu: akıllı abla; yargılamaz, esprili, net tavsiye, "sen" diye hitap.
- Her kadına bir köşe: Her hafta 20'ler, 30'lar, 40'lar, 50+ gruplarının HER BİRİ en az bir post ya da story'de kendini görmeli (ör. "Aylık 500 TL'ye güzellik", "Sabah 7:45 formu", "40'tan sonra kimse söylemedi", "Kural yok, Pudra var").
- İmza seriler (her serinin sabit sticker adı):
  - Pazartesi 10:00 post: KIRMIZI BAYRAK (ilişki; "arkadaşına gönder")
  - Çarşamba 10:00 post: KANDIRILMAMAK İÇİN (rehber; kaydettirir; sahte indirim, içerik etiketi, cilt mitleri)
  - Cuma 10:00 post: YAŞ KÖŞESİ ("20'lerde / 40'larda bunu bil")
  - Salı/Perşembe/Cumartesi 18:00: PUDRA GÜNDEM (gündem görevi)
  - FİLTRESİZ (dürüst güzellik), EDİTÖRÜN STİLİ (Eliz'in fotoğrafları), HAFTA SONU MANİFESTOSU: slot boşsa post, değilse story olarak
  - OKURLARDAN: story sorularına gelen cevaplardan (kullanıcı paylaşırsa) anonim carousel
- Eliz'in hazır Reels videoları önceliklidir; varsa boş post slotlarına konur.
- Story ritmi: 10:30 günün içeriğine yönlendirme, 13:00 etkileşim (A/B, doğru-yanlış, soru), 19:00 kişisel/ilham.
- Facebook açıklaması 40+ kitle için biraz daha sıcak ve açıklayıcı olabilir (aynı gönderi, aynı metin kullanılabilir).
- Haftalık özetin sonuna Metricool analitiğinden 4 sayı ekle (getAnalyticsDataByMetrics): takip etmeyenlere erişim, kaydetme+paylaşım, profil ziyareti→takip, net takipçi artışı; en iyi ve en zayıf içeriği belirt.

## Gündem içerikleri
- Haber/trend içerikleri her zaman web araması ile doğrulanmış güncel bilgiye dayanır; kaynaklar açıklamada değil, kullanıcıya gönderilen özette listelenir.
- Ünlülerin fotoğrafları kullanılmaz; tipografik/illüstratif tasarım yapılır. Siyasi konular, trajediler, kesinleşmemiş dedikodular, sağlık iddiaları kullanılmaz.
- Açıklamada iddia edilen her bilgi kaynakta yazanla birebir uyumlu olmalı.
