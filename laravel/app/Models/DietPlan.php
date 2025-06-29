<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class DietPlan extends Model
{
    protected $fillable = [
        'patient_id', 'doctor_id', 'description'
    ];

    public function patient()
    {
        return $this->belongsTo(Patient::class);
    }

    public function doctor()
    {
        return $this->belongsTo(Doctor::class);
    }
}
