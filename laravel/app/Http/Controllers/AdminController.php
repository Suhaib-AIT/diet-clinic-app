<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Doctor;
use App\Models\Patient;
use App\Models\User;

class AdminController extends Controller
{
    public function dashboard()
    {
        return view('admin.dashboard');
    }

    // Additional CRUD methods would go here
}
