import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Signup from "./pages/Signup";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/Login" element={<Login />} />

        <Route path="/" element={<Signup />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
