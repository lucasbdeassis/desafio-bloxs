import React, { useState } from "react";

function LoginView() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [erroMessage, setErrorMessage] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        const data = await response.json();
        sessionStorage.setItem("userToken", data.token);
        window.location.reload();
      }
    } catch (error) {
      if (error.response && error.response.status === 401) {
        console.log("Unauthorized");
        setErrorMessage("Usuário ou senha inválidos");
        sessionStorage.setItem("userToken", data.token);
        window.location.reload();
      } else {
        console.error("Error:", error);
        setErrorMessage("Erro ao realizar login");
        sessionStorage.setItem("userToken", data.token);
        window.location.reload();
      }
    }
  };

  return (
    <>
      <div className='container mt-5' style={{ maxWidth: "400px" }}>
        <form onSubmit={handleSubmit}>
          <div className='mb-3'>
            <label htmlFor='exampleInputEmail1' className='form-label'>
              Email address
            </label>
            <input
              type='email'
              className='form-control'
              id='exampleInputEmail1'
              aria-describedby='emailHelp'
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
          </div>
          <div className='mb-3'>
            <label htmlFor='exampleInputPassword1' className='form-label'>
              Password
            </label>
            <input
              type='password'
              className='form-control'
              id='exampleInputPassword1'
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
          </div>
          <button type='submit' className='btn btn-primary'>
            Submit
          </button>
        </form>
        <div>{erroMessage}</div>
      </div>
    </>
  );
}

export default LoginView;
