import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch("/workouts")
      .then((r) => r.json())
      .then(setWorkouts);
  }, []);

  function handleDelete(id) {
    fetch(`/workouts/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setWorkouts((workouts) =>
          workouts.filter((workout) => workout.id !== id)
        );
      }
    });
  }

  return (
    <section className="container">
      {workouts.map((workout) => (
        <div key={workout.id} className="card">
          <h2>
            <Link to={`/workouts/${workout.id}`}>{workout.name}</Link>
          </h2>
          <p>Workout</p>
          <button onClick={() => handleDelete(workout.id)}>Delete</button>
        </div>
      ))}
    </section>
  );
}

export default Home;
