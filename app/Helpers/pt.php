<?php
use Illuminate\Support\Facades\DB;

function master() {
    $data = DB::table('masters')->first();
    return $data;
}
function pengajuanBaru() {
    return DB::table('pengajuan')
            ->where('status', 0)
            ->count();
}
function pengajuanProses() {
    return DB::table('pengajuan')
            ->where('status', 1)
            ->count();
}
function laporanBaru() {
    return DB::table('laporan')
            ->where('status', 0)
            ->count();
}
function laporanProses() {
    return DB::table('laporan')
            ->where('status', 1)
            ->count();
}