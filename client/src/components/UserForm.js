import { useEffect, useState } from "react";
// import { useFormik } from 'formik'
// import * as yup from 'yup'

function UserForm({ workoutId, onAddUser }) {
  const [users, setUsers] = useState([]);
  const [userId, setUserId] = useState("");
  const [sets, setSets] = useState("");
  const [formErrors, setFormErrors] = useState([]);

  useEffect(() => {
    fetch("/users")
      .then((r) => r.json())
      .then(setUsers);
  }, []);


  // const initialValues = {
  //   name: ""
  // }

  // const validationSchema = yup.object({
  //   name: yup.string().min(3).max(50).required()
  // })



  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      user_id: userId,
      workout_id: workoutId,
      sets,
    };
    fetch("/user_plans", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        r.json().then((newUserPlan) => {
          onAddUser(newUserPlan);
          setFormErrors([]);
        });
      } else {
        r.json().then((err) => setFormErrors(err.errors));
      }
    });
  }
  // const formik = useFormik({
  //   initialValues,
  //   validationSchema,
  //   onSubmit: handleSubmit,
  //   validateOnChange: false
  // })



  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="user_id">User:</label>
      <select
        id="user_id"
        name="user_id"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      >
        <option value="">Select a user</option>
        {users.map((user) => (
          <option key={user.id} value={user.id}>
            {user.name}
          </option>
        ))}
      </select>
      <label htmlFor="user_id">Sets:</label>
      <input
        id="sets"
        name="sets"
        type="number"
        value={sets}
        onChange={(e) => setSets(parseInt(e.target.value))}
      />
      {formErrors.length > 0
        ? formErrors.map((err) => (
            <p key={err} style={{ color: "red" }}>
              {err}
            </p>
          ))
        : null}
      <button type="submit">Add To Workout</button>
    </form>
  );
}

export default UserForm;
