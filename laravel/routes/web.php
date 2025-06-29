<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AdminController;
use App\Http\Controllers\DoctorController;
use App\Http\Controllers\PatientController;
use App\Http\Controllers\AppointmentController;
use App\Http\Controllers\DietPlanController;

Route::get('/', function () {
    return view('welcome');
});

Route::middleware(['auth'])->group(function () {
    Route::get('/admin', [AdminController::class, 'dashboard'])->middleware('role:admin');
    Route::get('/doctor', [DoctorController::class, 'dashboard'])->middleware('role:doctor');
    Route::get('/patient', [PatientController::class, 'dashboard'])->middleware('role:patient');

    Route::resource('appointments', AppointmentController::class)->except(['create', 'edit']);
    Route::resource('diet-plans', DietPlanController::class)->only(['store', 'show']);
});

require __DIR__.'/auth.php';
