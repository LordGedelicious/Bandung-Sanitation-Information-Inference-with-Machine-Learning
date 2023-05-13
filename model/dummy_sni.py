import numpy as np
import pandas as pd
import random

# Total feature combinations:
# = (5 x 2) + (7 x 2) + (6 x 2) + (3 x 2 x 4 x 5 x 2 x 2 x 4)
# = 36960
total_rows = 100000

row_data = []

for row_id in range(total_rows):
    # Create row info about "tangki septik"
    tangkiSeptik_penggunaan = np.random.choice(["Berfungsi","Tidak Berfungsi","Berfungsi","Tidak Berfungsi",None])
    tangkiSeptik_penggunaan_num = 1 if tangkiSeptik_penggunaan == "Berfungsi" else 0
    tangkiSeptik_terawat = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    tangkiSeptik_terawat_num = 1 if tangkiSeptik_terawat == "Ya" else 0
    tangkiSeptik_bauTidakSedap = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    tangkiSeptik_bauTidakSedap_num = 0 if tangkiSeptik_bauTidakSedap == "Ya" else 1
    tangkiSeptik_ketercemaranLingkungan = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    tangkiSeptik_ketercemaranLingkungan_num = 0 if tangkiSeptik_ketercemaranLingkungan == "Ya" else 1
    tangkiSeptik_jarakDariSumberAir = round(random.uniform(0.0, 50.0), 2)
    tangkiSeptik_jarakDariSumberAir_num = 1 if tangkiSeptik_jarakDariSumberAir >= 15 else 0
    tangkiSeptik_overallScore = 0.3 * tangkiSeptik_penggunaan_num + 0.3 * tangkiSeptik_terawat_num + 0.05 * tangkiSeptik_bauTidakSedap_num + 0.15 * tangkiSeptik_ketercemaranLingkungan_num + 0.2 * tangkiSeptik_jarakDariSumberAir_num
    
    # Create row info about "sarana pembuangan BAB"
    saranaPembuanganBAB_penggunaan = np.random.choice(["Berfungsi","Tidak Berfungsi","Berfungsi","Tidak Berfungsi",None])
    saranaPembuanganBAB_penggunaan_num = 1 if saranaPembuanganBAB_penggunaan == "Berfungsi" else 0
    saranaPembuanganBAB_bangunanTerawat = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_bangunanTerawat_num = 1 if saranaPembuanganBAB_bangunanTerawat == "Ya" else 0
    saranaPembuanganBAB_adaDindingBangunan = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_adaDindingBangunan_num = 1 if saranaPembuanganBAB_adaDindingBangunan == "Ya" else 0
    saranaPembuanganBAB_adaVentilasiPintu = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_adaVentilasiPintu_num = 1 if saranaPembuanganBAB_adaVentilasiPintu == "Ya" else 0
    saranaPembuanganBAB_peneranganCukup = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_peneranganCukup_num = 1 if saranaPembuanganBAB_peneranganCukup == "Ya" else 0
    saranaPembuanganBAB_klosetLeherAngsa = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_klosetLeherAngsa_num = 1 if saranaPembuanganBAB_klosetLeherAngsa == "Ya" else 0
    saranaPembuanganBAB_adaAirBersih = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saranaPembuanganBAB_adaAirBersih_num = 1 if saranaPembuanganBAB_adaAirBersih == "Ya" else 0
    saranaPembuanganBAB_overallScore = 0.25 * saranaPembuanganBAB_penggunaan_num + 0.1 * saranaPembuanganBAB_bangunanTerawat_num + 0.1 * saranaPembuanganBAB_adaDindingBangunan_num + 0.05 * saranaPembuanganBAB_adaVentilasiPintu_num + 0.05 * saranaPembuanganBAB_peneranganCukup_num + 0.2 * saranaPembuanganBAB_klosetLeherAngsa_num + 0.25 * saranaPembuanganBAB_adaAirBersih_num
    
    # Create row info about "IPLT"
    iplt_penggunaan = np.random.choice(["Berfungsi","Tidak Berfungsi","Berfungsi","Tidak Berfungsi",None])
    iplt_penggunaan_num = 1 if iplt_penggunaan == "Berfungsi" else 0
    iplt_bangunanTerawat = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    iplt_bangunanTerawat_num = 1 if iplt_bangunanTerawat == "Ya" else 0
    iplt_bauTidakSedap = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    iplt_bauTidakSedap_num = 0 if iplt_bauTidakSedap == "Ya" else 1
    iplt_pencemaranLingkungan = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    iplt_pencemaranLingkungan_num = 0 if iplt_pencemaranLingkungan == "Ya" else 1
    iplt_airLimbahBerwarna = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    iplt_airLimbahBerwarna_num = 0 if iplt_airLimbahBerwarna == "Ya" else 1
    iplt_jarakDariPermukiman = round(random.uniform(0.0, 20.0), 2)
    iplt_jarakDariPermukiman_num = 1 if iplt_jarakDariPermukiman >= 5 else 0
    iplt_overallScore = 0.25 * iplt_penggunaan_num + 0.2 * iplt_bangunanTerawat_num + 0.05 * iplt_bauTidakSedap_num + 0.15 * iplt_pencemaranLingkungan_num + 0.15 * iplt_airLimbahBerwarna_num + 0.2 * iplt_jarakDariPermukiman_num
    
    # Create row info about "saluran drainase"
    saluranDrainase_hierarki = np.random.choice(["Primer","Sekunder","Tersier","Primer","Sekunder","Tersier",None])
    saluranDrainase_hierarki_num = 0.05
    saluranDrainase_jenis = np.random.choice(["Terbuka","Tertutup","Terbuka","Tertutup",None])
    saluranDrainase_jenis_num = 0.1
    saluranDrainase_bentukPenampang = np.random.choice(["Persegi", "Trapesiun", "Setengah Lingkaran", "Segitiga","Persegi", "Trapesiun", "Setengah Lingkaran", "Segitiga",None])
    saluranDrainase_bentukPenampang_num = 0.05
    saluranDrainase_perkerasanTepi = np.random.choice(["Pasir Halus","Lempung Kepasiran","Tanah","Kerikil Halus","Batuan","Pasir Halus","Lempung Kepasiran","Tanah","Kerikil Halus","Batuan",None])
    saluranDrainase_perkerasanTepi_num = 0.1 if saluranDrainase_perkerasanTepi in ["Kerikil Halus", "Batuan"] else 0
    saluranDrainase_kondisiDrainase = np.random.choice(["Terawat","Tidak Terawat","Terawat","Tidak Terawat",None])
    saluranDrainase_kondisiDrainase_num = 0.3 if saluranDrainase_kondisiDrainase == "Terawat" else 0
    saluranDrainase_bauTidakSedap = np.random.choice(["Ya","Tidak","Ya","Tidak",None])
    saluranDrainase_bauTidakSedap_num = 0 if saluranDrainase_bauTidakSedap == "Ya" else 0.1
    saluranDrainase_sedimentasiDrainase = np.random.choice(["Tidak Ada","Tanah","Sampah","Eceng Gondok","Tidak Ada","Tanah","Sampah","Eceng Gondok",None])
    saluranDrainase_sedimentasiDrainase_num = 0.3 if saluranDrainase_sedimentasiDrainase == "Tidak Ada" else 0
    saluranDrainase_overallScore = saluranDrainase_hierarki_num + saluranDrainase_jenis_num + saluranDrainase_bentukPenampang_num + saluranDrainase_perkerasanTepi_num + saluranDrainase_kondisiDrainase_num + saluranDrainase_bauTidakSedap_num + saluranDrainase_sedimentasiDrainase_num
    
    # Check results for classification process
    tangkiSeptik_class = "0" if tangkiSeptik_overallScore < 0.75 else "1"
    saranaPembuanganBAB_class = "0" if saranaPembuanganBAB_overallScore < 0.95 else "1"
    iplt_class = "0" if iplt_overallScore < 0.75 else "1"
    saluranDrainase_class = "0" if saluranDrainase_overallScore < 0.5 else "1"
    combined_class = tangkiSeptik_class + saranaPembuanganBAB_class + iplt_class + saluranDrainase_class
    
    row_data.append([row_id, tangkiSeptik_penggunaan, tangkiSeptik_terawat, tangkiSeptik_bauTidakSedap, tangkiSeptik_ketercemaranLingkungan, tangkiSeptik_jarakDariSumberAir,
                    saranaPembuanganBAB_penggunaan, saranaPembuanganBAB_bangunanTerawat, saranaPembuanganBAB_adaDindingBangunan, saranaPembuanganBAB_adaVentilasiPintu, saranaPembuanganBAB_peneranganCukup, saranaPembuanganBAB_klosetLeherAngsa, saranaPembuanganBAB_adaAirBersih,
                    iplt_penggunaan, iplt_bangunanTerawat, iplt_bauTidakSedap, iplt_pencemaranLingkungan, iplt_airLimbahBerwarna, iplt_jarakDariPermukiman,
                    saluranDrainase_hierarki, saluranDrainase_jenis, saluranDrainase_bentukPenampang, saluranDrainase_perkerasanTepi, saluranDrainase_kondisiDrainase, saluranDrainase_bauTidakSedap, saluranDrainase_sedimentasiDrainase,
                    combined_class])

