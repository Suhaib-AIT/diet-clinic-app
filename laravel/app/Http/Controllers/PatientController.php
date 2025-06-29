<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Patient;
use App\Models\Appointment;
use App\Models\DietPlan;

class PatientController extends Controller
{
    public function dashboard()
    {
        return view('patient.dashboard');
    }

    // Methods for booking appointments and viewing plans
}
