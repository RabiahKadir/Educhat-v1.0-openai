<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Crypt;

class Home extends Model
{
    use HasFactory;

    public function Kec()
    {
        return DB::table('kec')
        ->get();
    }

    public function Kel()
    {
        return DB::table('kel')
        ->get();
    }
    public function Lpju()
    {
        return DB::table('lampu_pju AS a')
            ->select('a.lat', 'a.lon', 'status', 'a.alamat', 'd.merek')
            // ->select('a.*', 'b.kategori', 'c.jenis', 'd.merek', 'e.daya', 'f.kontruksi', 'g.jenis_kabel', 'h.ukuran_kabel')
            // ->join('kategori AS b', 'a.kategori_id', '=', 'b.id')
            // ->join('jenis AS c', 'a.jenis_id', '=', 'c.id')
            ->join('merek AS d', 'a.merek_id', '=', 'd.id')
            // ->join('daya AS e', 'a.daya_id', '=', 'e.id')
            // ->join('kontruksi AS f', 'a.kontruksi_id', '=', 'f.id')
            // ->join('jenis_kabel AS g', 'a.jenis_kabel_id', '=', 'g.id')
            // ->join('ukuran_kabel AS h', 'a.ukuran_kabel_id', '=', 'h.id')
            ->get();
    }
    public function LpjuKot()
    {
        return DB::table('lampu_pju AS a')
            ->select('a.*', 'b.kategori', 'c.jenis', 'd.merek', 'e.daya', 'f.kontruksi', 'g.jenis_kabel', 'h.ukuran_kabel')
            ->join('kategori AS b', 'a.kategori_id', '=', 'b.id')
            ->join('jenis AS c', 'a.jenis_id', '=', 'c.id')
            ->join('merek AS d', 'a.merek_id', '=', 'd.id')
            ->join('daya AS e', 'a.daya_id', '=', 'e.id')
            ->join('kontruksi AS f', 'a.kontruksi_id', '=', 'f.id')
            ->join('jenis_kabel AS g', 'a.jenis_kabel_id', '=', 'g.id')
            ->join('ukuran_kabel AS h', 'a.ukuran_kabel_id', '=', 'h.id')
            ->paginate(10);
    }
    public function LpjuDetail($id, $mer, $kat)
    {
        return DB::table('lampu_pju AS a')
            ->select('a.*', 'b.kategori', 'c.jenis', 'd.merek', 'e.daya', 'f.kontruksi', 'g.jenis_kabel', 'h.ukuran_kabel', 'i.kec', 'j.kel')
            ->join('kategori AS b', 'a.kategori_id', '=', 'b.id')
            ->join('jenis AS c', 'a.jenis_id', '=', 'c.id')
            ->join('merek AS d', 'a.merek_id', '=', 'd.id')
            ->join('daya AS e', 'a.daya_id', '=', 'e.id')
            ->join('kontruksi AS f', 'a.kontruksi_id', '=', 'f.id')
            ->join('jenis_kabel AS g', 'a.jenis_kabel_id', '=', 'g.id')
            ->join('ukuran_kabel AS h', 'a.ukuran_kabel_id', '=', 'h.id')
            ->join('kec AS i', 'a.kec_id', '=', 'i.id')
            ->join('kel AS j', 'a.kel_id', '=', 'j.id')
            ->where('a.id', $id)
            ->first();
    }
    public function Kontruksi()
    {
        return DB::table('kontruksi')
        ->get();
    }
    public function KontruksiCount()
    {
        return DB::table('kontruksi')
        ->count();
    }
    public function KontruksiData()
    {
        return DB::table('lampu_pju')
        ->get();
    }

    public function HomeKelData()
    {
        return DB::table('lampu_pju')
        ->select('kel_id')
        ->selectRaw('sum(jumlah) AS total')
        ->groupBy('kel_id')
        ->get();
    }

    public function HomeKecamatanData()
    {
        return DB::table('lampu_pju')
        ->select('kec_id')
        ->selectRaw('sum(jumlah) AS total')
        ->groupBy('kec_id')
        ->get();
    }

    public function allTotal()
    {
        return DB::table('lampu_pju')
        ->selectRaw('sum(jumlah) AS allTotal')
        ->first();
    }

    public function hidupTotal()
    {
        return DB::table('lampu_pju')
        ->selectRaw('sum(jumlah) AS hidupTotal')
        ->where('status', 1)
        ->first();
    }

    public function matiTotal()
    {
        return DB::table('lampu_pju')
        ->selectRaw('sum(jumlah) AS matiTotal')
        ->where('status', 0)
        ->first();
    }

    public function laporanPeta()
    {
        return DB::table('laporan')
            ->get();
    }
    public function LaporanData()
    {
        return DB::table('laporan')
            ->orderBy('id', 'DESC')
            ->paginate('10');
    }
    public function LaporanDataDetail($id)
    {
        return DB::table('laporan')
            ->where('id', $id)
            ->first();
    }
    public function LaporanDataTanggapan($id)
    {
        return DB::table('tanggapan')
            ->where('laporan_id', $id)
            ->get();
    }
}
