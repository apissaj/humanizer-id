# Pemetaan *Wikipedia:Signs of AI writing* (*WP:AISIGNS*) ke Kaidah Bahasa Indonesia & EYD V

Dokumen rujukan ini memetakan panduan lapangan [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (*WikiProject AI Cleanup*) ke pola bahasa Indonesia beserta landasan pedoman resmi Indonesia (**EYD Edisi V** SK No. 0424/I/BS.00.01/2022, **TBBBI Edisi IV**, Gorys Keraf *Diksi dan Gaya Bahasa* / *Komposisi*, dan Pamusuk Eneste *Buku Pintar Penyuntingan Naskah*).

---

## 1. Tabel Pemetaan Pola & ID Aturan (`AIS-001`..`AIS-010`)

| ID | Kategori *WP:AISIGNS* | Wujud Khas di Bahasa Indonesia | Landasan Indonesia | Tipe |
|---|---|---|---|---|
| `AIS-001` | *Superficial `-ing` analyses* | `..., menyoroti pentingnya...`, `..., menggarisbawahi peran vital...`, `..., memastikan integrasi yang mulus...` | Keraf (*Argumentasi dan Narasi*): klaim wajib ditopang bukti, bukan ekor pernyataan kosong | Regex aktif |
| `AIS-002` | *Vague attributions* (*weasel words*) | `para ahli berpendapat`, `banyak pengamat menilai`, `laporan industri menunjukkan`, `beberapa kritikus berargumen` | Keraf (*Komposisi*): kejelasan sumber dan atribusi rujukan | Regex aktif |
| `AIS-003` | *Didactic filler / disclaimers* | `penting untuk dicatat bahwa`, `perlu diingat bahwa`, `tak dapat dipungkiri bahwa` | Ekonomi Kata Tempo & TBBBI: pangkas pengantar penunda fakta | Regex aktif |
| `AIS-004` | *Chatbot leftovers & sycophantic tone* | `Tentu, berikut...`, `Pertanyaan yang bagus`, `Semoga membantu!`, `berdasarkan pengetahuan terakhir saya` | Eneste (*Penyuntingan Naskah*): kebersihan naskah dari artefak di luar teks | Regex aktif |
| `AIS-005` | *Puffery & significance inflation* | `menjadi bukti nyata atas`, `berdiri sebagai simbol`, `menandai tonggak bersejarah`, `meninggalkan jejak abadi` | Keraf (*Diksi dan Gaya Bahasa*): ragam denotatif-netral bebas hiperbola | Regex aktif |
| `AIS-006` | *Negative parallelisms* | `bukan sekadar X, melainkan sebuah Y` (berulang sebagai bingkai retoris) | Badudu & TBBBI: hindari kontras retoris paksaan pada paparan informatif | Regex aktif |
| `AIS-007` | *Challenges & future prospects boilerplate* | `Meskipun memiliki banyak kelebihan, X menghadapi sejumlah tantangan`, `prospek masa depan yang cerah` | Keraf (*Komposisi*): simpulan harus spesifik terhadap data, bukan templat umum | Regex aktif |
| `AIS-008` | *Em-dash formatting tell* | ` — ` (tanda pisah em-dash berspasi khas keluaran LLM) | **EYD Edisi V** (Tanda Pisah): tanda pisah (`—`) ditulis **tanpa spasi** mengapit (`kata—kata`) | Regex aktif |
| `AIS-009` | *Synonym cycling & false ranges* | Mengganti nomina yang sama tiap kalimat (*sistem ini* → *platform tersebut* → *arsitektur mutakhir itu*); rentang semu *mulai dari X hingga Y* | Keraf (*Diksi dan Gaya Bahasa*): konsistensi istilah teknis & presisi perincian | `[telaah]` |
| `AIS-010` | *Rule of three & AI formatting tells* | Pola tiga kata sifat mekanis tiap paragraf, daftar ber-**boldface** di tiap kepala butir, *Title Case* ala Inggris di subjudul Indonesia, emoji di naskah formal | **EYD Edisi V** (Huruf Kapital Judul & Huruf Tebal) & Eneste | `[telaah]` |

---

## 2. Catatan Penerapan Editorial

- Sebagaimana ditegaskan oleh *WP:AISIGNS*, satu tanda tunggal bukan bukti mutlak teks ditulis AI; penilaian dilakukan secara kolektif berdasarkan kepadatan pola, hilangnya bukti spesifik, dan ketidaksesuaian dengan kaidah bahasa Indonesia baku.
- Pada `AIS-008`, tanda pisah EYD V (`—`) tetap sah digunakan untuk menyisipkan keterangan aposisi di tengah kalimat **tanpa spasi** (`Pengujian dilakukan dua kali—pada pagi dan sore hari—untuk menjaga keandalan.`).
