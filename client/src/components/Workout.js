import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import UserForm from "./UserForm";

function Home() {
  const [{ data: workout, error, status }, setWorkout] = useState({
    data: null,
    error: null,
    status: "pending",
  });
  const { id } = useParams();

  useEffect(() => {
    fetch(`/workouts/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((workout) =>
          setWorkout({ data: workout, error: null, status: "resolved" })
        );
      } else {
        r.json().then((err) =>
          setWorkout({ data: null, error: err.error, status: "rejected" })
        );
      }
    });
  }, [id]);

  function handleAddUser(newUserPlan) {
    setWorkout({
      data: {
        ...workout,
        user_plans: [
          ...workout.user_plans,
          newUserPlan,
        ],
      },
      error: null,
      status: "resolved",
    });
  }

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error.error}</h1>;

  return (
    <section className="container">
      <div className="card">
        <h1>{workout.name}</h1>
        <p>Workout</p>
      </div>
      <div className="card">
        <h2>User</h2>
        {workout.user_plans.map((user_plan) => (
          <div key={user_plan.user.id}>
            <h3>{user_plan.user.name}</h3>
            <p>
              <em>Sets: {user_plan.sets}</em>
            </p>
          </div>
        ))}
      </div>
      <div className="card">
        <h3>Add New User</h3>
        <UserForm workoutId={workout.id} onAddUser={handleAddUser} />
      </div>
    </section>
  );
}

export default Home;
