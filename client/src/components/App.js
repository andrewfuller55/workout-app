import { Route, Switch } from "react-router";
import Home from "./Home";
import Navbar from "./Navbar";
import Workout from "./Workout";

function App() {
  return (
    <>
      <Navbar />
      <Switch>
        <Route exact path="/workouts/:id">
          <Workout />
        </Route>
        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
    </>
  );
}

export default App;
