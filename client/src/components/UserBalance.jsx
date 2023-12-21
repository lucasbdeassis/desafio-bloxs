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
    <div className='card' style={{ width: "18rem" }}>
      <div className='card-body'>
        <h5 className='card-title'>Total Balance</h5>
        <p className='card-text'>${balance}</p>
      </div>
    </div>
  );
}

export default UserBalance;
