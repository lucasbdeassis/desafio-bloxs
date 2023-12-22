import React, { useState, useEffect } from "react";

function UserBalance() {
  const [balance, setBalance] = useState(0);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/accounts", {
      headers: {
        Authorization: sessionStorage.getItem("userToken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        const totalBalance = data.reduce(
          (total, account) => total + account.balance,
          0
        );
        setBalance(totalBalance);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div className='container'>
      <div class='card'>
        <div class='card-header'>Saldo</div>
        <div class='card-body'>
          <h5 class='card-title'>Total:</h5>
          <p class='card-text'>
            <strong>${(balance / 100).toFixed(2)}</strong>
          </p>
        </div>
      </div>
    </div>
  );
}

export default UserBalance;
