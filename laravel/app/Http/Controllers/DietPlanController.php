<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\DietPlan;

class DietPlanController extends Controller
{
    public function store(Request $request)
    {
        // Logic to store diet plan
    }

    public function show(DietPlan $dietPlan)
    {
        return view('dietplan.show', compact('dietPlan'));
    }
}