columns=["ID","Tangki Septik_Penggunaan","Tangki Septik_Terawat","Tangki Septik_Bau Tidak Sedap","Tangki Septik_Ketercemaran Lingkungan","Tangki Septik_Jarak Dari Sumber Air (m)",
        "Sarana Pembuangan BAB_Penggunaan","Sarana Pembuangan BAB_Bangunan Terawat","Sarana Pembuangan BAB_Keberadaan Dinding Bangunan","Sarana Pembuangan BAB_Keberadaan Ventilasi Pintu","Sarana Pembuangan BAB_Penerangan yang Cukup","Sarana Pembuangan BAB_Terdapat Kloset Leher Angsa","Sarana Pembuangan BAB_Terdapat Sarana Air Bersih",
        "IPLT_Penggunaan","IPLT_Bangunan Terawat","IPLT_Bau Tidak Sedap","IPLT_Pencemaran Lingkungan","IPLT_Air Limbah Berwarna","IPLT_Jarak Dari Permukiman (km)",
        "Saluran Drainase_Hierarki Drainase","Saluran Drainase_Jenis Drainase","Saluran Drainase_Bentuk Penampang","Saluran Drainase_Perkerasan Tepi Drainase","Saluran Drainase_Kondisi Drainase","Saluran Drainase_Bau Tidak Sedap","Saluran Drainase_Sedimentasi Drainase",
        "Target Class"]
sni_df = pd.DataFrame(row_data, columns=columns)

sni_df.to_csv("data/sni.csv", sep=",", index=False)
print("Data created!")