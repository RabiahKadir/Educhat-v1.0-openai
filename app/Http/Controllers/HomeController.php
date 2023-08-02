<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Crypt;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Mail;
use PHPMailer\PHPMailer\PHPMailer;  
use PHPMailer\PHPMailer\Exception;

use App\Models\Home;

class HomeController extends Controller
{
    public function __construct() {
        $this->Home = new Home;
    }

    public function index()
    {
        return view('chat');
    }
    public function ChatPost(Request $request)
    {

		$myfile = fopen("db.txt", "w");
        fwrite($myfile, $request->teks);
        fclose($myfile);
        exec('C:/Users/Administrator/AppData/Local/Programs/Python/Python311/python3.exe userinput.py', $output2);

        $myfile2 = fopen("db_main.txt", "w");
        fwrite($myfile2, $output2[0]);
        fclose($myfile2);
        exec('C:/Users/Administrator/AppData/Local/Programs/Python/Python311/python3.exe main.py', $output);
        // $type= $output[3];
        // $tag= $output[7];
        // $subject= $output[8];
        // $predicate= $output[9];
        // $object= $output[10];

        $type= '';
        $tag= '';
        $subject= '';
        $predicate= '';
        $object= '';
        
        // print_r($output);die;

        DB::table('tbl_querydescription')->insert([
            'query'         => $output2[0],
            'type'          => $type,
            'tag'           => $tag,
            'subject'       => $subject,
            'predicate'     => $predicate,
            'object'        => $object,
        ]);

        $data['input'] = $request->teks;
        $data['output'] = $output;

        return view('chat', $data);
    }

    
}
