# Diet Clinic Backend

This repository contains a minimal FastAPI backend for a diet clinic management application.
It uses SQLite for persistence and JWT for authentication.

## Features
- User roles: admin, dietitian, patient
- Models: User, Appointment, DietPlan, FoodLog
- JWT login system
- Docker support

## Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Docker
Build and run the image:
```bash
docker build -t diet-clinic .
docker run -p 8000:8000 diet-clinic
```
