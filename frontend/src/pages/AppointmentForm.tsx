import { FormEvent, useState } from 'react';

const AppointmentForm = () => {
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [notes, setNotes] = useState('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    alert(`Appointment requested on ${date} at ${time}. Notes: ${notes}`);
  };

  return (
    <div className="appointment-form">
      <h1>Book Appointment</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Date:
            <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
          </label>
        </div>
        <div>
          <label>
            Time:
            <input type="time" value={time} onChange={(e) => setTime(e.target.value)} />
          </label>
        </div>
        <div>
          <label>
            Notes:
            <textarea value={notes} onChange={(e) => setNotes(e.target.value)} />
          </label>
        </div>
        <button type="submit">Book</button>
      </form>
    </div>
  );
};

export default AppointmentForm;
