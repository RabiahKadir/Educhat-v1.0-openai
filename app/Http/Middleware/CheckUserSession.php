<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class CheckUserSession
{

    public function handle($request, Closure $next, ...$levels)
    {
        if(isset($_COOKIE['hak_akses'])){
            if(in_array($_COOKIE['hak_akses'],$levels)){
                return $next($request);
            }
        }
        return redirect('/logout');
    }

}